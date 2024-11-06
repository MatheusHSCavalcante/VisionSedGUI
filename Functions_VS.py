import os
from imagegrains import grainsizing, plotting, segmentation_helper, data_loader, gsd_uncertainty

class segmentation():

    def segmentation(self,direct_path,model_path):

        images_files = [file for file in os.listdir(direct_path) if file.endswith('.jpg')]

        if not os.path.exists(direct_path + 'prediction_masks'):

            segmentation_helper.predict_dataset(direct_path, model_path, image_format="jpg", mute=True, return_results=False, save_masks=False, do_subfolders=False)

            imgs, lbls, preds = data_loader.dataset_loader(direct_path, label_str='mask', pred_str='pred')

            for i in range(0, len(images_files)):
                plotting.plot_single_img_pred(imgs[i].replace("\\", "/"), preds[i].replace("\\", "/"), show=True,save=True)

