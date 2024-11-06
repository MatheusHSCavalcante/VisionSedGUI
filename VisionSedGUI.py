from queue import Full
import warnings

from PySide6.QtGui import QShortcut

from GUI.uiVisionSedGUI import *
from PySide6.QtWidgets import *
import PySide6.QtCore
from Custom_Widgets.Widgets import *
import sys
from functionsGUI import *
from PIL import Image, ImageTk

warnings.simplefilter('ignore', UserWarning)
activeWidget = 1
error_txt = ""
stage_1_msg = ""
stage_2_msg = ""
stage_3_msg = ""
stage_4_msg = ""

class MyMainWindow(QMainWindow, Ui_MainWindow):
    #Definindo Variavéis do Escopo
    model = ""
    directory = ""
    fsUtil = None
    count=0

    #Definições dos métodos
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        self.fsUtil = FunctionsUtil()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Vision Sed")
        self.setWindowOpacity(0.95)
        self.id_op_movie = "open_movie"
        self.id_cam="cam_on"
        self.command_prev_cam = 'previous'
        self.command_next_cam = 'next'
        self.ui.home_btn.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.shortcut = QShortcut(QKeySequence("Q"), self)
        self.ui.trade_page_stacked_widget.setCurrentIndex(0)
        self.ui.home_btn.clicked.connect(self.switch_to_homePage)
        self.ui.train_btn.clicked.connect(self.switch_to_trainPage)
        self.ui.segment_btn.clicked.connect(self.switch_to_segmentPage)
        self.ui.measure_btn.clicked.connect(self.switch_to_measurePage)
        self.ui.velocity_btn.clicked.connect(self.switch_to_velocityPage)
        self.ui.open_dir_with_imgs_seg_btn.clicked.connect(self.open_directory)
        self.ui.open_model_seg_btn.clicked.connect(self.open_model)
        self.ui.open_dir_with_imgs_mask_btn.clicked.connect(self.open_directory)
        self.ui.open_model_pre_trained_btn.clicked.connect(self.open_model)
        self.ui.open_dir_with_predicts_btn.clicked.connect(self.open_directory)
        self.ui.open_directory_rename_btn.clicked.connect(self.open_directory)
        self.ui.open_movie.clicked.connect(lambda: self.fsUtil.open_video(self.ui.lb_movie,self.ui.pause_button,self.ui.play_button,self.ui.stop_button,self.ui.back_time_button,self.ui.foward_time_button,self.ui.sound,self.ui.mute_sound,self.ui.volume_slider,self.ui.lb_time_actual,self.ui.lb_total_time,self.ui.slider_time,self.ui.scrollAreaWidgetContents_6_objects,self.ui.icon_sphere,self.ui.horizontalLayout_5,self.ui.help_btn,self.ui.rd_btn_ignored,self.ui.rd_btn_keep,self.ui.rd_btn_keep_expand,self.ui.identify_check_box,self.ui.update_models,self.ui.list_models,self.ui.velocity_page,self.id_op_movie))
        self.ui.camera.clicked.connect(lambda:self.fsUtil.open_video(self.ui.lb_movie,self.ui.pause_button,self.ui.play_button,self.ui.stop_button,self.ui.back_time_button,self.ui.foward_time_button,self.ui.sound,self.ui.mute_sound,self.ui.volume_slider,self.ui.lb_time_actual,self.ui.lb_total_time,self.ui.slider_time,self.ui.scrollAreaWidgetContents_6_objects,self.ui.icon_sphere,self.ui.horizontalLayout_5,self.ui.help_btn,self.ui.rd_btn_ignored,self.ui.rd_btn_keep,self.ui.rd_btn_keep_expand,self.ui.identify_check_box,self.ui.update_models,self.ui.list_models,self.ui.velocity_page,self.id_cam))
        self.ui.add_camera.clicked.connect(lambda:self.fsUtil.add_camera(self.ui.line_camera,self.ui.list_camera))
        self.shortcut.activated.connect(lambda :self.fsUtil.on_q_pressed())
        self.ui.previous_camera.clicked.connect(lambda:self.fsUtil.switch_cam_web_thread(self.command_prev_cam))
        self.ui.next_camera.clicked.connect(lambda: self.fsUtil.switch_cam_web_thread(self.command_next_cam))
        #self.ui.rd_btn_sfiv.clicked.connect(lambda: self.fsUtil.on_persistent_clicked(self.ui.rd_btn_sfiv))
        loadJsonStyle(self, self.ui)

        self.ui.progress_indicator.selectFormProgressIndicatorTheme(3)
        self.ui.progress_indicator.updateFormProgressIndicator(
            formProgressCount=5,
            formProgressAnimationDuration=2000,
            height=40,
            startPercentage=100
            )

        self.ui.main_frame.setGeometry(QRect(30, 0, 1150, 900))
        self.ui.main_container.setGeometry(QRect(30, 0, 1101, 900))

        self.ui.start_btn.clicked.connect(lambda: self.start_btn())
        self.ui.cancel_btn.clicked.connect(lambda: self.stop_btn())
        self.ui.welcome.expandMenu()
        self.ui.help_btn.clicked.connect(lambda:self.restore_or_maximize())

        self.ui.exit_btn.clicked.connect(lambda:self.showExitDialogue())
        self.ui.no_exit.clicked.connect(lambda: self.hideExitDialogue())

        self.ui.adv_btn.clicked.connect(lambda:self.nxtSlide())
        self.ui.next_btn.clicked.connect(lambda: self.nxtSlide())
        self.ui.next_btn.clicked.connect(lambda: self.ui.trade_page_stacked_widget.slideToNextWidget())

        self.ui.home_btn.clicked.connect(lambda:self.home_page_progress())
        self.ui.train_btn.clicked.connect(lambda: self.train_page_progress())
        self.ui.segment_btn.clicked.connect(lambda: self.segment_page_progress())
        self.ui.measure_btn.clicked.connect(lambda: self.measure_page_progress())
        self.ui.velocity_btn.clicked.connect(lambda: self.velocity_page_progress())

        self.ui.prev_btn.clicked.connect(lambda: self.prevSlide())
        self.ui.back_btn.clicked.connect(lambda: self.prevSlide())
        self.ui.back_btn.clicked.connect(lambda: self.ui.trade_page_stacked_widget.slideToPreviousWidget())

        self.ui.seg_btn.clicked.connect(lambda: self.fsUtil.segmentation(self.directory, self.model, self.ui.scrollAreaWidgetContents_4, self.ui.horizontalLayout_3,self.ui.fm_image_overlay, self.ui.fm_image_result,self.ui.segment_page))
        self.ui.clear_seg_btn.clicked.connect(lambda: self.fsUtil.clear(self.ui.fm_image_overlay, self.ui.fm_image_result, self.ui.scrollAreaWidgetContents_4))
        self.ui.train_btn_2.clicked.connect(lambda: self.fsUtil.train(self.directory, self.model, self.ui.fm_train_results_area,self.ui.vertical_layout_train,self.ui.horizontal_layout_train,self.ui.train_page,self.ui.nepochs))
        self.ui.clear_btn.clicked.connect(lambda: self.fsUtil.clear_train(self.ui.fm_train_results))
        self.ui.set_values_filters_btn.clicked.connect(lambda: self.fsUtil.set_values_measure(self.ui.line_edge,self.ui.line_cut,self.ui.line_image_distance, self.ui.line_focal_lenght,self.ui.line_sensor_height,self.ui.line_sensor_width,self.ui.line_pixel_width,self.ui.line_pixel_height,self.ui.set_values_filters_btn,self.ui.lb_measure,self.ui.measure_btn_2,self.ui.lb_clear_measure,self.ui.clear_measure_btn))
        self.ui.clear_values_filters_btn.clicked.connect(lambda:self.fsUtil.clear_set_values_filters(self.ui.line_edge,self.ui.line_cut))
        self.ui.set_values_parameters_btn.clicked.connect(lambda: self.fsUtil.set_values_measure(self.ui.line_edge,self.ui.line_cut,self.ui.line_image_distance, self.ui.line_focal_lenght,self.ui.line_sensor_height,self.ui.line_sensor_width,self.ui.line_pixel_width,self.ui.line_pixel_height,self.ui.set_values_parameters_btn,self.ui.lb_measure,self.ui.measure_btn_2,self.ui.lb_clear_measure,self.ui.clear_measure_btn))
        self.ui.clear_values_parameters_btn.clicked.connect(lambda: self.fsUtil.clear_set_values_parameters(self.ui.line_image_distance, self.ui.line_focal_lenght,self.ui.line_sensor_height,self.ui.line_sensor_width,self.ui.line_pixel_width,self.ui.line_pixel_height))
        self.ui.measure_btn_2.clicked.connect(lambda: self.fsUtil.measure(self.directory,self.ui.scrollAreaWidgetContents_5,self.ui.verticalLayout_9,self.ui.fm_image_measure,self.ui.fm_graph_result_measure,self.ui.measure_page))
        self.ui.clear_measure_btn.clicked.connect(lambda:self.fsUtil.clear_measure(self.ui.fm_image_measure,self.ui.fm_graph_result_measure,self.ui.scrollAreaWidgetContents_5))
        self.ui.rename_files_btn.clicked.connect(lambda:self.fsUtil.rename_files(self.directory))
        self.ui.Ok_method.clicked.connect(lambda:self.fsUtil.ok_method(self.ui.rd_btn_sfiv,self.ui.Ok_method,self.ui.lb_method,self.ui.velocity_page,self.ui.rd_btn_direct))
        self.ui.set_coordinates.clicked.connect(lambda:self.fsUtil.set_coordinates(self.ui.x_coordinate,self.ui.y_coordinate,self.ui.table_coordinates_point,self.ui.x_label,self.ui.y_label,self.ui.x2_label,self.ui.y2_label,True,self.ui.set_coordinates))
        self.ui.add_point.clicked.connect(lambda:self.fsUtil.add_point(self.ui.table_coordinates_point,self.ui.add_point))
        self.ui.clear_point.clicked.connect(lambda:self.fsUtil.clear_coodinates(self.ui.table_coordinates_point))
        self.ui.help_btn.clicked.connect(lambda:self.fsUtil.on_resize_method(self.ui.velocity_page,self.ui.rd_btn_sfiv,self.ui.rd_btn_direct))
        self.ui.delete_models.clicked.connect(lambda:self.fsUtil.delete_models())

        self.show()

    def restore_or_maximize(self):

        if self.isMaximized():
            self.showNormal()
            self.start_active()
            self.format_minimize()
            self.ui.frame_2.setGeometry(QRect(1170, 0, 31, 901))



        else:
            self.showMaximized()
            self.frame_expand()
            self.format_maximize()

    def frame_expand(self):
        self.ui.frame.setGeometry(QRect(0, 0, 31, 1020))
        self.ui.frame_6.setGeometry(QRect(0, 0, 1890, 20))
        self.ui.frame_2.setGeometry(QRect(1890, 0, 31, 900))
        self.ui.frame_7.setGeometry(QRect(0, 1020, 1890, 20))
        self.ui.header_frame.setGeometry(QRect(400, 10, 3000, 121))
        self.ui.header_right.setGeometry(QRect(0, 10, 3000, 121))
        self.ui.main_frame.setGeometry(QRect(30, 140, 1860, 880))
        self.ui.main_container.setGeometry(QRect(10, 120, 1900, 900))

    def showExitDialogue(self):

        if self.ui.exit_container.collapsed:

            self.ui.exit_container.expandMenu()
            self.ui.main_container.collapseMenu()
            self.ui.header_frame.collapseMenu()

        else:
            self.hideExitDialogue()

    def hideExitDialogue(self):

        self.ui.exit_container.collapseMenu()
        self.ui.header_frame.expandMenu()
        self.ui.main_container.expandMenu()
        self.ui.widget_insider_footer_with_btns.expandMenu()

    def start_btn(self):
        self.start_active()
        self.perc()
        self.format_minimize()

    def format_maximize(self):
        self.ui.fm_train_results.setGeometry(QRect(700, 30, 750, 600))
        self.ui.clear_btn.setGeometry(QRect(20, 280, 51, 51))
        self.ui.lb_clear.setGeometry(QRect(75, 290, 51, 31))
        self.ui.fm_image_overlay.setGeometry(QRect(250, 120, 450, 450))
        self.ui.fm_image_result.setGeometry(QRect(750, 120, 350, 450))
        self.ui.scrollArea_3.setGeometry(QRect(1000, 9, 121, 400))
        self.ui.lb_results_Seg.setGeometry(QRect(900, 600, 71, 31))
        self.ui.clear_seg_btn.setGeometry(QRect(615, 62, 51, 51))
        self.ui.lb_clear_seg.setGeometry(QRect(650, 70, 51, 31))
        self.ui.set_values_parameters_btn.setGeometry(QRect(40, 520, 75, 23))
        self.ui.clear_values_parameters_btn.setGeometry(QRect(150, 520, 101, 23))
        self.ui.set_values_filters_btn.setGeometry(QRect(40, 210, 75, 23))
        self.ui.clear_values_filters_btn.setGeometry(QRect(160, 210, 75, 23))
        self.ui.lb_measure.setGeometry(QRect(50, 570, 81, 31))
        self.ui.measure_btn_2.setGeometry(QRect(10, 560, 51, 51))
        self.ui.open_directory_rename_btn.setGeometry(QRect(1260, 10, 51, 51))
        self.ui.open_directory_rename.setGeometry(QRect(1300, 20, 131, 31))
        self.ui.rename_files_btn.setGeometry(QRect(1270, 70, 131, 41))
        self.ui.lb_clear_measure.setGeometry(QRect(170, 570, 51, 31))
        self.ui.clear_measure_btn.setGeometry(QRect(140, 560, 41, 41))
        self.ui.fm_graph_result_measure.setGeometry(QRect(500, 420, 461, 220))
        self.ui.fm_image_measure.setGeometry(QRect(530, 10, 400, 400))
        self.ui.scrollArea_2.setGeometry(QRect(250, 580, 450, 91))
        self.ui.btn_stabilization_movie.setGeometry(QRect(1300, 20, 181, 31))
        self.ui.btn_estimate_velocity.setGeometry(QRect(1300, 60, 181, 31))
        self.ui.lb_movie.setGeometry(QRect(600, 100, 441, 350))
        self.ui.lb_open_movie.setGeometry(QRect(640, 30, 111, 31))
        self.ui.open_movie.setGeometry(QRect(600, 20, 51, 51))
        self.ui.lb_objects.setGeometry(QRect(520, 640, 71, 31))
        self.ui.lb_objects.hide()
        self.ui.scrollArea_4_objects.setGeometry(QRect(600, 580, 450, 91))
        self.ui.lb_coordinates_points.setGeometry(QRect(290, 70, 161, 31))
        self.ui.table_coordinates_point.setGeometry(QRect(250, 100, 241, 411))
        self.ui.add_point.setGeometry(QRect(250, 530, 81, 21))
        self.ui.clear_point.setGeometry(QRect(410, 530, 81, 21))
        self.ui.lb_method.setGeometry(QRect(20, 570, 71, 31))
        self.ui.rd_btn_sfiv.setGeometry(QRect(20, 600, 82, 31))
        self.ui.rd_btn_direct.setGeometry(QRect(100, 600, 82, 31))
        self.ui.x_coordinate.setGeometry(QRect(290, 565, 61, 20))
        self.ui.y_coordinate.setGeometry(QRect(370, 565, 61, 20))
        self.ui.x_label.setGeometry(QRect(270, 565, 21, 20))
        self.ui.y_label.setGeometry(QRect(350, 565, 21, 20))
        self.ui.Ok_method.setGeometry(QRect(200, 605, 31, 21))
        self.ui.set_coordinates.setGeometry(QRect(440, 565, 110, 20))
        self.ui.lb_time_actual.setGeometry(QRect(620, 60, 61, 41))
        self.ui.lb_total_time.setGeometry(QRect(800, 60, 61, 41))
        self.ui.camera.setGeometry(QRect(800, 40, 30, 30))
        self.ui.slider_time.setGeometry(QRect(685, 70, 111, 22))
        self.ui.volume_slider.setGeometry(QRect(570, 340, 22, 71))
        self.ui.sound.setGeometry(QRect(570, 420, 21, 23))
        self.ui.mute_sound.setGeometry(QRect(570, 420, 21, 23))
        self.ui.mute_sound.hide()
        self.ui.stop_button.setGeometry(QRect(570, 150, 21, 23))
        self.ui.pause_button.setGeometry(QRect(570, 120, 21, 23))
        self.ui.play_button.setGeometry(QRect(570, 120, 21, 23))
        self.ui.play_button.hide()
        self.ui.back_time_button.setGeometry(QRect(570, 210, 21, 23))
        self.ui.foward_time_button.setGeometry(QRect(570, 180, 21, 23))
        self.ui.x2_label.setGeometry(QRect(270, 565, 21, 20))
        self.ui.y2_label.setGeometry(QRect(350, 565, 21, 20))
        self.ui.x2_label.hide()
        self.ui.y2_label.hide()
        self.ui.rd_btn_ignored.setGeometry(QRect(1050, 100, 150, 31))
        self.ui.rd_btn_ignored.show()
        self.ui.rd_btn_keep.setGeometry(QRect(1050, 120, 140, 31))
        self.ui.rd_btn_keep.show()
        self.ui.rd_btn_keep_expand.setGeometry(QRect(1050, 140, 220, 31))
        self.ui.rd_btn_keep_expand.show()
        self.ui.identify_check_box.setGeometry(QRect(530, 650, 70, 17))
        self.ui.list_models.setGeometry(QRect(670, 465, 300, 100))
        self.ui.update_models.setGeometry(QRect(565, 620, 30, 30))
        self.ui.delete_models.setGeometry(QRect(650, 465, 20, 20))
        self.ui.nepochs_label.setGeometry(QRect(160, 215, 170, 40))
        self.ui.nepochs.setGeometry(QRect(320, 225, 61, 20))
        self.ui.scale_train.show()
        self.ui.scale_train_line.show()
        self.ui.scale_train.setGeometry(QRect(340, 350, 170, 40))
        self.ui.scale_train_line.setGeometry(QRect(400, 360, 61, 20))
        self.ui.lb_or.setGeometry(QRect(310, 350, 170, 40))
        self.ui.px_mm.setGeometry(QRect(460, 350, 170, 40))
        self.ui.list_camera.setGeometry(QRect(540, 235, 55, 70))
        self.ui.line_camera.setGeometry(QRect(540, 310, 55, 20))
        self.ui.add_camera.setGeometry(QRect(500, 310, 55, 20))
        self.ui.previous_camera.setGeometry(QRect(1060, 430, 120, 20))
        self.ui.next_camera.setGeometry(QRect(1190, 430, 100, 20))

    def format_minimize(self):
        self.ui.fm_train_results.setGeometry(QRect(20, 280, 750, 250))
        self.ui.clear_btn.setGeometry(QRect(680, 20, 51, 51))
        self.ui.lb_clear.setGeometry(QRect(720, 30, 51, 31))
        self.ui.fm_image_overlay.setGeometry(QRect(20, 110, 350, 350))
        self.ui.fm_image_result.setGeometry(QRect(460, 110, 261, 350))
        self.ui.scrollArea_2.setGeometry(QRect(20, 470, 350, 80))
        self.ui.lb_results_Seg.setGeometry(QRect(570, 480, 71, 31))
        self.ui.clear_seg_btn.setGeometry(QRect(615, 62, 51, 51))
        self.ui.lb_clear_seg.setGeometry(QRect(650, 70, 51, 31))
        self.ui.set_values_parameters_btn.setGeometry(QRect(40, 520, 75, 23))
        self.ui.clear_values_parameters_btn.setGeometry(QRect(150, 520, 101, 23))
        self.ui.set_values_filters_btn.setGeometry(QRect(40, 210, 75, 23))
        self.ui.clear_values_filters_btn.setGeometry(QRect(160, 210, 75, 23))
        self.ui.lb_measure.setGeometry(QRect(230, 100, 81, 31))
        self.ui.measure_btn_2.setGeometry(QRect(190, 90, 51, 51))
        self.ui.open_directory_rename_btn.setGeometry(QRect(590, 10, 51, 51))
        self.ui.open_directory_rename.setGeometry(QRect(630, 20, 131, 31))
        self.ui.rename_files_btn.setGeometry(QRect(600, 70, 131, 41))
        self.ui.lb_clear_measure.setGeometry(QRect(230, 160, 51, 31))
        self.ui.clear_measure_btn.setGeometry(QRect(200, 150, 41, 41))
        self.ui.fm_graph_result_measure.setGeometry(QRect(300, 320, 461, 220))
        self.ui.fm_image_measure.setGeometry(QRect(310, 10, 301, 301))
        self.ui.scrollArea_3.setGeometry(QRect(619, 9, 121, 301))
        self.ui.btn_estimate_velocity.setGeometry(QRect(600, 60, 181, 31))
        self.ui.btn_stabilization_movie.setGeometry(QRect(600, 20, 181, 31))
        self.ui.lb_movie.setGeometry(QRect(340, 100, 441, 350))
        self.ui.lb_open_movie.setGeometry(QRect(360, 30, 111, 31))
        self.ui.open_movie.setGeometry(QRect(320, 20, 51, 51))
        self.ui.lb_objects.setGeometry(QRect(200, 510, 71, 31))
        self.ui.lb_objects.hide()
        self.ui.scrollArea_4_objects.setGeometry(QRect(400, 480, 311, 71))
        self.ui.lb_coordinates_points.setGeometry(QRect(10, 50, 161, 31))
        self.ui.table_coordinates_point.setGeometry(QRect(10, 80, 241, 341))
        self.ui.add_point.setGeometry(QRect(10, 425, 81, 21))
        self.ui.clear_point.setGeometry(QRect(170, 425, 81, 21))
        self.ui.lb_method.setGeometry(QRect(20, 500, 71, 31))
        self.ui.rd_btn_sfiv.setGeometry(QRect(20, 520, 82, 31))
        self.ui.rd_btn_direct.setGeometry(QRect(100, 520, 82, 31))
        self.ui.x_coordinate.setGeometry(QRect(50, 460, 61, 20))
        self.ui.y_coordinate.setGeometry(QRect(130, 460, 61, 20))
        self.ui.x_label.setGeometry(QRect(30, 460, 21, 20))
        self.ui.y_label.setGeometry(QRect(110, 460, 21, 20))
        self.ui.Ok_method.setGeometry(QRect(200, 525, 31, 21))
        self.ui.set_coordinates.setGeometry(QRect(200, 460, 110, 20))
        self.ui.lb_time_actual.setGeometry(QRect(340, 60, 61, 41))
        self.ui.lb_total_time.setGeometry(QRect(520, 60, 61, 41))
        self.ui.camera.setGeometry(QRect(520, 40, 30, 30))
        self.ui.slider_time.setGeometry(QRect(410, 70, 111, 22))
        self.ui.volume_slider.setGeometry(QRect(310, 340, 22, 71))
        self.ui.sound.setGeometry(QRect(310, 420, 21, 23))
        self.ui.mute_sound.setGeometry(QRect(310, 420, 21, 23))
        self.ui.mute_sound.hide()
        self.ui.stop_button.setGeometry(QRect(320, 150, 21, 23))
        self.ui.pause_button.setGeometry(QRect(320, 120, 21, 23))
        self.ui.play_button.setGeometry(QRect(320, 120, 21, 23))
        self.ui.play_button.hide()
        self.ui.back_time_button.setGeometry(QRect(320, 210, 21, 23))
        self.ui.foward_time_button.setGeometry(QRect(320, 180, 21, 23))
        self.ui.x2_label.setGeometry(QRect(30, 460, 21, 20))
        self.ui.y2_label.setGeometry(QRect(110, 460, 21, 20))
        self.ui.x2_label.hide()
        self.ui.y2_label.hide()
        self.ui.rd_btn_ignored.hide()
        self.ui.rd_btn_keep.hide()
        self.ui.rd_btn_keep_expand.hide()
        self.ui.identify_check_box.setGeometry(QRect(340, 530, 70, 17))
        self.ui.list_models.setGeometry(QRect(715, 453, 65, 100))
        self.ui.update_models.setGeometry(QRect(360, 500, 30, 30))
        self.ui.delete_models.setGeometry(QRect(690, 460, 20, 20))
        self.ui.nepochs_label.setGeometry(QRect(140, 215, 170, 40))
        self.ui.nepochs.setGeometry(QRect(300, 225, 61, 20))
        self.ui.scale_train.setGeometry(QRect(170, 240, 170, 40))
        self.ui.scale_train_line.setGeometry(QRect(225, 250, 40, 20))
        self.ui.lb_or.setGeometry(QRect(140, 240, 170, 40))
        self.ui.px_mm.setGeometry(QRect(260, 240, 170, 40))
        self.ui.list_camera.setGeometry(QRect(280, 235, 55, 70))
        self.ui.line_camera.setGeometry(QRect(280, 310, 55, 20))
        self.ui.add_camera.setGeometry(QRect(240, 310, 55, 20))
        self.ui.previous_camera.setGeometry(QRect(340, 455, 120, 20))
        self.ui.next_camera.setGeometry(QRect(470, 455, 100, 20))

    def start_active(self):

        global activeWidget
        self.ui.pages.expandMenu()
        self.ui.welcome.collapseMenu()
        self.ui.header_frame.expandMenu()
        self.ui.frame_2.setGeometry(QRect(1180, 0, 20, 900))
        self.ui.frame.setGeometry(QRect(0, 0, 20, 1020))
        self.ui.header_frame.setGeometry(QRect(37, 10, 1121, 121))
        self.ui.widget_insider_footer_with_btns.expandMenu()
        self.ui.main_frame.setGeometry(QRect(30, 130, 1131, 751))

    def perc(self):
        currentPerc = (activeWidget/5)*100
        self.ui.progress_indicator.animateFormProgress(currentPerc)

    def stop_btn(self):

        self.ui.pages.collapseMenu()
        self.ui.welcome.expandMenu()
        self.ui.widget_insider_footer_with_btns.collapseMenu()
        self.ui.header_frame.collapseMenu()
        self.ui.progress_indicator.animateFormProgress(100)
        self.ui.main_frame.setGeometry(QRect(30, 0, 1150, 900))
        self.ui.main_container.setGeometry(QRect(30, 0, 1101, 900))
        self.ui.frame_2.setGeometry(QRect(1170, 0, 31, 901))
        if self.isMaximized():
            self.showNormal()

    def viewNavBtns(self):

        if self.ui.pages.collapsed:
            self.ui.adv_btn.setEnabled(False)
            self.ui.prev_btn.setEnabled(False)
            self.ui.next_btn.setEnabled(False)
            self.ui.back_btn.setEnabled(False)

        else:
            if self.ui.trade_page_stacked_widget.currentIndex() >= 4:
                self.ui.adv_btn.setEnabled(False)
                self.ui.next_btn.setEnabled(False)

            else:
                self.ui.adv_btn.setEnabled(True)
                self.ui.next_btn.setEnabled(True)

            if self.ui.trade_page_stacked_widget.currentIndex() <= 0:
                self.ui.prev_btn.setEnabled(False)
                self.ui.back_btn.setEnabled(False)

            else:
                self.ui.prev_btn.setEnabled(True)
                self.ui.back_btn.setEnabled(True)



    def home_page_progress(self):
        self.ui.home_btn.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.ui.train_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.segment_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.measure_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.velocity_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.progress_indicator.animateFormProgress(20)
    def train_page_progress(self):
        self.ui.home_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.train_btn.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.ui.segment_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.measure_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.velocity_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.progress_indicator.animateFormProgress(40)
    def segment_page_progress(self):
        self.ui.home_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.train_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.segment_btn.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.ui.measure_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.velocity_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.progress_indicator.animateFormProgress(60)
    def measure_page_progress(self):
        self.ui.home_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.train_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.segment_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.measure_btn.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.ui.velocity_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.progress_indicator.animateFormProgress(80)
    def velocity_page_progress(self):
        self.ui.home_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.train_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.segment_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ui.measure_btn.setStyleSheet(u"background-color: rgb(255,255, 255);")
        self.ui.velocity_btn.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.ui.progress_indicator.animateFormProgress(100)

    def nxtSlide(self):
        global activeWidget

        if self.ui.trade_page_stacked_widget.currentIndex() < 4:

            activeWidget = self.ui.trade_page_stacked_widget.currentIndex()+2

        if activeWidget == 1:
            self.home_page_progress()

        elif activeWidget == 2:
            self.train_page_progress()

        elif activeWidget == 3:
            self.segment_page_progress()

        elif activeWidget == 4:
            self.measure_page_progress()

        elif activeWidget == 5:
            self.velocity_page_progress()

        currentPerc = (activeWidget/5)*100
        self.ui.progress_indicator.animateFormProgress(currentPerc)
    def prevSlide(self):
        global activeWidget
        activeWidget=self.ui.trade_page_stacked_widget.currentIndex()

        if activeWidget == 1:
            self.home_page_progress()

        elif activeWidget == 2:
            self.train_page_progress()

        elif activeWidget == 3:
            self.segment_page_progress()

        elif activeWidget == 4:
            self.measure_page_progress()

        elif activeWidget == 5:
            self.velocity_page_progress()

        currentPerc = (activeWidget / 5) * 100
        self.ui.progress_indicator.animateFormProgress(currentPerc)

        currentPerc=(activeWidget/5)*100
        self.ui.progress_indicator.animateFormProgress(currentPerc)

    def switch_to_homePage(self):
        self.ui.trade_page_stacked_widget.setCurrentIndex(0)

    def switch_to_trainPage(self):
        self.ui.trade_page_stacked_widget.setCurrentIndex(1)

    def switch_to_segmentPage(self):
        self.ui.trade_page_stacked_widget.setCurrentIndex(2)

    def switch_to_measurePage(self):
        self.ui.trade_page_stacked_widget.setCurrentIndex(3)

    def switch_to_velocityPage(self):
        self.ui.trade_page_stacked_widget.setCurrentIndex(4)

    def open_directory(self):
        self.directory = QFileDialog.getExistingDirectory()

    def open_model(self):
        self.model = QFileDialog.getOpenFileName()[0]


