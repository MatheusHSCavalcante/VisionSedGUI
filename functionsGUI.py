import pathlib
import subprocess
import time
from datetime import datetime
import re
from itertools import cycle
import threading
import cv2
import keyboard
from PyQt5.QtCore import pyqtSignal

from imagegrains import grainsizing, plotting, segmentation_helper, data_loader, gsd_uncertainty
from cellpose import io
import pandas as pd
import os
from PIL import Image, ImageTk
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from GUI.uiVisionSedGUI import *
import matplotlib.pyplot as plt
import torch
import shutil
from pathlib import Path
from ultralytics import YOLO
from motrackers import *
from PySide6.QtGui import QPainter, QPen,QIcon,QKeyEvent
import warnings
from PySide6.QtMultimediaWidgets import *
from PySide6.QtMultimedia import *
from PySide6.QtCore import QUrl, Qt, QTimer
import time
from ultralytics import YOLO
import moviepy.editor
warnings.simplefilter('ignore', UserWarning)
import math
class TrainThread(QThread):

    training_finished_train = Signal(str)

    def __init__(self, directory, model,nepochs):
        super().__init__()
        self.directory = directory
        self.model = model
        self.nepochs_model = nepochs

    def run(self):
        train_images, train_masks, test_images, test_masks = data_loader.find_data(self.directory)
        segmentation_helper.check_labels(train_masks)
        segmentation_helper.check_labels(test_masks)
        segmentation_helper.check_im_label_pairs(train_images, train_masks)
        segmentation_helper.check_im_label_pairs(test_images, test_masks)

        if self.model:
            model_path = self.model
        else:
            model_path = "nuclei"

        train_path = self.directory + "/" + "train" + "/"
        test_path = self.directory + "/" + "test" + "/"
        mask_filter = '_mask'
        train_str = f'python -m cellpose --use_gpu --verbose --train --dir {train_path} --test_dir {test_path} --pretrained_model {model_path} --mask_filter {mask_filter} --n_epochs {self.nepochs_model}'
        print(train_str)
        training = subprocess.check_output(train_str, shell=True)
        decoded_output = training.decode()
        print(decoded_output)
        self.training_finished_train.emit(decoded_output)


class SegThread(QThread):

    segmentation_finished = Signal(str)
    data_ready = Signal(list)

    def __init__(self, directory, model):
        super().__init__()
        self.directory = directory
        self.model = model

    def run(self):
        global segment
        if not os.path.exists(self.directory + 'prediction_masks'):
            segmentation_helper.predict_dataset(self.directory, self.model, image_format="jpg", mute=True,
                                                return_results=False, save_masks=True, do_subfolders=False)
            segment="confirm"
        imgs, lbls, preds = data_loader.dataset_loader(self.directory, label_str='mask', pred_str='pred')


        self.data_ready.emit([imgs, lbls, preds,self.directory])

        decode_output_seg = segment
        self.segmentation_finished.emit(decode_output_seg)

class MeasureThread(QThread):

    measure_finished = Signal(str)

    def __init__(self,directory,filters,parameters):

        super().__init__()

        self.directory = directory
        self.filters = filters
        self.parameters = parameters

    def run(self):

        global grid_resampled_real,grid_resampled_pred,str_model

        for file in os.listdir(self.directory):
            name, extension = os.path.splitext(file)
            if extension[1:].isdigit():
                str_model = name + "_pred"

        filters_values = self.filters

        imgs, lbls, _ = data_loader.dataset_loader(self.directory, label_str='mask')
        _, _, preds = data_loader.dataset_loader(self.directory, pred_str=str_model)

        save_image_measure_pred = self.directory + "/images_pos_measure_preds"
        img_preds_path = save_image_measure_pred + "/imgs_preds"
        mask_imgs_preds = save_image_measure_pred + "/imgs_and_masks_preds"
        save_image_measure_real = self.directory + "/images_pos_measure_real"
        img_real_path = save_image_measure_real + "/imgs_real"
        mask_imgs_real = save_image_measure_real + "/imgs_and_masks_real"

        if not (os.path.exists(save_image_measure_pred) and os.path.isdir(save_image_measure_pred)):
            os.makedirs(save_image_measure_pred)
            os.makedirs(img_preds_path)
            os.makedirs(mask_imgs_preds)

        if not (os.path.exists(save_image_measure_real) and os.path.isdir(save_image_measure_real)):
            os.makedirs(save_image_measure_real)
            os.makedirs(img_real_path)
            os.makedirs(mask_imgs_real)

        elements = ['image', 'mask', 'ellipse_b', 'ellipse_a', 'ellipse']
        properties = ['label', 'area', 'centroid', 'major_axis_length', 'minor_axis_length']


        var_masks_real = {}
        var_imgs_real = {}
        for n in range(len(lbls)):
            name_var_mask_real = f"real_mask_image{n}"
            masks_real = io.imread(lbls[n])
            var_masks_real[name_var_mask_real] = masks_real

            name_var_imgs_real = f"real_img_mask{n}"
            imgs_real_mask = io.imread(imgs[n])
            var_imgs_real[name_var_imgs_real] = imgs_real_mask

        for m in range(len(lbls)):
            name_var_mask_real = f"real_mask_image{m}"
            masks_real = var_masks_real[name_var_mask_real]
            grid_resampled_real, xx, yy = grainsizing.resample_masks(masks_real, filters=filters_values, grid_size=16.5,
                                                                     mute=True)
            io.imsave(mask_imgs_real + f'/img_{m + 1}_measure_real_masks.tif', grid_resampled_real)

            plt.figure(figsize=(7, 7))
            plotting.plot_single_img_mask(io.imread(imgs[m]), grid_resampled_real,
                                          file_id=f'img_{m + 1}_measure_real_masks')
            plt.savefig(img_real_path + f'/img_{m + 1}_identify_real.png', dpi=300)
            plt.savefig(mask_imgs_real + f'/img_{m + 1}_identify_real.png', dpi=300)
            plt.close()
            plt.cla()
            plt.clf()

        lbl_grains, lbl_grains_props, lbl_grain_id = grainsizing.batch_grainsize(save_image_measure_real,
                                                                                 filters=filters_values,
                                                                                 mask_str='_real_masks',
                                                                                 properties=properties,
                                                                                 mute=True, return_results=True,
                                                                                 do_subfolders=True)


        for k in range(len(lbls)):
            plt.figure(figsize=(7, 7))
            plotting.all_grains_plot(grid_resampled_real, props=lbl_grains_props[k], elements=elements,
                                     image=io.imread(imgs[k]),
                                     title=lbl_grain_id[k])
            plt.savefig(mask_imgs_real + f'/img_{k + 1}_evaluate_real_result.png', dpi=300)
            plt.savefig(img_real_path + f'/img_{k + 1}_evaluate_real_result.png', dpi=300)
            plt.close()
            plt.cla()
            plt.clf()


        var_masks = {}
        var_imgs = {}
        for n in range(len(preds)):
            name_var_mask = f"mask_image{n}"
            masks = io.imread(preds[n])
            var_masks[name_var_mask] = masks

            name_var_imgs = f"real_img{n}"
            imgs_real = io.imread(imgs[n])
            var_imgs[name_var_imgs] = imgs_real

        for m in range(len(preds)):
            name_var_mask = f"mask_image{m}"
            masks = var_masks[name_var_mask]

            grid_resampled_pred, xx, yy = grainsizing.resample_masks(masks, filters=filters_values, grid_size=16.5,
                                                                     mute=True)
            io.imsave(mask_imgs_preds + f'/img_{m + 1}_measure_preds_masks.tif', grid_resampled_pred)

            plt.figure(figsize=(7, 7))
            plotting.plot_single_img_mask(io.imread(imgs[m]), grid_resampled_pred,
                                          file_id=f'img_{m + 1}_measure_preds_masks')
            plt.savefig(img_preds_path + f'/img_{m + 1}_identify_preds.png', dpi=300)
            plt.savefig(mask_imgs_preds + f'/img_{m + 1}_identify_preds.png', dpi=300)

            plt.close()
            plt.cla()
            plt.clf()

        preds_grains, preds_grains_props, preds_grain_id = grainsizing.batch_grainsize(save_image_measure_pred,
                                                                                       filters=filters_values,
                                                                                       mask_str='_preds_masks',
                                                                                       properties=properties,
                                                                                       mute=True, return_results=True,
                                                                                       do_subfolders=True)


        for k in range(len(preds)):
            plt.figure(figsize=(7, 7))
            plotting.all_grains_plot(grid_resampled_pred, props=preds_grains_props[k], elements=elements,
                                     image=io.imread(imgs[k]),
                                     title=preds_grain_id[k])
            plt.savefig(mask_imgs_preds + f'/img_{k + 1}_evaluate_pred_result.png', dpi=300)
            plt.savefig(img_preds_path + f'/img_{k + 1}_evaluate_pred_result.png', dpi=300)
            plt.close()
            plt.cla()
            plt.clf()

        if self.parameters:

            camera_parameters = {
                'image_distance_m': parameters[0],
                'focal_length_mm': parameters[1],
                'sensorH_mm': parameters[2],
                'sensorW_mm': parameters[3],
                'pixelsW': parameters[4],
                'pixelsH': parameters[5],
            }
            grainsizing.re_scale_dataset(mask_imgs_real, resolution=None, camera_parameters=camera_parameters, gsd_str='_grains', return_results=True,
                                         save_gsds=True)

            grainsizing.re_scale_dataset(mask_imgs_preds, resolution=None, camera_parameters=camera_parameters,
                                         gsd_str='_grains', return_results=True,
                                         save_gsds=True)

            tar_dir = Path(self.directory).joinpath('grain_outlines').as_posix()
            os.makedirs(tar_dir, exist_ok=True)
            grainsizing.export_grain_outline(io.imread(str(lbls[0])), img=io.imread(str(imgs[0])), tar_dir=str(tar_dir),
                                         props=lbl_grains_props[0], file_id='demo', plot_summary=True)

            grainsizing.batch_outline(lbls, imgs, prop_l=lbl_grains_props, tar_dir=str(tar_dir), filters=filters_values)
            measure="confirm"

        decode_output_meas = measure
        self.measure_finished.emit(decode_output_meas)

class GrainAnalyseThread(QThread):

   grain_finished = Signal(str)

   def __init__(self,data_path_pred,data_path_real,data_path,data_path_results,str_model):

       super().__init__()

       self.data_path_pred = data_path_pred
       self.data_path_real = data_path_real
       self.data_path = data_path
       self.data_path_results = data_path_results
       self.str_model = str_model

   def run(self):
    grain_finished = Signal(str)
    pred_grains_scaled = data_loader.load_grain_set(self.data_path_pred, gsd_str='preds_masks_grains_re_scaled')
    real_grains_scaled = data_loader.load_grain_set(self.data_path_real, gsd_str='real_masks_grains_re_scaled')

    column_name = 'ell: b-axis (mm)'
    pred_gsd_l, pred_id_l = grainsizing.gsd_for_set(pred_grains_scaled, column=column_name)
    real_gsd_l, real_id_l = grainsizing.gsd_for_set(real_grains_scaled, column=column_name)

    method = 'bootstrapping'

    res_dict_bs_pred = gsd_uncertainty.dataset_uncertainty(gsds=pred_grains_scaled, num_it=1000, method=method,
                                                           mute=True,
                                                           column_name=column_name, save_results=True,
                                                           return_results=True, sep=',', gsd_id=pred_id_l)

    res_dict_bs_real = gsd_uncertainty.dataset_uncertainty(gsds=real_grains_scaled, num_it=1000, method=method,
                                                           mute=True,
                                                           column_name=column_name, save_results=True,
                                                           return_results=True, sep=',', gsd_id=real_id_l)

    full_gsd_results_pred = pd.DataFrame({f'{column_name}_perc_lower_CI': res_dict_bs_pred[pred_id_l[0]][2],
                                          f'{column_name}_perc_median': res_dict_bs_pred[pred_id_l[0]][0],
                                          f'{column_name}_perc_upper_CI': res_dict_bs_pred[pred_id_l[0]][1],
                                          f'{column_name}_perc_value': res_dict_bs_pred[pred_id_l[0]][3]})

    full_gsd_results_real = pd.DataFrame({f'{column_name}_perc_lower_CI': res_dict_bs_real[real_id_l[0]][2],
                                          f'{column_name}_perc_median': res_dict_bs_real[real_id_l[0]][0],
                                          f'{column_name}_perc_upper_CI': res_dict_bs_real[real_id_l[0]][1],
                                          f'{column_name}_perc_value': res_dict_bs_real[real_id_l[0]][3]})

    out_dir = self.data_path + '/GSD_uncertainty/'
    os.makedirs(out_dir, exist_ok=True)

    full_gsd_results_pred.to_csv(f'{out_dir}/imgs_preds_{method}_full_uncertainty.csv')
    full_gsd_results_real.to_csv(f'{out_dir}/imgs_real_{method}_full_uncertainty.csv')

    csv_files_preds = []
    csv_files_real = []

    for file in os.listdir(self.data_path_pred):

        if file.endswith('.csv'):
            csv_files_preds.append(file)

    for file in os.listdir(self.data_path_real):

        if file.endswith('.csv'):
            csv_files_real.append(file)


    for i in range(len(pred_gsd_l)):
        plt.figure(figsize=(10, 5))
        df_pred = pd.read_csv(self.data_path_pred + f"/{csv_files_preds[i]}")
        length_max_pred = df_pred[column_name].max()
        length_min_pred = df_pred[column_name].min()

        df_real = pd.read_csv(self.data_path_real + f"/{csv_files_real[i]}")
        length_max_real = df_real[column_name].max()
        length_min_real = df_real[column_name].min()

        plotting.plot_gsd(pred_gsd_l[i], color='k', length_min=length_min_pred, length_max=length_max_pred,
                          orientation='vertical',
                          label_axes=True, units='mm', title=pred_id_l[i].split(f'_{str_model}')[0])

        plotting.plot_gsd_uncert(res_dict_bs_pred[pred_id_l[i]], color='k')

        plotting.plot_gsd(real_gsd_l[i], color='b', length_min=length_min_real, length_max=length_max_real,
                          orientation='vertical',
                          label_axes=True, units='mm')

        plotting.plot_gsd_uncert(res_dict_bs_real[real_id_l[i]], color='k')

        plt.savefig(self.data_path_results + f"/graph_result_BS_img_{i + 1}.png", dpi=300)
        plt.close()
        plt.cla()
        plt.clf()

    summary_df_pred = grainsizing.summary_statistics(pred_grains_scaled, pred_id_l, res_dict=res_dict_bs_pred,
                                                     data_id='fh_demo_pred')
    summary_df_pred.head()

    summary_df_real = grainsizing.summary_statistics(real_grains_scaled, real_id_l, res_dict=res_dict_bs_real,
                                                     data_id='fh_demo_real')
    summary_df_real.head()

    grain = "confirm"

    decode_output_grain = grain
    self.grain_finished.emit(decode_output_grain)

