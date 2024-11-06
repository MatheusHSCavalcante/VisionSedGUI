import pathlib
import subprocess
import time
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
import nvidia_smi
class FunctionsUtil():

    def segmentation(self, direct_path, file_path, scroll_area, horizontal_layout, frame_image, frame_result):
        images_list = []
        images_vars = []
        icon = []
        images_list_pred = []
        images_files = [file for file in os.listdir(direct_path) if file.endswith('.jpg')]
        if not os.path.exists(direct_path + 'prediction_masks'):
            segmentation_helper.predict_dataset(direct_path, file_path, image_format="jpg", mute=True,
                                        return_results=False, save_masks=True, do_subfolders=False)

        imgs, lbls, preds = data_loader.dataset_loader(direct_path, label_str='mask', pred_str='pred')

        for i in range(0, len(imgs)):
            plotting.plot_single_img_pred(imgs[i].replace("\\", "/"), preds[i].replace("\\", "/"), save=True)

        direct_path_pred = direct_path + "/" + "prediction_masks"
        images_pred_files = os.listdir(direct_path_pred)

        for k in range(0, len(images_files)):
            images_list_pred.append([(Image.open(direct_path_pred + "/" + images_pred_files[k]))])

        for i in range(0, len(images_files)):
            images_list.append([Image.open(direct_path + "/" + images_files[i])])
            images_vars.append(f'img_{i}')

        filters = {'edge': [False, .05], 'px_cutoff': [False, 12]}
        mask_path = os.path.splitext(os.path.basename(file_path))[0]
        results_seg = "Results"
        results_path_seg = os.path.join(direct_path, results_seg)

        if not results_path_seg:
            os.mkdir(results_path_seg)

        eval_results_fh_boosted = segmentation_helper.eval_set(imgs, lbls, preds, data_id=mask_path,tar_dir=results_path_seg,filters=filters)
        direct_path_last = pathlib.PurePath(direct_path)
        test_idxs1 = segmentation_helper.find_test_idxs(lbls)

        elem = {
            'dataset': str(direct_path_last.name),
            'model_id': 'FH',
            'colors': ['m', 'palevioletred'],
            'images': False,
            'std': True,
            'avg_model': True
        }

        plt.figure(figsize=(5, 8))
        plt.plot()
        plt.title('Results Model')
        plotting.AP_IoU_summary_plot([eval_results_fh_boosted], elem, test_idx_list=test_idxs1)
        dir_results = results_path_seg + '/' + f'{mask_path}''.jpg'

        self.display_images(images_vars, scroll_area, horizontal_layout, icon, direct_path_pred, images_pred_files, frame_image, frame_result, dir_results)
        plt.close()
        plt.cla()
        plt.clf()

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
            images_vars[n].setIconSize(QSize(100, 100))
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
            button.deleteLater()

    def train(self,directory,model,frame_train,vertical_layout,horizontal_layout,page):
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        lb_progress_train = QLabel(page)
        lb_progress_train.setObjectName(u"lb_progress_train")
        lb_progress_train.setGeometry(450,80,311, 50)
        lb_progress_train.setStyleSheet(u"color: none;\n""background-color: none;\n""border:none;\n""")
        lb_progress_train.setText(QCoreApplication.translate("MainWindow", "Training...", None))
        lb_progress_train.setFont(font)
        lb_progress_train.show()
        lb_train_results_teste = QLabel(frame_train)
        lb_train_results_teste.setObjectName(u"lb_train_results")
        lb_train_results_teste.setGeometry(QRect(0, 0, 650, 16777215))
        lb_train_results_teste.setMinimumSize(QSize(650, 16777215))
        lb_train_results_teste.setStyleSheet(u"color: none;\n""background-color: none;\n""border-radius:10px;\n""")
        vertical_layout.addWidget(lb_train_results_teste)
        lb_train_results_teste.show()
        time.sleep(1)
        self.train_progress(directory,model,lb_train_results_teste)
    def train_progress(self,directory,model,lb_train_results_teste):
        print(f"PyTorch version: {torch.__version__}")
        print(f"GPU available for pytorch: {torch.cuda.is_available()}")
        train_images, train_masks, test_images, test_masks = data_loader.find_data(directory)
        segmentation_helper.check_labels(train_masks)
        segmentation_helper.check_labels(test_masks)
        segmentation_helper.check_im_label_pairs(train_images, train_masks)
        segmentation_helper.check_im_label_pairs(test_images, test_masks)

        if model:
            model_path = model
        else:
            model_path = "nuclei"

        train_path = directory + "/" + "train" + "/"
        test_path = directory + "/" + "test" + "/"
        mask_filter = '_mask'
        train_str = f'python -m cellpose --use_gpu --verbose --train --dir {train_path} --test_dir {test_path} --pretrained_model {model_path} --mask_filter {mask_filter}'
        print(train_str)
        training = subprocess.check_output(train_str,shell=True)
        decoded_output = training.decode()
        print(decoded_output)

        #lb_train_results_teste.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        lb_train_results_teste.setText(QCoreApplication.translate("MainWindow", decoded_output, None))
        lb_train_results_teste.adjustSize()

    def clear_train(self, directory, model_path):
        print("Ainda não implementado")