# class VideoWidget(QVideoWidget):
#
#     def __init__(self,x1,y1,x2,y2,parent=None):
#         super().__init__(None)
#         self.x1=x1
#         self.y1 =y1
#         self.x2 =x2
#         self.y2 = y2
#         #self.container=container
#
#
#     def paintEvent(self,event):
#
#         if isinstance(self.x1, int) and isinstance(self.y1, int) and isinstance(self.x2, int) and isinstance(self.y2, int):
#             print(f"x1:{self.x1},y1:{self.y1},x2:{self.x2},y2:{self.y2}")
#             painter = QPainter(self)
#             pen = QPen(Qt.red, 2)
#             painter.setPen(pen)
#             painter.drawLine(self.x1, self.y1, self.x2, self.y2)

class ProcessVideoThread(QThread):
    process_video_finished=Signal(str)
    ImageUpdatedetect = Signal(QImage)
    def __init__(self,button_models_check,video_path,video_path_origin,name,caminho_arquivo,cam,select_cam):

        super().__init__()
        self.buttons_models_check=button_models_check
        self.video_path=video_path
        self.name=name
        self.caminho_arquivo_th=caminho_arquivo
        self.video_path_origin=video_path_origin
        self.cam=cam
        self.running=True
        self.select_cam=select_cam
        self._stop_event = threading.Event()
    def run (self):

        directory_file=os.path.dirname(self.caminho_arquivo_th)
        video_name = os.path.splitext(os.path.basename(self.caminho_arquivo_th))[0]
        video_name = video_name.split('_')[0]
        self.caminho_video_title=os.path.join(directory_file,video_name)

        path_audio=self.video_path_origin.replace('.mp4', '.mp3')
        self.model_check = []
        self.name_list = [f"_{part}" for part in self.name.split('_') if part]

        for j in range(0, len(self.buttons_models_check)):
            self.model_check.append(self.buttons_models_check[j].objectName())

        self.check_caminho_video = self.caminho_video_title + self.name_list[0]

        for j in range(0, len(self.model_check)):

            video_path_base = os.path.basename(self.video_path)

            if self.name_list[j] in video_path_base:

                continue

            if os.path.exists(self.check_caminho_video+".avi"):
                self.video_path=self.check_caminho_video+".avi"

                if j < len(self.model_check)-1:
                    self.check_caminho_video=self.check_caminho_video+self.name_list[j+1]
                continue

            model_path = f"models/{self.model_check[j]}.pt"
            model = YOLO(model_path)

            if self.cam =="on":

                if len(self.select_cam) == 0:
                    break

                self.camera_detect_object(self.model_check, self.select_cam)
                break

            if self.running:
                model.predict(source=self.video_path, show=True, task='segment', save=True, conf=0.80)
                path_orig = "runs/segment/predict"
                self.move_files_avi(path_orig, self.video_path, self.name_list[j])
                self.remove_dir(path_orig)
                self.video_path=self.new_dest
                self.add_audio(self.video_path,path_audio)

                if j == len(self.model_check)-1 and j!=0:

                    if os.path.exists(self.caminho_video_title+self.name_list[j]+".avi"):
                        self.video = "confirm"
                        self.process_video_finished.emit(self.video)

                    else:
                        model_path = f"models/{self.model_check[j]}.pt"
                        model = YOLO(model_path)
                        model.predict(source=self.video_path_origin, show=True, task='segment', save=True, conf=0.80)
                        self.move_files_avi(path_orig, self.video_path, self.name_list[j])
                        self.remove_dir(path_orig)

                        self.add_audio(self.new_dest, path_audio)

                        self.video = "confirm"
                        self.process_video_finished.emit(self.video)

                else:
                    self.video = "confirm"
                    self.process_video_finished.emit(self.video)

    def camera_detect_object(self, model_name, video_path):

        model = []
        for p in range(0, len(model_name)):
            model.append(YOLO(f"models/{model_name[p]}.pt"))

        self.caps_detect = [cv2.VideoCapture(self.verify_and_converter(idx)) for idx in video_path]
        self.active_camera_index_detect = 0
        command = 'neutral'
        command_break='continue'
        for cap in self.caps_detect:
            if not cap.isOpened():
                print("Erro ao abrir uma das webcams")
                return
        results=[]
        annotated_frame=[]
        alpha = 0.5
        beta = 1 - alpha
        self.old_active_index = self.active_camera_index_detect
        while self.running:
            stop_command=self.stop_cam(command_break)
            if stop_command == 'stop':
                self.running=False
                break
            cap = self.caps_detect[self.switch_cam_detect(video_path, self.active_camera_index_detect, command)]
            if self.old_active_index != self.active_camera_index_detect:
                results = []
                annotated_frame = []
                self.old_active_index = self.active_camera_index_detect

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            ret, frame = cap.read()
            if not ret:
                print("Não foi possível capturar o frame")
                break
            for m in range(0,len(model_name)):
                results.append(model[m](frame,conf=0.80))
                annotated_frame.append(results[m][0].plot())

            combined_frame=annotated_frame[0]
            if len(model_name)>1:
                for i in range(0,len(model_name)):
                    combined_frame = cv2.addWeighted(annotated_frame[i+1], alpha, combined_frame,beta,0)
                    if i+1 == len(model_name)-1:
                        break

            Image_detect = cv2.cvtColor(combined_frame, cv2.COLOR_BGR2RGB)
            FlippedImage_detect = cv2.flip(Image_detect, 1)
            ConvertToQtFormat_detect = QImage(FlippedImage_detect.data, FlippedImage_detect.shape[1], FlippedImage_detect.shape[0],
                                       QImage.Format_RGB888)
            Pic_detect = ConvertToQtFormat_detect.scaled(width, 350, Qt.KeepAspectRatio)

            self.ImageUpdatedetect.emit(Pic_detect)

        for cap in self.caps:
            cap.release()
        cv2.destroyAllWindows()

    def switch_cam_detect(self, list_cam, index, command):

        if command == 'neutral':
            self.active_camera_index = index
        elif command == 'next':
            self.active_camera_index = index + 1
            if self.active_camera_index == len(list_cam):
                self.active_camera_index = 0
        elif command == 'previous':
            self.active_camera_index = index - 1
            if self.active_camera_index < 0:
                self.active_camera_index = len(list_cam) - 1

        return self.active_camera_index

    def stop_cam(self,command_break):
        if command_break=='continue':
            command_break=command_break

        elif command_break=='stop':
            command_break='stop'

        return command_break

    def add_audio(self,video_path, audio_path):

        try:

            video = moviepy.editor.VideoFileClip(video_path)
            audio = moviepy.editor.AudioFileClip(audio_path)
            video = video.set_audio(audio)
            directory=os.path.dirname(video_path)
            temp_output_path=f"{directory}/temp_video_with_audio.mp4"
            video.write_videofile(temp_output_path, codec="libx264", audio_codec="aac", fps=video.fps)
            os.replace(temp_output_path, video_path)

        except Exception as e:
            print(f"ERROR: {e}")

    def verify_and_converter(self, valor):
        try:
            return int(valor)
        except ValueError:
            return valor

    def move_files_avi(self, orig,dest,name):
        if not os.path.exists(dest):
            os.makedirs(dest)

        for file in os.listdir(orig):

            if file.endswith(".avi"):

                path_orig= os.path.join(orig, file)
                name_archive, extension = os.path.splitext(file)
                new_name = f"{name_archive}{name}{extension}"
                path_dest = os.path.dirname(dest)
                path_dest = os.path.join(path_dest, new_name)
                path_dest = path_dest[::-1].replace("\\", "/", 1)[::-1]

                shutil.move(path_orig, path_dest)
                self.new_dest=path_dest

    def remove_dir(self,path):
        if os.path.exists(path):
            shutil.rmtree(path)
        else:
            print(f"The folder: {path} does not exist!")

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class WebcamThread(QThread):
    ImageUpdate = Signal(QImage)

    def __init__(self, list_camera):
        super().__init__()
        self.running = True
        self.list_camera = list_camera
        self.caps = [cv2.VideoCapture(self.verify_index_converter(idx)) for idx in list_camera]
        self.active_camera_index = 0

    def run(self):
        command='neutral'

        for cap in self.caps:
            if not cap.isOpened():
                print("Erro ao abrir uma das webcams")
                return

        while not self.isInterruptionRequested():
            cap=self.caps[self.switch_cam(self.list_camera,self.active_camera_index,command)]
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            ret, frame = cap.read()
            if not ret:
                print("Não foi possível capturar o frame")
                break

            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FlippedImage = cv2.flip(Image, 1)
            ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],
                                       QImage.Format_RGB888)
            Pic = ConvertToQtFormat.scaled(width, 350, Qt.KeepAspectRatio)
            self.ImageUpdate.emit(Pic)

        for cap in self.caps:
            cap.release()
        cv2.destroyAllWindows()

    def switch_cam(self,list_cam,index,command):

        if command=='neutral':
            self.active_camera_index=index
        elif command =='next':
            self.active_camera_index=index+1
            if self.active_camera_index==len(list_cam):
                self.active_camera_index=0
        elif command =='previous':
            self.active_camera_index = index - 1
            if self.active_camera_index<0:
                self.active_camera_index=len(list_cam)-1

        return self.active_camera_index

    def verify_index_converter(self, valor):
        try:
            return int(valor)
        except ValueError:
            return valor

class FunctionsUtil():
    def segmentation(self, direct_path, file_path, scroll_area, horizontal_layout, frame_image, frame_result,page):

        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)

        lb_progress_segment = QLabel(page)
        lb_progress_segment.setObjectName(u"lb_progress_segment")
        lb_progress_segment.setGeometry(470, 10, 311, 50)
        lb_progress_segment.setStyleSheet(u"color: none;\n""background-color: none;\n""border:none;\n""")
        lb_progress_segment.setText(QCoreApplication.translate("MainWindow", "Segmenting...", None))
        lb_progress_segment.setFont(font)
        lb_progress_segment.show()

        self.seg_thread = SegThread(direct_path, file_path)
        self.seg_thread.segmentation_finished.connect(
            lambda output: self.update_segmentation_results(output, lb_progress_segment, scroll_area, horizontal_layout,
                                                            frame_image, frame_result, direct_path, file_path))
        self.seg_thread.data_ready.connect(self.plot_results)
        self.seg_thread.start()

    @Slot(list)
    def plot_results(self, data):
        imgs, lbls, preds, directory= data

        for i in range(len(imgs)):
            plotting.plot_single_img_pred(imgs[i].replace("\\", "/"), preds[i].replace("\\", "/"), save=True)

        filters = {'edge': [False, .05], 'px_cutoff': [False, 12]}
        mask_path = os.path.splitext(os.path.basename(self.seg_thread.model))[0]
        results_seg = "Results"
        results_path_seg = os.path.join(self.seg_thread.directory, results_seg)

        if not os.path.exists(results_path_seg):
            os.mkdir(results_path_seg)

        eval_results_fh_boosted = segmentation_helper.eval_set(imgs, lbls, preds, data_id=mask_path,
                                                               tar_dir=results_path_seg, filters=filters)
        plt.figure(figsize=(5, 8))
        plt.plot()
        plt.title('Results Model')
        test_idxs1 = segmentation_helper.find_test_idxs(lbls)
        direct_path_last = pathlib.PurePath(directory)
        elem = {
            'dataset': str(direct_path_last.name),
            'model_id': 'FH',
            'colors': ['m', 'palevioletred'],
            'images': False,
            'std': True,
            'avg_model': True
        }
        plotting.AP_IoU_summary_plot([eval_results_fh_boosted], elem, test_idxs1)
        dir_results = os.path.join(results_path_seg, f'{mask_path}.jpg')
        plt.savefig(dir_results)
        plt.close()
        plt.cla()
        plt.clf()

    def update_segmentation_results(self, output, lb_progress_segment, scroll_area, horizontal_layout, frame_image, frame_result, direct_path,file_path):

        images_list = []
        images_vars = []
        icon = []
        images_list_pred = []
        images_files = [file for file in os.listdir(direct_path) if file.endswith('.jpg')]

        direct_path_pred = direct_path + "/" + "prediction_masks"
        images_pred_files = os.listdir(direct_path_pred)
        results_seg = "Results"
        results_path_seg = os.path.join(direct_path, results_seg)
        mask_path = os.path.splitext(os.path.basename(file_path))[0]
        dir_results = results_path_seg + '/' + f'{mask_path}''.jpg'

        lb_progress_segment.setText(QCoreApplication.translate("MainWindow", output, None))
        lb_progress_segment.adjustSize()
        lb_progress_segment.hide()

        for k in range(0, len(images_files)):
            images_list_pred.append([(Image.open(direct_path_pred + "/" + images_pred_files[k]))])

        for i in range(0, len(images_files)):
            images_list.append([Image.open(direct_path + "/" + images_files[i])])
            images_vars.append(f'img_{i}')

        self.display_images(images_vars, scroll_area, horizontal_layout, icon, direct_path_pred, images_pred_files, frame_image, frame_result, dir_results)

    def display_images_frame(self, frame_image, directory, preds, index):
        frame_image.setPixmap(QPixmap(""))
        frame_image.setPixmap(QPixmap(directory + "/" + preds[index]))
        frame_image.setScaledContents(True)

    def display_result_frame(self, frame_result, directory):
        frame_result.setPixmap(QPixmap(""))
        frame_result.setPixmap(QPixmap(directory))
        frame_result.setScaledContents(True)

    def display_images(self, images_vars, scroll_area, horizontal_layout, icon, direct_path_pred, images_pred_files, fm_image, fm_results, dir_results):

        for n in range(len(images_vars)):
            images_vars[n] = QPushButton(scroll_area)
            images_vars[n].setObjectName(u"set_images_vars_" + str(n) + "_btn")
            images_vars[n].setGeometry(QRect(((5+(75*n))), 5, 65, 65))
            images_vars[n].setStyleSheet(u"color: none;\n""background-color: none;\n""border-radius:10px;\n""")
            horizontal_layout.addWidget(images_vars[n])
            icon.append(f'icon_{n}')
            icon[n]=QIcon()
            icon[n].addFile(direct_path_pred + "/" + images_pred_files[n], QSize(), QIcon.Normal, QIcon.Off)
            images_vars[n].setIcon(icon[n])
            images_vars[n].setIconSize(QSize(65, 65))
            images_vars[n].show()
            images_vars[n].clicked.connect(self.callback(n, fm_image, direct_path_pred, images_pred_files))
            scroll_area.setStyleSheet(
                u"color: rgb(255, 255, 255);\n""background-color: rgb(255, 255, 255);\n""border-radius:10px;\n""")
            self.display_result_frame(fm_results, dir_results)

    def callback(self, index, frame, direct_path_pred, images_pred_files):
         return lambda: self.display_images_frame(frame, direct_path_pred, images_pred_files, index)

    def clear(self, frame_image, frame_result, scroll_area):
        frame_image.setPixmap(QPixmap(""))
        frame_result.setPixmap(QPixmap(""))
        scroll_area.setStyleSheet(u"background-color: none;\n"
                                          "border-color:none;")
        for button in scroll_area.findChildren(QPushButton):
            button.setParent(None)
            button.deleteLater()

        self.seg_thread = None


    def train(self, directory, model, frame_train, vertical_layout, horizontal_layout, page,nepochs_text):

        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        lb_progress_train = QLabel(page)
        lb_progress_train.setObjectName(u"lb_progress_train")
        lb_progress_train.setGeometry(450, 80, 311, 50)
        lb_progress_train.setStyleSheet(u"color: none;\n""background-color: none;\n""border:none;\n""")
        lb_progress_train.setText(QCoreApplication.translate("MainWindow", "Training...", None))
        lb_progress_train.setFont(font)
        lb_progress_train.show()
        lb_train_results_teste = QLabel(frame_train)
        lb_train_results_teste.setObjectName(u"lb_train_results")
        lb_train_results_teste.setGeometry(QRect(0, 0, 16777215, 16777215))
        lb_train_results_teste.setMinimumSize(QSize(16777215, 16777215))
        lb_train_results_teste.setStyleSheet(u"color: none;\n""background-color: none;\n""border-radius:10px;\n""")
        vertical_layout.addWidget(lb_train_results_teste)
        lb_train_results_teste.show()

        try:
            self.nepochs = nepochs_text.text()
            self.nepochs = int(self.nepochs)

            if self.nepochs < 0:
                raise ValueError("Negative Number!")

        except ValueError:

            QMessageBox.warning(None, 'Input Error', 'Please enter valid integer numbers!')

        self.train_thread = TrainThread(directory, model,self.nepochs)
        self.train_thread.training_finished_train.connect(lambda output: self.update_train_results(output, lb_train_results_teste,lb_progress_train))
        self.train_thread.start()

    def update_train_results(self, output, lb_train_results_teste,lb_progress_train):

        lb_train_results_teste.setText(QCoreApplication.translate("MainWindow", output, None))
        lb_progress_train.hide()

    def clear_train(self, frame_train):

        for label in frame_train.findChildren(QLabel):
            label.setParent(None)
            label.deleteLater()

        #self.train_thread = None

    global filters, parameters
    filters=[]
    parameters=[]

    def set_values_measure(self,line_edge,line_cut,line_image_distance,line_focal_lenght,line_sensor_height,line_sensor_width,line_pixel_width,line_pixel_height,set_values,lb_measure,btn_measure,lb_clear,btn_clear):
        global filters,parameters
        edge_text = line_edge.text()
        cut_text = line_cut.text()

        image_distance_text = line_image_distance.text()
        focal_lenght_text = line_focal_lenght.text()
        pixel_height_text = line_pixel_height.text()
        pixel_width_text = line_pixel_width.text()
        sensor_height_text = line_sensor_height.text()
        sensor_width_text = line_sensor_width.text()

        if set_values.objectName() == "set_values_filters_btn":
            if edge_text and cut_text:
                try:
                    edge_number = float(edge_text)
                    cut_number = int(cut_text)

                    QMessageBox.information(None, 'Success', 'Values of filter loaded successfully!')
                    filters = [edge_number, cut_number]
                except ValueError:
                    QMessageBox.warning(None, 'Input Error', 'Please enter valid float numbers.')

            else:
                QMessageBox.warning(None, 'Input Error', 'Please fill all filters.')

        if set_values.objectName() == "set_values_parameters_btn":
            if image_distance_text and focal_lenght_text and pixel_height_text and pixel_width_text and sensor_height_text and sensor_width_text:
                try:
                    image_distance_number = float(image_distance_text)
                    focal_lenght_number = float(focal_lenght_text)
                    pixel_height_number = int(pixel_height_text)
                    pixel_width_number = int(pixel_width_text)
                    sensor_height_number = float(sensor_height_text)
                    sensor_width_number = float(sensor_width_text)

                    QMessageBox.information(None, 'Success', 'Values of parameters loaded successfully!')

                    parameters = [image_distance_number, focal_lenght_number, pixel_height_number, pixel_width_number,
                                  sensor_height_number, sensor_width_number]

                except ValueError:
                    QMessageBox.warning(None, 'Input Error', 'Please enter valid float numbers!')

            else:
                QMessageBox.warning(None, 'Input Error', 'Please fill all parameters!')

    def clear_set_values_filters(self,line_edge,line_cut):
        line_edge.clear()
        line_cut.clear()

    def clear_set_values_parameters(self,line_image_distance,line_focal_lenght,line_sensor_height,line_sensor_width,line_pixel_width,line_pixel_height):

        line_image_distance.clear()
        line_focal_lenght.clear()
        line_pixel_height.clear()
        line_pixel_width.clear()
        line_sensor_height.clear()
        line_sensor_width.clear()

    def measure(self,data_path,scrool_area_measure,vertical_layout_measure,frame_image,frame_graph,page):

        global str_model
        global filters,parameters

        if not data_path:
            QMessageBox.warning(None, 'Input Error', 'Please, provide the path!')
            return

        if len(parameters) == 0:
            QMessageBox.warning(None, 'Input Error', 'Please, fill all parameters!')
            return

        if len(filters) == 0 or filters == None:

            QMessageBox.warning(None, 'Attention', 'Attention: Measuring without any filter!')
            filters = None

        else:

            filters = {
                'edge': [True, filters[0]], 'px_cutoff': [True, filters[1]]
            }

        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)

        lb_progress_measure = QLabel(page)
        lb_progress_measure.setObjectName(u"lb_progress_measure")
        lb_progress_measure.setGeometry(350, 10, 311, 50)
        lb_progress_measure.setStyleSheet(u"color: none;\n""background-color: none;\n""border:none;\n""")
        lb_progress_measure.setText(QCoreApplication.translate("MainWindow", "Measuring...", None))
        lb_progress_measure.setFont(font)
        lb_progress_measure.show()

        data_path_results = data_path + "/graphs_grain_sizes"
        os.makedirs(data_path_results, exist_ok=True)

        for file in os.listdir(data_path):
            name, extension = os.path.splitext(file)
            if extension[1:].isdigit():
                str_model = name + "_pred"

        self.meas_thread=MeasureThread(data_path,filters,parameters)
        self.meas_thread.measure_finished.connect(lambda:self.update_measure(data_path,data_path_results,lb_progress_measure,page,scrool_area_measure,vertical_layout_measure,frame_image,frame_graph))
        self.meas_thread.start()


    def update_measure(self,data_path,data_path_results,lb_progress_measure,page,scrool_area_measure,vertical_layout_measure,frame_image,frame_graph):

        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)

        lb_progress_measure.hide()
        lb_progress_analyse = QLabel(page)
        lb_progress_analyse.setObjectName(u"lb_progress_analyse")
        lb_progress_analyse.setGeometry(350, 10, 311, 50)
        lb_progress_analyse.setStyleSheet(u"color: none;\n""background-color: none;\n""border:none;\n""")
        lb_progress_analyse.setText(QCoreApplication.translate("MainWindow", "Analysing...", None))
        lb_progress_analyse.setFont(font)
        lb_progress_analyse.show()

        save_image_measure_pred = data_path + "/images_pos_measure_preds"
        img_preds_path = save_image_measure_pred + "/imgs_preds"
        mask_imgs_preds = save_image_measure_pred + "/imgs_and_masks_preds"
        save_image_measure_real = data_path + "/images_pos_measure_real"
        img_real_path = save_image_measure_real + "/imgs_real"
        mask_imgs_real = save_image_measure_real + "/imgs_and_masks_real"

        self.copy_re_scaled_csv(mask_imgs_preds, img_preds_path)
        self.copy_re_scaled_csv(mask_imgs_real, img_real_path)
        self.reorganize_imgs(mask_imgs_real)
        self.reorganize_imgs(mask_imgs_preds)

        image_vars_measure = []
        icon_measure = []
        self.grains_analyse(img_preds_path, img_real_path, data_path, data_path_results, str_model,lb_progress_analyse)
        self.grains_thread.grain_finished.connect(lambda:self.display_image_measure(img_preds_path, image_vars_measure,scrool_area_measure, vertical_layout_measure,
                                   icon_measure, frame_image, frame_graph, data_path_results))


    def copy_re_scaled_csv(self,data_path_orig,data_path_copy):

        for file in os.listdir(data_path_orig):

            if "re_scaled" in file:
                path_orig = os.path.join(data_path_orig, file)
                path_dest = os.path.join(data_path_copy, file)
                shutil.copy2(path_orig, path_dest)

            if "summary" in file:
                path_orig = os.path.join(data_path_orig, file)
                path_dest = os.path.join(data_path_copy, file)
                shutil.move(path_orig, path_dest)
    def display_image_measure(self, data_path, images_vars_measure, scroll_area, vertical_layout, icon_measure,fm_image,fm_graph,data_path_graph):

        images_pred_files_measure = [file for file in os.listdir(data_path) if 'identify' in file]

        images_files_measure = [file for file in os.listdir(data_path) if file.endswith('.png') and "identify" in file]

        images_results_files_measure = [file for file in os.listdir(data_path) if 'evaluate' in file]

        for i in range(0,len(images_files_measure)):
            images_vars_measure.append(f'img_{i}')

        for n in range(0,len(images_vars_measure)):
            images_vars_measure[n] = QPushButton(scroll_area)
            images_vars_measure[n].setObjectName(u"set_images_vars_" + str(n) + "_btn")
            images_vars_measure[n].setGeometry(QRect(5, (5 + (75 * n)), 65, 65))
            images_vars_measure[n].setStyleSheet(u"color: none;\n""background-color: none;\n""border-radius:10px;\n""")
            vertical_layout.addWidget(images_vars_measure[n])
            icon_measure.append(f'icon_{n}')
            icon_measure[n] = QIcon()
            icon_measure[n].addFile(data_path + "/" + images_pred_files_measure[n], QSize(), QIcon.Normal, QIcon.Off)
            images_vars_measure[n].setIcon(icon_measure[n])
            images_vars_measure[n].setIconSize(QSize(65, 65))
            images_vars_measure[n].show()
            images_vars_measure[n].clicked.connect(self.callback_image_measure(n, fm_image, fm_graph,data_path,data_path_graph, images_results_files_measure))
            scroll_area.setStyleSheet(
                u"color: rgb(255, 255, 255);\n""background-color: rgb(255, 255, 255);\n""border-radius:10px;\n""")
    def grains_analyse(self,data_path_pred,data_path_real,data_path,data_path_results,str_model,lb_progress_analyse):

        self.grains_thread = GrainAnalyseThread(data_path_pred,data_path_real,data_path,data_path_results,str_model)
        self.grains_thread.grain_finished.connect(
            lambda: self.update_grain(lb_progress_analyse,data_path,data_path_pred,data_path_real))
        self.grains_thread.start()


    def update_grain(self,lb_progress_analyse,data_path,data_path_pred,data_path_real):

        lb_progress_analyse.hide()

        out_dir = data_path + '/GSD_uncertainty/'
        back_path_pred = os.path.dirname(data_path_pred)
        back_path_real = os.path.dirname(data_path_real)
        self.copy_re_scaled_csv(back_path_pred, out_dir)
        self.copy_re_scaled_csv(back_path_real, out_dir)

    def callback_image_measure(self, index, frame, frame_graph,direct_path_pred, direct_path_graph,images_pred_files):
        return lambda: self.display_images_measure_frame(frame, frame_graph,direct_path_pred,direct_path_graph, images_pred_files, index)

    def display_images_measure_frame(self, frame_image, frame_graph,directory,directory_graph, preds, index):

        frame_image.setPixmap(QPixmap(""))
        frame_image.setPixmap(QPixmap(directory + "/" + preds[index]))
        frame_image.setScaledContents(True)

        graphs = [file for file in os.listdir(directory_graph)]

        frame_graph.setPixmap(QPixmap(""))
        frame_graph.setPixmap(QPixmap(directory_graph + "/" + graphs[index]))
        frame_graph.setScaledContents(True)

    def clear_measure(self,frame_image, frame_graph, scrool_area):

        frame_image.setPixmap(QPixmap(""))
        frame_graph.setPixmap(QPixmap(""))
        scrool_area.setStyleSheet(u"background-colo:none;\n"
                                  "border-color:none;")
        for button in scrool_area.findChildren(QPushButton):
            button.setParent(None)
            button.deleteLater()

    def reorganize_imgs(self,data_path):

        pattern = r'img_(\d+)'

        for filename in os.listdir(data_path):
            match = re.search(pattern, filename)
            if match:
                img_number = match.group(1)

                destination_folder = os.path.join(data_path, f'img_{img_number}')

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(os.path.join(data_path, filename), os.path.join(destination_folder, filename))

    def rename_files(self,data_path):

        jpg_count = 1
        tif_count = 1

        for filename in sorted(os.listdir(data_path)):
            if filename.endswith('.jpg'):
                match = re.match(r'(.*)\.jpg', filename)

                if match:
                    new_name = f"img_{jpg_count}.jpg"
                    os.rename(os.path.join(data_path, filename), os.path.join(data_path, new_name))
                    jpg_count += 1

            elif filename.endswith('_mask.tif'):

                match = re.match(r'(.*)_mask\.tif', filename)

                if match:
                    new_name = f"img_{tif_count}_mask.tif"
                    os.rename(os.path.join(data_path, filename), os.path.join(data_path, new_name))
                    tif_count += 1

    def open_video(self,page,pause,play,stop,back,forward,sound,no_sound,slider_sound,lb_current_time,lb_total_time,slider_time,scrool_area,icon_sphere,horizontal_layout,btn_max,rd_ignored,rd_keep,rd_keep_expand,btn_check,btn_update_models,list_widget,velocity_page,id_call):


        self.velocity_page=page
        self.aspect_ratio = Qt.IgnoreAspectRatio
        self.page_video=velocity_page
        self.rd_ignored=rd_ignored
        self.rd_keep=rd_keep
        self.rd_keep_expand=rd_keep_expand
        aspect_radio_button = QButtonGroup(page)
        aspect_radio_button.addButton(self.rd_ignored)
        aspect_radio_button.addButton(self.rd_keep)
        aspect_radio_button.addButton(self.rd_keep_expand)

        self.btn_detect=btn_check
        self.scroll_area=scrool_area
        self.horizontal_layout=horizontal_layout
        self.list_widget=list_widget
        self.function_called = False
        self.count_called = 0
        self.count_called_no_check = 0
        self.slider_time=slider_time
        self.lb_current_time=lb_current_time
        self.lb_total_time=lb_total_time
        self.pause=pause
        self.play=play

        self.list_widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)

        self.rd_ignored.toggled.connect(lambda: self.radio_button_toggled())
        self.rd_keep.toggled.connect(lambda: self.radio_button_toggled())
        self.rd_keep_expand.toggled.connect(lambda: self.radio_button_toggled())

        self.scroll_area.setStyleSheet(
            u"color: rgb(255, 255, 255);\n""background-color: rgb(255, 255, 255);\n""border-radius:10px;\n""")

        if id_call=="open_movie":
            self.video_path= QFileDialog.getOpenFileName()[0]
            self.cam = "off"
            self.reg_cam = True

        if id_call=="cam_on":

            self.reg_cam = False
            self.cam = "on"
            self.trade_index_cam = 0
            if not hasattr(self,'layout_camera') and not hasattr(self,'label_camera'):

                self.reg_cam=True
                self.layout_camera = QVBoxLayout(page)
                self.layout_camera.setGeometry(QRect(0, 0,  441, 350))
                self.layout_camera.setContentsMargins(0, 0, 0, 0)
                self.layout_camera.setSpacing(0)
                self.label_camera = QLabel()
                self.layout_camera.addWidget(self.label_camera)

            if not hasattr(self,'list_camera'):
                self.selected_cameras=[0]
            else:
                self.selected_cameras = [item.text() for item in self.list_camera.selectedItems()]
                if len(self.selected_cameras) == 0:
                    self.selected_cameras=[0]

            self.video_path= "yolo/videoexample_process.avi"
            self.webcam_thread = WebcamThread(self.selected_cameras)
            self.webcam_thread.ImageUpdate.connect(self.ImageUpdateSlot)

            self.webcam_thread.start()
            self.cam_run = 1
            self.q_shortcut = 'not_pressed'

        if hasattr(self, 'video_path'):
            self.video_original = self.video_path

        self.path_video_original=os.path.dirname(self.video_original)
        self.path_audio = self.video_original.replace('.mp4', '.mp3')

        if not os.path.exists(self.path_audio):
            self.extract_audio_from_video(self.video_original, f"{self.path_video_original}/audio.mp3")

        if self.video_path and self.reg_cam:

            path_models = "models/"
            models_pt = [file for file in os.listdir(path_models) if file.endswith('.pt')]
            self.models_names = [os.path.splitext(file)[0] for file in models_pt]
            self.control_models=len(models_pt)
            png_icons = [file_png for file_png in os.listdir(path_models) if file_png.endswith('.png') and file_png.endswith("_d" + '.png')]
            self.icons_names = [file_png[:-len("_d" + '.png')] for file_png in png_icons]
            self.buttons_models=[]
            self.icon_button = []
            self.video_thread_check = "off"

            self.existing_items = [self.list_widget.item(i).text() for i in range(self.list_widget.count())]

            if not hasattr(self, 'buttons_dict'):
                self.buttons_dict = {}

            for model_name in self.models_names:
                if model_name not in self.existing_items:
                    self.list_widget.addItem(model_name)

            for i in range(0,len(models_pt)):
                self.buttons_models.append(f"{self.models_names[i]}")
                self.icon_button.append(f"{self.icons_names[i]}")

            for i in range(0,len(self.models_names)):

                if self.models_names[i] not in self.buttons_dict:
                    self.buttons_models[i] = QToolButton(self.scroll_area)
                    self.buttons_models[i].setCheckable(True)
                    self.buttons_models[i].setObjectName(f"{self.models_names[i]}")
                    self.buttons_models[i].setGeometry(QRect(0, 0, 65, 65))
                    self.buttons_models[i].setStyleSheet(u"color: none;\n""background-color: none;\n""border:none;\n""")
                    self.horizontal_layout.addWidget(self.buttons_models[i])
                    self.icon_button[i] = QIcon()
                    self.icon_button[i].addFile(path_models+self.icons_names[i]+"_d.png", QSize(), QIcon.Normal, QIcon.Off)
                    self.icon_button[i].addFile(path_models+self.icons_names[i]+"_e.png", QSize(), QIcon.Active, QIcon.On)
                    self.buttons_models[i].setIcon(self.icon_button[i])
                    self.buttons_models[i].setIconSize(QSize(65, 65))
                    self.buttons_models[i].show()
                    self.buttons_dict[self.models_names[i]] = self.buttons_models[i]
                    self.buttons_models[i].clicked.connect(self.call_detect(i, "button_model"))
                    self.btn_detect.stateChanged.connect(self.call_detect(i, "btn_detect"))

            btn_update_models.clicked.connect(lambda:self.update_models())

        if not self.video_path:
            return

        self.window = QWidget(page)
        self.window.setGeometry(QRect(0, 0, 441, 350))
        self.window.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
                                                       "color: rgb(0, 0, 0);\n"
                                                       "border:none\n"
                                                       "")

        lay = QVBoxLayout(self.window)
        lay.setGeometry(QRect(0, 0, self.window.width(), self.window.height()))
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        self.graphics_view = QGraphicsView()
        self.graphics_view.setGeometry(QRect(0, 0, self.window.width(), self.window.height()))
        self.graphics_view.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.graphics_view.setStyleSheet(u"background: transparent;")
        lay.addWidget(self.graphics_view)

        self.window.setLayout(lay)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.graphics_view.width(), self.graphics_view.height())
        self.graphics_view.setScene(self.scene)

        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.video_item = QGraphicsVideoItem()
        self.video_item.setSize(self.graphics_view.size())
        self.video_item.setAspectRatioMode(self.aspect_ratio)

        self.scene.addItem(self.video_item)

        self.coords_label = QLabel("Coordinates: (0, 0)", self.graphics_view)
        self.coords_label.setStyleSheet("background-color: none; color: white;")
        self.coords_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.coords_label.setGeometry(5, 5, 140, 20)
        self.coords_label.hide()

        if hasattr(self,'media_player'):
            if self.media_player.PlaybackState.PlayingState:
                self.media_player.stop()

        self.media_player = QMediaPlayer(self.window)
        self.audio_output = QAudioOutput(self.window)
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.video_item)

        self.media_player.mediaStatusChanged.connect(lambda status:self.handle_media_status(status))

        if self.cam == "off":

            self.media_player.setSource(QUrl.fromLocalFile(self.video_path))
            self.media_player.play()

            self.media_player.setPosition(0)
            self.window.show()

        slider_sound.setRange(0, 100)
        slider_sound.setValue(50)
        slider_sound.valueChanged.connect(lambda volume: self.set_volume(volume,sound,no_sound))
        self.slider_time.setRange(0, 0)
        self.slider_time.sliderMoved.connect(self.set_position)
        volume = slider_sound.value()

        self.media_player.positionChanged.connect(lambda position: self.positionChanged(position, self.slider_time,self.lb_current_time))
        self.media_player.durationChanged.connect(lambda duration: self.durationChanged(duration, self.slider_time,self.lb_total_time))

        self.pause.clicked.connect(lambda:self.play_pause_video(self.pause,self.play))
        self.play.clicked.connect(lambda:self.play_pause_video(self.pause,self.play))
        stop.clicked.connect(lambda:self.stop_video(pause,play))
        back.clicked.connect(lambda:self.back_video())
        forward.clicked.connect(lambda:self.skip_forward())
        sound.clicked.connect(lambda:self.sound_mute_video(sound,no_sound))
        no_sound.clicked.connect(lambda: self.sound_mute_video(sound, no_sound))

        btn_max.clicked.connect(lambda:self.on_resize(self.window, self.graphics_view,self.video_item,self.scene))

        def mouse_move_event(event):

            view_pos = self.graphics_view.mapFromGlobal(event.globalPosition().toPoint())
            if self.graphics_view.rect().contains(view_pos):
                self.coords_label.setText(f"Coordinates: ({int(view_pos.x())}, {int(view_pos.y())})")
                self.coords_label.show()
            else:
                self.coords_label.hide()

        def leave_event(event):
            self.coords_label.hide()

        self.graphics_view.setMouseTracking(True)
        self.graphics_view.mouseMoveEvent = mouse_move_event
        self.graphics_view.leaveEvent = leave_event
        self.video_item.setAspectRatioMode(Qt.IgnoreAspectRatio)

        self.count = 0
        self.i = 0
        self.lines = []
        self.reg=0

        # self.video_item.setFlag(QGraphicsItem.ItemIsFocusable)
        # self.video_item.setAcceptHoverEvents(True)
        #
        # self.graphics_view.setMouseTracking(True)


    #     self.video_item.mouseDoubleClickEvent = self.toggle_fullscreen
    #
    # def toggle_fullscreen(self, event):
    #     if self.video_item.isFullScreen():
    #         self.showNormal()
    #     else:
    #         self.showFullScreen()

    def on_q_pressed(self):

        self.q_shortcut='pressed'
        if hasattr(self,'webcam_thread'):
            if self.webcam_thread.isRunning():

                self.webcam_thread.requestInterruption()
                self.webcam_thread.wait()
                self.label_camera.setPixmap(QPixmap())
                self.label_camera.clear()
                self.label_camera.close()

        if hasattr(self,'video_process'):
            if self.video_process.isRunning():

                self.video_process.stop_cam('stop')

    def switch_cam_web_thread(self,command):

        if hasattr(self,'webcam_thread'):
            if self.webcam_thread.isRunning():
                self.trade_index_cam=self.webcam_thread.switch_cam(self.selected_cameras,self.trade_index_cam,command)

        if hasattr(self,'video_process'):
            if self.video_process.isRunning():
                self.trade_index_cam_detect=self.video_process.switch_cam_detect(self.selected_texts,self.trade_index_cam_detect,command)

    def handle_media_status(self,status):

        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.media_player.setPosition(0)
            self.media_player.play()

        if hasattr(self, 'current_position'):
            if status == QMediaPlayer.MediaStatus.LoadedMedia:
                self.media_player.setPosition(self.current_position)
                self.media_player.mediaStatusChanged.disconnect()

    def extract_audio_from_video(self,video_path, audio_path):
        try:
            video_name = os.path.splitext(os.path.basename(video_path))[0]
            directory_video = os.path.dirname(video_path)
            audio_path = f"{directory_video}/{video_name}.mp3"
            video = moviepy.editor.VideoFileClip(video_path)
            audio = video.audio
            audio.write_audiofile(audio_path)
            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def update_models(self):

        self.path_models = "models/"
        models_pt = [file for file in os.listdir(self.path_models) if file.endswith('.pt')]
        self.models_names = [os.path.splitext(file)[0] for file in models_pt]
        png_icons = [file_png for file_png in os.listdir(self.path_models) if
                     file_png.endswith('.png') and file_png.endswith("_d" + '.png')]
        self.icons_names = [file_png[:-len("_d" + '.png')] for file_png in png_icons]
        self.existing_items = [self.list_widget.item(i).text() for i in range(self.list_widget.count())]

        for item in self.existing_items:
            if item not in self.models_names:
                matching_items = self.list_widget.findItems(item, Qt.MatchExactly)
                if matching_items:
                    for match in matching_items:
                        row = self.list_widget.row(match)
                        self.list_widget.takeItem(row)

        for model_name in self.models_names:
            if model_name not in self.existing_items:
                self.list_widget.addItem(model_name)

        existing_model_names = list(self.buttons_dict.keys())
        for model_name in existing_model_names:
            if model_name not in self.models_names:
                button_to_remove = self.buttons_dict.pop(model_name)

                index_to_remove = None
                for idx, button in enumerate(self.buttons_models):
                    if button and button.objectName() == model_name:
                        index_to_remove = idx
                        break

                if index_to_remove is not None:
                    self.horizontal_layout.removeWidget(button_to_remove)
                    button_to_remove.deleteLater()
                    self.buttons_models.pop(index_to_remove)
                    self.icon_button.pop(index_to_remove)

                    icon_d_path = os.path.join(self.path_models, f"{model_name}_d.png")
                    icon_e_path = os.path.join(self.path_models, f"{model_name}_e.png")

                    if os.path.exists(icon_d_path):
                        os.remove(icon_d_path)

                    if os.path.exists(icon_e_path):
                        os.remove(icon_e_path)


        for i in range(len(self.models_names)):

            if i < len(self.buttons_models) and isinstance(self.buttons_models[i], QToolButton):
                continue
            else:
                if i < len(self.buttons_models):
                    self.buttons_models[i] = None
                else:
                    self.buttons_models.append(None)

        for i in range(len(self.icons_names)):

            if i < len(self.icon_button) and self.icon_button[i] is not None:
                continue

            else:
                if i < len(self.icon_button):
                    self.icon_button[i] = None
                else:
                    self.icon_button.append(None)

        self.buttons_models = self.buttons_models[:len(self.models_names)]
        self.icon_button = self.icon_button[:len(self.icons_names)]

        if not hasattr(self, 'buttons_dict'):
            self.buttons_dict = {}

        for i in range(0,len(self.models_names)):
            if(self.buttons_models[i]==None):
                self.buttons_models[i]=self.models_names[i]
                self.icon_button[i]=self.models_names[i]


        for i in range(0, len(self.models_names)):

            if self.models_names[i] not in self.buttons_dict:

                self.buttons_models[i] = QToolButton(self.scroll_area)
                self.buttons_models[i].setCheckable(True)
                self.buttons_models[i].setObjectName(f"{self.models_names[i]}")
                self.buttons_models[i].setGeometry(QRect(0, 0, 65, 65))
                self.buttons_models[i].setStyleSheet(u"color: none;\n""background-color: none;\n""border:none;\n""")
                self.horizontal_layout.addWidget(self.buttons_models[i])

                self.icon_button[i] = QIcon()
                self.icon_button[i].addFile(self.path_models + self.icons_names[i] + "_d.png", QSize(), QIcon.Normal,
                                                    QIcon.Off)
                self.icon_button[i].addFile(self.path_models + self.icons_names[i] + "_e.png", QSize(), QIcon.Active,
                                                    QIcon.On)
                self.buttons_models[i].setIcon(self.icon_button[i])
                self.buttons_models[i].setIconSize(QSize(65, 65))
                self.buttons_models[i].show()
                self.buttons_dict[self.models_names[i]] = self.buttons_models[i]
                self.buttons_models[i].clicked.connect(self.call_detect(i, "button_model_update"))
                #self.btn_detect.stateChanged.connect(self.call_detect(i, "btn_detect_update"))

            else:
                pass

        for i in range(0, len(self.buttons_models)):

            if isinstance(self.buttons_models[i], QToolButton):
                pass
            else:
                self.buttons_models[i] = QToolButton(self.scroll_area)
                self.buttons_models[i].setCheckable(True)
                self.buttons_models[i].setObjectName(f"{self.models_names[i]}")
                self.buttons_models[i].setGeometry(QRect(0, 0, 65, 65))
                self.buttons_models[i].setStyleSheet(u"color: none;\n""background-color: none;\n""border:none;\n""")
                self.horizontal_layout.addWidget(self.buttons_models[i])

    def delete_models(self):
        if not hasattr(self,'list_widget'):
            return
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            for selected_item in selected_items:
                selected_name = selected_item.text()
                file_path = os.path.join("models", f"{selected_name}.pt")

                if os.path.exists(file_path):
                    os.remove(file_path)

            self.update_models()
        else:
            pass

    def select_list_item(self, index,checked):

        items = self.list_widget.findItems(self.models_names[index], Qt.MatchExactly)
        if items:
            item = items[0]
            if checked:
                if not item.isSelected():
                    item.setSelected(True)

            else:
                item.setSelected(False)
        else:
            pass
    def radio_button_toggled(self):

        if self.rd_ignored.isChecked():

            self.aspect_ratio = Qt.IgnoreAspectRatio

        elif self.rd_keep.isChecked():

            self.aspect_ratio = Qt.KeepAspectRatio

        elif self.rd_keep_expand.isChecked():

            self.aspect_ratio = Qt.KeepAspectRatioByExpanding

        self.video_item.setAspectRatioMode(self.aspect_ratio)

    def on_resize(self, window,graphics,video,scene):

        if self.count % 2 == 0:

            window.setGeometry(QRect(0, 0, 441, 350))
            graphics.setGeometry(QRect(0, 0, 441, 350))
            video.setSize(graphics.size())
            scene.setSceneRect(0,0,graphics.width(),graphics.height())
            video.setAspectRatioMode(self.aspect_ratio)

        else:

            window.setGeometry(QRect(0, 0, 441, 350))
            graphics.setGeometry(QRect(0, 0, 441, 350))
            video.setSize(graphics.size())
            scene.setSceneRect(0,0,graphics.width(),graphics.height())
            video.setAspectRatioMode(self.aspect_ratio)

        self.count += 1

    def call_detect(self,index,id):

        return lambda: self.handle_detect(index, id)

    def handle_detect(self,index, id):

        self.verify_pressed(index)
        self.buttons_models_check = []

        for i in range(0, len(self.buttons_models)):
            if (self.buttons_models[i].isChecked()):
                self.buttons_models_check.append(self.buttons_models[i])


        if id=="btn_detect":

            self.count_called += 1
            if self.btn_detect.isChecked():
                self.count_called_no_check += 1

        self.name = ""

        if id == "button_model" or id == "button_model_update":

            for j in range(0, len(self.buttons_models_check)):

                name_movie = os.path.splitext(os.path.basename(self.video_path))[0]
                self.name = self.name + f"_{self.buttons_models_check[j].objectName()}"
                parts = self.name.split('_')
                sorted_parts = sorted(parts)
                self.name='_'.join(sorted_parts)

                self.movie_dirname=os.path.dirname(self.video_path)
                self.caminho_arquivo = os.path.join(self.movie_dirname, f"{name_movie}{self.name}.avi")

        if id == "btn_detect":

            if self.count_called % 2 != 0:

                for j in range(0, len(self.buttons_models_check)):

                    name_movie = os.path.splitext(os.path.basename(self.video_path))[0]
                    self.name = self.name + f"_{self.buttons_models_check[j].objectName()}"
                    parts = self.name.split('_')
                    sorted_parts = sorted(parts)
                    self.name = '_'.join(sorted_parts)

                    self.movie_dirname = os.path.dirname(self.video_path)
                    self.caminho_arquivo = os.path.join(self.movie_dirname, f"{name_movie}{self.name}.avi")

        if not hasattr(self,'caminho_arquivo'):
            self.caminho_arquivo=self.video_original

        self.remove_duplicate()

        if not self.function_called:
            if self.btn_detect.isChecked():
                self.reorder()
                self.video_trade = os.path.join(self.caminho_dir, f"{self.first_name}{self.name}.avi")

                if len(self.buttons_models_check) == 0:

                    if id=="button_model" or id =="button_model_update":

                        current_position_original = self.media_player.position()
                        self.trade_video(current_position_original, self.video_original)

                        return

                    if id =="btn_detect":

                        if self.count_called_no_check % 2 == 0:

                            current_position_original = self.media_player.position()
                            self.trade_video(current_position_original, self.video_original)
                            self.count_called_no_check=0
                            return
                        else:

                            return

                if not os.path.exists(self.caminho_arquivo) and self.video_thread_check == "off":

                    self.identify_sphere(index, id)
                    self.count_called=1

                else:

                    current_position_done = self.media_player.position()

                    if id=="button_model" or id=="button_model_update":

                        if os.path.exists(self.video_trade):

                            self.trade_video(current_position_done, self.video_trade)


                        else:
                            self.trade_video(current_position_done,self.caminho_arquivo)



                    if id == "btn_detect":

                        if self.count_called % 2 != 0:

                            if os.path.exists(self.video_trade):
                                self.trade_video(current_position_done, self.video_trade)



                            else:
                                self.trade_video(current_position_done, self.caminho_arquivo)


            else:
                current_position_original = self.media_player.position()
                if id == "button_model" or id == "button_model_update":
                    self.trade_video(current_position_original,self.video_original)

                if id == "btn_detect":
                    if self.count_called % 2 == 0:
                        self.trade_video(current_position_original,self.video_original)
    def remove_duplicate(self):

        self.caminho_dir, self.caminho_arquivo_ext = os.path.split(self.caminho_arquivo)
        self.name_caminho_arquivo, self.ext_arquivo = os.path.splitext(self.caminho_arquivo_ext)
        self.parts_caminho_arquivo = self.name_caminho_arquivo.split('_')
        seen = []
        for index, part in enumerate(self.parts_caminho_arquivo):
            if index == 0:
                seen.append(part)
            else:
                name_sublime = f"{part}"
                if name_sublime not in seen:
                    seen.append(name_sublime)

        self.caminho_arquivo_basename_new = '_'.join(seen) + self.ext_arquivo
        self.caminho_arquivo = os.path.join(self.caminho_dir, self.caminho_arquivo_basename_new)


    def reorder(self):

        directory, filename = os.path.split(self.caminho_arquivo)

        name, extension = os.path.splitext(filename)

        parts = name.split('_')
        self.first_name = parts[0]
        remaining_parts = sorted(parts[1:])

        new_name = self.first_name + '_' + '_'.join(remaining_parts) + extension

        self.caminho_arquivo = os.path.join(directory, new_name)

    def verify_pressed(self,index):

        if self.buttons_models[index].isChecked():
            self.checked=True
        else:
            self.checked=False

        self.select_list_item(index,self.checked)
    def identify_sphere(self,index,id):

        if not os.path.exists(self.path_audio):
            self.extract_audio_from_video(self.video_original, f"{self.path_video_original}/audio.mp3")

        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(15)
        font.setBold(True)

        self.lb_progress_video = QLabel(self.page_video)
        self.lb_progress_video.setObjectName(u"lb_progress_video")
        self.lb_progress_video.setGeometry(480, 15, 111, 31)
        self.lb_progress_video.setStyleSheet(u"color: none;\n""background-color: none;\n""border:none;\n""")
        self.lb_progress_video.setText(QCoreApplication.translate("MainWindow", "Detecting...", None))
        self.lb_progress_video.setFont(font)
        self.lb_progress_video.show()

        if self.name=="":
            self.name="_"
            for i in range(0,len(self.buttons_models_check)):
                self.name=self.name + self.buttons_models_check[i].objectName()
                parts = self.name.split('_')
                sorted_parts = sorted(parts)
                self.name = '_'.join(sorted_parts)

        if self.cam=="on":

            if not hasattr(self,'list_camera'):
                self.selected_texts=[0]
            else:
                self.selected_texts = [item.text() for item in self.list_camera.selectedItems()]

        else:
            self.selected_texts=[]

        self.trade_index_cam_detect=0
        self.video_process=ProcessVideoThread(self.buttons_models_check,self.video_path,self.video_original,self.name,self.caminho_arquivo,self.cam,self.selected_texts)
        self.video_process.ImageUpdatedetect.connect(self.ImageUpdateSlot)
        if self.cam=="on":

            if self.cam_run <= 1:
                self.on_q_pressed()
                self.q_shortcut = 'not_pressed'
                self.video_process.start()
                self.cam_run+=1

        elif self.cam=="off":

            self.video_process.start()

        if self.video_process.isRunning():
            self.video_thread_check = "on"

        self.video_process.wait()
        self.update_video()

        #self.video_process.process_video_finished.connect(lambda:self.update_video())

    def update_video(self):

        if hasattr(self, 'video_process'):
            if self.video_process.isRunning():
                return
            else:
                if self.cam_run == len(self.buttons_models_check)+1:
                    self.cam_run=1
                else:
                    self.cam_run += 1

        # self.cam="off_to_on_cam"

        self.lb_progress_video.hide()
        current_position = self.media_player.position()

        self.trade_video(current_position, self.caminho_arquivo)
        self.video_thread_check = "off"

        # if os.path.exists(self.path_audio):
        #     os.remove(self.path_audio)

    def ImageUpdateSlot(self, Image):

        if not self.label_camera.isVisible() and self.q_shortcut=='not_pressed':
            self.label_camera.setGeometry(QRect(0, 0, 441, 350))
            self.label_camera.show()

        self.label_camera.setPixmap(QPixmap.fromImage(Image))

    def trade_video(self,current_position,new_dest):

        if hasattr(self,'video_process'):
            if self.video_process.isRunning():
                return

        status = self.media_player.playbackState()
        self.current_position = current_position
        self.media_player.stop()
        self.video_path = new_dest
        self.video_path = self.video_path.replace("\\", "/")

        self.media_player.setSource(QUrl.fromLocalFile(self.video_path))
        self.media_player.mediaStatusChanged.connect(lambda status: self.handle_media_status(status))
        self.media_player.setPosition(self.current_position)
        self.slider_time.setValue(self.current_position)

        if status == QMediaPlayer.PlaybackState.PlayingState or status == QMediaPlayer.PlaybackState.StoppedState:
            self.media_player.play()
            self.pause.show()
            self.play.hide()

        elif status == QMediaPlayer.PlaybackState.PausedState:

            self.media_player.pause()
            self.pause.hide()
            self.play.show()

    def play_pause_video(self, pause,play):

        if hasattr(self,'media_player'):
            if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:

                self.media_player.pause()
                pause.hide()
                play.show()

            elif self.media_player.playbackState() == QMediaPlayer.PlaybackState.PausedState or self.media_player.playbackState() == QMediaPlayer.PlaybackState.StoppedState:

                self.media_player.play()
                pause.show()
                play.hide()

    def sound_mute_video(self,sound,mute):

        if not self.audio_output.isMuted():

            sound.hide()
            mute.show()
            self.audio_output.setMuted(True)

        else:

            sound.show()
            mute.hide()
            self.audio_output.setMuted(False)

    def stop_video(self,pause,play):

        self.media_player.stop()
        pause.hide()
        play.show()

    def skip_forward(self):

        current_position = self.media_player.position()
        new_position = current_position + 5000
        if new_position > self.media_player.duration():
            new_position = self.media_player.duration()

        self.media_player.setPosition(new_position)

    def back_video(self):

        current_position = self.media_player.position()
        new_position = current_position - 5000
        if new_position < 0:
            new_position = 0

        self.media_player.setPosition(new_position)

    def set_volume(self, volume,sound,no_sound):

        self.audio_output.setVolume(volume)

        if volume == 0:

            sound.hide()
            no_sound.show()

        else:

            sound.show()
            no_sound.hide()
            self.audio_output.setMuted(False)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def positionChanged(self, position, slider,lb_current_time):
        slider.setValue(position)
        lb_current_time.setText(time.strftime('%H:%M:%S', time.gmtime(position // 1000)))

        if position >= self.media_player.duration():

            self.media_player.setPosition(0)
            self.media_player.play()

    def durationChanged(self, duration, slider,lb_total_time):
        slider.setRange(0, duration)
        lb_total_time.setText(time.strftime('%H:%M:%S', time.gmtime(duration // 1000)))

    def ok_method(self,rd_btn,btn_ok,lb_method,page,rd_direct):

        methods_radio_button = QButtonGroup(page)
        methods_radio_button.addButton(rd_btn)
        methods_radio_button.addButton(rd_direct)

        if not hasattr(self, 'count_aux'):
            self.count_aux = 0

        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)

        self.back_method = QPushButton(page)
        self.back_method.setObjectName(u"back_method")
        self.back_method.setFont(font)
        self.back_method.setText(QCoreApplication.translate("MainWindow", u"Back", None))

        self.set_method = QPushButton(page)
        self.set_method.setObjectName(u"set_method")
        self.set_method.setFont(font)
        self.set_method.setText(QCoreApplication.translate("MainWindow", u"Set", None))

        self.get_distance = QPushButton(page)
        self.get_distance.setObjectName(u"get_distance")
        self.get_distance.setFont(font)
        self.get_distance.setText(QCoreApplication.translate("MainWindow", u"Get", None))

        self.trade_get_set = QPushButton(page)
        self.trade_get_set.setObjectName(u"trade_get_set")
        self.trade_get_set.setFont(font)
        self.trade_get_set.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.trade_get_set.setStyleSheet(u"border-color: none;\n"
                                          "background-color: none;")
        self.icon_trade_get_set = QIcon()
        self.icon_trade_get_set.addFile(u"Icons/side-bar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.trade_get_set.setIcon(self.icon_trade_get_set)
        self.trade_get_set.setIconSize(QSize(15, 15))

        if rd_direct.isChecked():

            self.real_distance = QLabel(page)
            self.real_distance.setObjectName(u"real_distance")
            self.real_distance.setFont(font)
            self.real_distance.setStyleSheet(u"\n"
                                             "background-color: none;\n"
                                             "border-color:none;")
            self.real_distance.setText(QCoreApplication.translate("MainWindow", u"Real distance:", None))

            self.real_distance_line = QLineEdit(page)
            self.real_distance_line.setObjectName(u"real_distance_line")

            self.image_distance_lb = QLabel(page)
            self.image_distance_lb.setObjectName(u"image_distance_lb")
            self.image_distance_lb.setFont(font)
            self.image_distance_lb.setStyleSheet(u"\n"
                                             "background-color: none;\n"
                                             "border-color:none;")
            self.image_distance_lb.setText(QCoreApplication.translate("MainWindow", u"Image distance:", None))

            self.image_distance_line = QLineEdit(page)
            self.image_distance_line.setObjectName(u"image_distance_line")

            self.pixel_ratio_lb = QLabel(page)
            self.pixel_ratio_lb.setObjectName(u"pixel_ratio_lb")
            self.pixel_ratio_lb.setFont(font)
            self.pixel_ratio_lb.setStyleSheet(u"\n"
                                                 "background-color: none;\n"
                                                 "border-color:none;")
            self.pixel_ratio_lb.setText(QCoreApplication.translate("MainWindow", u"Pixel ratio:", None))
            self.pixel_ratio_line = QLineEdit(page)
            self.pixel_ratio_line.setObjectName(u"pixel_ratio_line")

            self.scale_lb = QLabel(page)
            self.scale_lb.setObjectName(u"scale_lb")
            self.scale_lb.setFont(font)
            self.scale_lb.setStyleSheet(u"\n"
                                              "background-color: none;\n"
                                              "border-color:none;")
            self.scale_lb.setText(QCoreApplication.translate("MainWindow", u"Scale:", None))
            self.scale_line = QLineEdit(page)
            self.scale_line.setObjectName(u"scale_line")

            if self.count_aux % 2 == 0:

                self.real_distance.setGeometry(QRect(10, 520, 95, 31))
                self.real_distance_line.setGeometry(QRect(100, 525, 50, 18))
                self.image_distance_lb.setGeometry(QRect(165, 520, 105, 31))
                self.image_distance_line.setGeometry(QRect(265, 525, 50, 18))
                self.pixel_ratio_lb.setGeometry(QRect(10, 490, 91, 31))
                self.pixel_ratio_line.setGeometry(QRect(80, 495, 50, 18))
                self.scale_lb.setGeometry(130, 490, 91, 31)
                self.scale_line.setGeometry(QRect(175, 495, 40, 18))
                self.set_method.setGeometry(QRect(240, 495, 51, 21))
                self.get_distance.setGeometry(QRect(240, 495, 51, 21))
                self.back_method.setGeometry(QRect(295, 495, 51, 21))
                self.trade_get_set.setGeometry(QRect(330, 480, 15, 15))

            else:
                self.real_distance.setGeometry(QRect(10, 630, 95, 31))
                self.real_distance_line.setGeometry(QRect(100, 635, 61, 18))
                self.image_distance_lb.setGeometry(QRect(195, 630, 105, 31))
                self.image_distance_line.setGeometry(QRect(300, 635, 61, 18))
                self.pixel_ratio_lb.setGeometry(QRect(10, 600, 91, 31))
                self.pixel_ratio_line.setGeometry(QRect(80, 605, 50, 18))
                self.scale_lb.setGeometry(130, 600, 91, 31)
                self.scale_line.setGeometry(QRect(175, 605, 40, 18))
                self.set_method.setGeometry(QRect(250, 605, 51, 21))
                self.get_distance.setGeometry(QRect(250, 605, 51, 21))
                self.back_method.setGeometry(QRect(305, 605, 51, 21))
                self.trade_get_set.setGeometry(QRect(360, 605, 15, 15))

            rd_direct.hide()
            rd_btn.hide()
            btn_ok.hide()
            lb_method.hide()
            self.real_distance.show()
            self.real_distance_line.show()
            self.image_distance_lb.show()
            self.image_distance_line.show()
            self.pixel_ratio_lb.show()
            self.pixel_ratio_line.show()
            self.scale_lb.show()
            self.scale_line.show()
            self.back_method.show()
            self.set_method.hide()
            self.get_distance.show()
            self.trade_get_set.show()
            self.back_method.clicked.connect(
                lambda: self.back_methods_direct(rd_direct,rd_btn,self.set_method,self.back_method,btn_ok,lb_method))

            if hasattr(self, 'get_show') and hasattr(self, 'set_show'):

                if self.get_show:
                    self.get_distance.show()
                    self.set_method.hide()
                if self.set_show:
                    self.get_distance.hide()
                    self.set_method.show()

            if hasattr(self,'pixel_ratio_line_last_text') and hasattr(self,'scale_last_text') and hasattr(self,'real_distance_last_text') and hasattr(self,'image_distance_last_text'):

                self.pixel_ratio_line.setText(self.pixel_ratio_line_last_text )
                self.scale_line.setText(self.scale_last_text)
                self.real_distance_line.setText(self.real_distance_last_text)
                self.image_distance_line.setText(self.image_distance_last_text)

            self.set_method.clicked.connect(lambda: self.set_methods(rd_btn,rd_direct))
            self.get_distance.clicked.connect(lambda: self.get_methods(rd_direct))
            self.trade_get_set.clicked.connect(lambda: self.trade_get_set_show(self.get_distance, self.set_method))

        if rd_btn.isChecked():

            rd_direct.hide()
            rd_btn.hide()
            btn_ok.hide()
            lb_method.hide()

            self.lb_height_len = QLabel(page)
            self.lb_height_len.setObjectName(u"lb_height_len")
            self.lb_height_len.setFont(font)
            self.lb_height_len.setStyleSheet(u"background-color: none;\n"
                                                 "border-color:none;")
            self.lb_height_len.setText(QCoreApplication.translate("MainWindow", u"Height lenght:", None))

            self.line_height_len = QLineEdit(page)
            self.line_height_len.setObjectName(u"line_image_distance")

            self.lb_diameter = QLabel(page)
            self.lb_diameter.setObjectName(u"lb_diameter")

            self.lb_diameter.setFont(font)
            self.lb_diameter.setStyleSheet(u"background-color: none;\n"
                                        "border-color:none;")
            self.lb_diameter.setText(QCoreApplication.translate("MainWindow", u"Diameter:", None))

            self.line_lb_diameter = QLineEdit(page)
            self.line_lb_diameter.setObjectName(u"line_lb_diameter")

            self.lb_focus_lenght = QLabel(page)
            self.lb_focus_lenght.setObjectName(u"lb_focus_lenght")

            self.lb_focus_lenght.setFont(font)
            self.lb_focus_lenght.setStyleSheet(u"background-color: none;\n"
                                        "border-color:none;")
            self.lb_focus_lenght.setText(QCoreApplication.translate("MainWindow", u"Focus lenght:", None))

            self.line_focus_lenght = QLineEdit(page)
            self.line_focus_lenght.setObjectName(u"line_focus_lenght")

            if self.count_aux % 2 == 0:

                self.lb_height_len.setGeometry(QRect(10, 490, 91, 31))
                self.line_height_len.setGeometry(QRect(105, 495, 61, 18))
                self.lb_diameter.setGeometry(QRect(10, 520, 71, 31))
                self.line_lb_diameter.setGeometry(QRect(85, 525, 61, 18))
                self.lb_focus_lenght.setGeometry(QRect(165, 520, 90, 31))
                self.line_focus_lenght.setGeometry(QRect(255, 525, 61, 18))
                self.set_method.setGeometry(QRect(200, 495, 51, 21))
                self.back_method.setGeometry(QRect(255, 495, 51, 21))

            else:
                self.lb_height_len.setGeometry(QRect(10, 600, 91, 31))
                self.line_height_len.setGeometry(QRect(105, 605, 61, 18))
                self.lb_diameter.setGeometry(QRect(10, 630, 71, 31))
                self.line_lb_diameter.setGeometry(QRect(85, 635, 61, 18))
                self.lb_focus_lenght.setGeometry(QRect(165, 630, 90, 31))
                self.line_focus_lenght.setGeometry(QRect(255, 635, 61, 18))
                self.set_method.setGeometry(QRect(200, 605, 51, 21))
                self.back_method.setGeometry(QRect(255, 605, 51, 21))

            self.lb_height_len.show()
            self.line_height_len.show()
            self.lb_diameter.show()
            self.line_lb_diameter.show()
            self.line_focus_lenght.show()
            self.lb_focus_lenght.show()
            self.set_method.show()
            self.back_method.show()

            if hasattr(self,'height_len_last_text') and hasattr(self,'diameter_last_text') and hasattr(self,'focus_lenght_last_text'):
                self.line_height_len.setText(self.height_len_last_text)
                self.line_lb_diameter.setText(self.diameter_last_text)
                self.line_focus_lenght.setText(self.focus_lenght_last_text)

            self.back_method.clicked.connect(lambda:self.back_methods(rd_btn,btn_ok,lb_method,self.lb_height_len,self.line_height_len,self.lb_diameter,self.line_lb_diameter,self.lb_focus_lenght,self.line_focus_lenght,self.set_method,self.back_method,rd_direct))
            self.set_method.clicked.connect(lambda: self.set_methods(rd_btn, rd_direct))
    def on_resize_method(self,page,rd_sfiv,rd_direct):

        if not hasattr(self, 'count_aux'):
            self.count_aux = 0

        if not hasattr(self, 'lb_height_len'):
            self.lb_height_len = QLabel(page)
            self.lb_height_len.hide()

        if not hasattr(self, 'line_height_len'):
            self.line_height_len = QLineEdit(page)
            self.line_height_len.hide()

        if not hasattr(self, 'lb_diameter'):
            self.lb_diameter = QLabel(page)
            self.lb_diameter.hide()

        if not hasattr(self, 'line_lb_diameter'):
            self.line_lb_diameter = QLineEdit(page)
            self.line_lb_diameter.hide()

        if not hasattr(self, 'line_focus_lenght'):
            self.line_focus_lenght = QLineEdit(page)
            self.line_focus_lenght.hide()

        if not hasattr(self, 'lb_focus_lenght'):
            self.lb_focus_lenght = QLabel(page)
            self.lb_focus_lenght.hide()

        if not hasattr(self, 'real_distance'):
            self.real_distance = QLabel(page)
            self.real_distance.hide()

        if not hasattr(self,'real_distance_line'):
            self.real_distance_line = QLabel(page)
            self.real_distance.hide()

        if not hasattr(self,'image_distance_lb'):
            self.image_distance_lb = QLabel(page)
            self.image_distance_lb.hide()

        if not hasattr(self, 'image_distance_line'):
            self.image_distance_line = QLabel(page)
            self.image_distance_line.hide()

        if not hasattr(self, 'pixel_ratio_lb'):
            self.pixel_ratio_lb = QLabel(page)
            self.pixel_ratio_lb.hide()

        if not hasattr(self, 'pixel_ratio_line'):
            self.pixel_ratio_line = QLabel(page)
            self.pixel_ratio_line.hide()

        if not hasattr(self, 'scale_lb'):
            self.scale_lb = QLabel(page)
            self.scale_lb.hide()

        if not hasattr(self, 'scale_line'):
            self.scale_line = QLabel(page)
            self.scale_line.hide()

        if not hasattr(self, 'set_method'):
            self.set_method = QPushButton(page)
            self.set_method.hide()

        if not hasattr(self, 'get_distance'):
            self.get_distance = QPushButton(page)
            self.get_distance.hide()

        if not hasattr(self, 'back_method'):

            self.back_method = QPushButton(page)
            self.back_method.hide()

        if not hasattr(self, 'trade_get_set'):
            self.trade_get_set = QPushButton(page)
            self.trade_get_set.hide()

        if hasattr(self,'media_player'):

            if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
                self.pause.show()
                self.play.hide()

            elif self.media_player.playbackState() == QMediaPlayer.PlaybackState.PausedState or self.media_player.playbackState() == QMediaPlayer.PlaybackState.StoppedState:

                self.pause.hide()
                self.play.show()

        self.count_aux += 1

        if rd_sfiv.isChecked():

            if self.count_aux % 2 == 0:

                self.lb_height_len.setGeometry(QRect(10, 490, 91, 31))
                self.line_height_len.setGeometry(QRect(105, 495, 61, 18))
                self.lb_diameter.setGeometry(QRect(10, 520, 71, 31))
                self.line_lb_diameter.setGeometry(QRect(85, 525, 61, 18))
                self.lb_focus_lenght.setGeometry(QRect(165, 520, 90, 31))
                self.line_focus_lenght.setGeometry(QRect(255, 525, 61, 18))
                self.set_method.setGeometry(QRect(200, 495, 51, 21))
                self.back_method.setGeometry(QRect(255, 495, 51, 21))

            else:

                self.lb_height_len.setGeometry(QRect(10, 600, 91, 31))
                self.line_height_len.setGeometry(QRect(105, 605, 61, 18))
                self.lb_diameter.setGeometry(QRect(10, 630, 71, 31))
                self.line_lb_diameter.setGeometry(QRect(85, 635, 61, 18))
                self.lb_focus_lenght.setGeometry(QRect(165, 630, 90, 31))
                self.line_focus_lenght.setGeometry(QRect(255, 635, 61, 18))
                self.set_method.setGeometry(QRect(200, 605, 51, 21))
                self.back_method.setGeometry(QRect(255, 605, 51, 21))

        if rd_direct.isChecked():

            if self.count_aux % 2 == 0:

                self.real_distance.setGeometry(QRect(10, 520, 95, 31))
                self.real_distance_line.setGeometry(QRect(100, 525, 50, 18))
                self.image_distance_lb.setGeometry(QRect(165, 520, 105, 31))
                self.image_distance_line.setGeometry(QRect(265, 525, 50, 18))
                self.pixel_ratio_lb.setGeometry(QRect(10, 490, 91, 31))
                self.pixel_ratio_line.setGeometry(QRect(80, 495, 50, 18))
                self.scale_lb.setGeometry(130, 490, 91, 31)
                self.scale_line.setGeometry(QRect(175, 495, 40, 18))
                self.set_method.setGeometry(QRect(240, 495, 51, 21))
                self.get_distance.setGeometry(QRect(240, 495, 51, 21))
                self.back_method.setGeometry(QRect(295, 495, 51, 21))
                self.trade_get_set.setGeometry(QRect(330, 480, 15, 15))

            else:

                self.real_distance.setGeometry(QRect(10, 630, 95, 31))
                self.real_distance_line.setGeometry(QRect(100, 635, 61, 18))
                self.image_distance_lb.setGeometry(QRect(195, 630, 105, 31))
                self.image_distance_line.setGeometry(QRect(300, 635, 61, 18))
                self.pixel_ratio_lb.setGeometry(QRect(10, 600, 91, 31))
                self.pixel_ratio_line.setGeometry(QRect(80, 605, 50, 18))
                self.scale_lb.setGeometry(130, 600, 91, 31)
                self.scale_line.setGeometry(QRect(175, 605, 40, 18))
                self.set_method.setGeometry(QRect(250, 605, 51, 21))
                self.back_method.setGeometry(QRect(305, 605, 51, 21))
                self.get_distance.setGeometry(QRect(250, 605, 51, 21))
                self.trade_get_set.setGeometry(QRect(360, 605, 15, 15))

    def trade_get_set_show(self,get_distance,set_method):

        if get_distance.isVisible():
            get_distance.hide()
            set_method.show()
            return

        if set_method.isVisible():
            get_distance.show()
            set_method.hide()
            return

    def set_coordinates(self,x_coordinate,y_coordinate,table_widget,x1_label,y1_label,x2_label,y2_label,first_set,set_coordinates):

        current_row = table_widget.rowCount()
        self.table_widget=table_widget
        if first_set:

            x1 = int(x_coordinate.text())
            y1 = int(y_coordinate.text())
            table_widget.insertRow(current_row)
            vertical_header_item = QTableWidgetItem(f"{current_row + 1}°  ")
            table_widget.setVerticalHeaderItem(current_row, vertical_header_item)

            table_widget.setItem(current_row, 0, QTableWidgetItem(str(x1)))
            table_widget.setItem(current_row, 1, QTableWidgetItem(str(y1)))

            x1_label.hide()
            y1_label.hide()
            x2_label.show()
            y2_label.show()

            set_coordinates.clicked.disconnect()
            set_coordinates.clicked.connect(lambda: self.set_coordinates(x_coordinate,y_coordinate,table_widget,x1_label,y1_label,x2_label,y2_label,False,set_coordinates))

        else:

            x2=int(x_coordinate.text())
            y2=int(y_coordinate.text())

            current_row = table_widget.rowCount() - 1

            table_widget.setItem(current_row, 2, QTableWidgetItem(str(x2)))
            table_widget.setItem(current_row, 3, QTableWidgetItem(str(y2)))

            x2_label.hide()
            y2_label.hide()
            x1_label.show()
            y1_label.show()

            set_coordinates.clicked.disconnect()
            set_coordinates.clicked.connect(
                lambda: self.set_coordinates(x_coordinate, y_coordinate, table_widget, x1_label, y1_label, x2_label,
                                             y2_label, True, set_coordinates))

    def add_point(self,table_widget,add_point):

        selected_row = table_widget.currentRow()

        if selected_row != -1:

            self.get_coordinates(selected_row, table_widget,self.reg)

            self.table_widget.itemChanged.connect(self.on_item_changed)

        else:
            print("No row")

    def on_item_changed(self, item):
        row = item.row()
        if row < len(self.line_item):
            self.scene.removeItem(self.line_item[row])

        if (self.table_widget.item(row, 0) is not None and
                self.table_widget.item(row, 1) is not None and
                self.table_widget.item(row, 2) is not None and
                self.table_widget.item(row, 3) is not None):

            self.x1 = int(self.table_widget.item(row, 0).text())
            self.y1 = int(self.table_widget.item(row, 1).text())
            self.x2 = int(self.table_widget.item(row, 2).text())
            self.y2 = int(self.table_widget.item(row, 3).text())

        pen = QPen(QColor("red"), 3)

        if row < len(self.line_item):
            self.line_item[row] = QGraphicsLineItem(self.x1, self.y1, self.x2, self.y2,self.video_item)
            self.line_item[row].setPen(pen)

    def get_coordinates(self,row,table_widget,reg):

        self.x1 = int(table_widget.item(row, 0).text())
        self.y1 = int(table_widget.item(row, 1).text())
        self.x2 = int(table_widget.item(row, 2).text())
        self.y2 = int(table_widget.item(row, 3).text())
        self.old_num_lines = 1
        self.num_lines=table_widget.rowCount()

        if not hasattr(self,'line_item'):
            self.line_item = []

        if reg==0 or len(self.line_item)==0:
            self.line_item = [None] * self.num_lines
            self.reg+=1

        if self.num_lines != self.old_num_lines:
            for i in range((self.num_lines-self.old_num_lines),self.num_lines+1):
                self.line_item.append(None)
            self.old_num_lines = self.num_lines

        for k in range(0,self.num_lines):
            if self.line_item[k] is None:
                self.line_item[k] = f"coordinate_{k+1}"

        self.line_item = [item for item in self.line_item if item is not None]

        if self.i < len(self.line_item):
            if not isinstance(self.line_item[self.i] , QGraphicsItem):
                self.line_item[self.i] = QGraphicsLineItem(self.x1, self.y1, self.x2, self.y2,self.video_item)

        pen = QPen(QColor("red"), 3)
        if self.i < len(self.line_item):
            self.line_item[self.i].setPen(pen)

        self.lines.append((self.x1, self.y1, self.x2, self.y2))
        self.i+=1

    def clear_coodinates(self,table_widget):

        selected_row = table_widget.currentRow()

        if selected_row != -1:

            self.clear_point(selected_row, table_widget)

        else:
            print("No row")

    def clear_point(self,row,table_widget):

      self.x1 = int(table_widget.item(row, 0).text())
      self.y1 = int(table_widget.item(row, 1).text())
      self.x2 = int(table_widget.item(row, 2).text())
      self.y2 = int(table_widget.item(row, 3).text())

      coords = (self.x1, self.y1, self.x2, self.y2)

      self.num_lines_actual = table_widget.rowCount()

      count_instance=0
      if hasattr(self, 'line_item'):
          for m in range(0, len(self.line_item)):
              if isinstance(self.line_item[m], QGraphicsItem):
                  count_instance+=1

      if hasattr(self,'line_item') and count_instance == self.num_lines_actual:

          for j in range(0,len(self.line_item)):

              line_compare=(self.line_item[j].line())

              x1_comp = int(line_compare.x1())
              y1_comp = int(line_compare.y1())
              x2_comp = int(line_compare.x2())
              y2_comp = int(line_compare.y2())
              coords_compare=(x1_comp,y1_comp,x2_comp,y2_comp)

              if (coords_compare == coords):

                  table_widget.removeRow(row)
                  self.scene.removeItem(self.line_item[j])
                  del self.line_item[j]
                  self.i-=1
                  for row_index in range(table_widget.rowCount()):
                      table_widget.setVerticalHeaderItem(row_index, QTableWidgetItem(f"{row_index + 1}°  "))
                  break
      else:

          if row != -1:
              table_widget.removeRow(row)
          for row_index in range(table_widget.rowCount()):
              table_widget.setVerticalHeaderItem(row_index, QTableWidgetItem(f"{row_index + 1}°  "))

    def show_message(self):

        message_box = QMessageBox()
        message_box.setWindowTitle("Question")
        message_box.setText("Do you want to use the average of the last three scale values?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        answer = message_box.exec()

        if answer == QMessageBox.Yes:
            self.average_scale=sum(self.scale_values)/len(self.scale_values)
            self.average_scale=round(self.average_scale,2)
        else:
            self.average_scale=self.scale

    def set_methods(self,rd_sfiv,rd_direct):

        if rd_sfiv.isChecked():
            self.height_len=self.line_height_len.text()
            self.diameter=self.line_lb_diameter.text()
            self.focus_lenght=self.line_focus_lenght.text()

        if rd_direct.isChecked():

            self.set_method.hide()
            self.get_distance.show()

            if not hasattr(self, 'scale_values'):
                self.scale_values = []

            if not self.image_distance_line.text().strip() == "" and not self.pixel_ratio_line.text().strip() == "":
                if self.real_distance_line.text().strip()== "" or self.scale_line.text().strip() == "":
                    if self.real_distance_line.text().strip() == "" and self.scale_line.text().strip() == "":
                        pass
                    if not self.real_distance_line.text().strip()== "":

                        image_distance = round(float(self.image_distance_line.text()),2)
                        real_distance = round(float(self.real_distance_line.text()),2)
                        self.scale = image_distance / real_distance
                        self.scale=round(self.scale,2)

                        if len(self.scale_values) < 3:

                            self.scale_values.append(self.scale)

                            if len(self.scale_values) == 3:
                                self.show_message()
                                self.scale_line.setText(f"{self.average_scale}")
                                self.scale_values = []
                                return

                        self.scale_line.setText(f"{self.scale}")

                        return

                    if not self.scale_line.text().strip() == "":
                        pixel_ratio = round(float(self.pixel_ratio_line.text()),2)
                        self.scale = round(float(self.scale_line.text()),2)
                        image_distance = round(float(self.image_distance_line.text()),2)
                        if hasattr(self,'x1_get') and hasattr(self,'y1_get') and hasattr(self,'x2_get') and hasattr(self,'y2_get'):
                            if not self.x1_get=="" and not self.x2_get=="" and not self.y1_get=="" and not self.y2_get=="":
                                x1_real = self.x1_get*(1/self.scale)
                                y1_real = self.y1_get*(1/self.scale)*pixel_ratio
                                x2_real = self.x2_get * (1/self.scale)
                                y2_real = self.y2_get * (1/self.scale)*pixel_ratio
                                self.distance_points(x1_real, y1_real, x2_real, y2_real)
                                self.real_distance_line.setText(f"{round(self.distance,2)}")
                                self.x1_get=""
                                self.y1_get=""
                                self.x2_get=""
                                self.y2_get=""

                            else:
                                real_distance = image_distance * (1 / (self.scale))
                                real_distance=round(real_distance,2)
                                self.real_distance_line.setText(f"{real_distance}")
                        else:
                            real_distance = image_distance * (1 / (self.scale))
                            real_distance = round(real_distance, 2)
                            self.real_distance_line.setText(f"{real_distance}")

                else:
                    if not self.real_distance_line.text().strip() == "":
                        image_distance = round(float(self.image_distance_line.text()),2)
                        real_distance = round(float(self.real_distance_line.text()),2)
                        self.scale = image_distance / real_distance
                        self.scale=round(self.scale,2)
                        if len(self.scale_values) < 3:
                            self.scale_values.append(self.scale)

                            if len(self.scale_values) == 3:
                                self.show_message()
                                self.scale_line.setText(f"{self.average_scale}")
                                self.scale_values = []
                                return

                        self.scale_line.setText(f"{self.scale}")

    def get_methods(self,rd_direct):

        if rd_direct.isChecked():

            self.set_method.show()
            self.get_distance.hide()
            if self.image_distance_line.text().strip() == "":
                if hasattr(self,'table_widget'):
                    selected_row = self.table_widget.currentRow()
                    if selected_row != -1:

                        self.x1_get = int(self.table_widget.item(selected_row, 0).text())
                        self.y1_get = int(self.table_widget.item(selected_row, 1).text())
                        self.x2_get = int(self.table_widget.item(selected_row, 2).text())
                        self.y2_get = int(self.table_widget.item(selected_row, 3).text())

                        self.distance_points(self.x1_get,self.y1_get,self.x2_get,self.y2_get)
                        self.image_distance_line.setText(f"{round(self.distance,2)}")

    def distance_points(self,x1,y1,x2,y2):
        self.distance = math.sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)
    def back_methods(self,rd_btn,btn_ok,lb_method,lb_height_len,line_height_len,lb_diameter,line_lb_diameter,lb_focus_lenght,line_focus_lenght,set_method,back_method,rd_direct):

        if rd_btn.isChecked():
            lb_height_len.hide()
            line_height_len.hide()
            lb_diameter.hide()
            line_lb_diameter.hide()
            lb_focus_lenght.hide()
            line_focus_lenght.hide()
            set_method.hide()
            back_method.hide()
            rd_btn.show()
            btn_ok.show()
            lb_method.show()
            rd_direct.show()

        if self.get_distance.isVisible():
            self.get_show = True
            self.set_show = False

        if self.set_method.isVisible():
            self.get_show = False
            self.set_show = True


        self.height_len_last_text = self.line_height_len.text()
        self.diameter_last_text = self.line_lb_diameter.text()
        self.focus_lenght_last_text = self.line_focus_lenght.text()

    def back_methods_direct(self,rd_direct,rd_sfiv,set_method,back_method,btn_ok,lb_method):

        if self.get_distance.isVisible():
            self.get_show = True
            self.set_show = False

        if self.set_method.isVisible():
            self.get_show = False
            self.set_show = True

        set_method.hide()
        back_method.hide()
        self.real_distance.hide()
        self.real_distance_line.hide()
        self.image_distance_lb.hide()
        self.image_distance_line.hide()
        self.pixel_ratio_lb.hide()
        self.pixel_ratio_line.hide()
        self.scale_lb.hide()
        self.scale_line.hide()
        self.get_distance.hide()
        self.trade_get_set.hide()
        rd_direct.show()
        rd_sfiv.show()
        btn_ok.show()
        lb_method.show()

        self.pixel_ratio_line_last_text = self.pixel_ratio_line.text()
        self.scale_last_text = self.scale_line.text()
        self.real_distance_last_text = self.real_distance_line.text()
        self.image_distance_last_text = self.image_distance_line.text()

    def add_camera(self,line_camera,list_camera):
        self.list_camera=list_camera
        list_camera.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        count_itens =0
        self.item_exists(list_camera,line_camera.text().strip())
        if not self.item_exists(list_camera, line_camera.text().strip()):
            if not line_camera.text().strip()=="":
                camera=line_camera.text()
                list_camera.addItem(camera)

        selected_items = list_camera.selectedItems()

        if not selected_items:
            return

        for item in selected_items:
            count_itens+=1
        if count_itens == 1:
            str="item"
        elif count_itens>1:
            str="itens"

        message_box = QMessageBox()
        message_box.setWindowTitle("Question")
        message_box.setText(f"Are you sure you want to remove the selected {str}?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        answer = message_box.exec()

        if answer == QMessageBox.Yes:
            for item in selected_items:
                row = list_camera.row(item)
                list_camera.takeItem(row)
        else:
            pass


    def item_exists(self, list_widget,item_text):
        for index in range(list_widget.count()):
            item = list_widget.item(index)
            if item.text() == item_text:
                return True
        return False
