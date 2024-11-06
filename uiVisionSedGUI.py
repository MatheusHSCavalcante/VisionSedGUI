# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VisionSedGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QScrollBar, QTableWidget,QTableWidgetItem, QRadioButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget,QSlider,QListWidget)

from Custom_Widgets.QCustomProgressIndicator import QCustomProgressIndicator
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.Widgets import *
import resources_rc
import warnings
warnings.simplefilter('ignore', UserWarning)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setMinimumSize(QSize(1200, 900))
        MainWindow.setMaximumSize(QSize(1900, 1200))

        #MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        MainWindow.setStyleSheet(u"background-color:transparent")
        #MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border:none;\n"
"background-color: none;")
        self.centralwidget.setMinimumSize(QSize(1200, 900))
        self.centralwidget.setMaximumSize(QSize(1900, 1200))
        self.header_frame = QCustomSlideMenu(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(16777215,16777215)
        self.header_frame.setMinimumSize(1121, 121)
        self.header_frame.setGeometry(QRect(40, 10, 1121, 121))
        self.header_frame.setStyleSheet(u"border:solid black;\n"
"background-color: rgb(0, 0, 0);\n"
"border-width:18px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0));")
        #self.header_frame.setFrameShape(QFrame.StyledPanel)
        #self.header_frame.setFrameShadow(QFrame.Raised)
        self.header_right = QFrame(self.header_frame)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setEnabled(True)
        self.header_right.setGeometry(QRect(18, 10, 1091, 101))
        self.header_right.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0));\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;")
        self.header_right.setFrameShape(QFrame.StyledPanel)
        self.header_right.setFrameShadow(QFrame.Raised)
        self.velocity_btn = QToolButton(self.header_right)
        self.velocity_btn.setObjectName(u"velocity_btn")
        self.velocity_btn.setGeometry(QRect(790, 20, 81, 51))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.velocity_btn.setFont(font)
        self.velocity_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/velocity_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.velocity_btn.setIcon(icon)
        self.velocity_btn.setIconSize(QSize(30, 30))
        self.train_btn = QToolButton(self.header_right)
        self.train_btn.setObjectName(u"train_btn")
        self.train_btn.setGeometry(QRect(330, 20, 81, 51))
        self.train_btn.setFont(font)
        self.train_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/train_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.train_btn.setIcon(icon1)
        self.train_btn.setIconSize(QSize(30, 30))
        self.measure_btn = QToolButton(self.header_right)
        self.measure_btn.setObjectName(u"measure_btn")
        self.measure_btn.setGeometry(QRect(630, 20, 81, 51))
        self.measure_btn.setFont(font)
        self.measure_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/measure_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.measure_btn.setIcon(icon2)
        self.measure_btn.setIconSize(QSize(30, 30))
        self.segment_btn = QToolButton(self.header_right)
        self.segment_btn.setObjectName(u"segment_btn")
        self.segment_btn.setGeometry(QRect(480, 20, 81, 51))
        self.segment_btn.setFont(font)
        self.segment_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/segment_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.segment_btn.setIcon(icon3)
        self.segment_btn.setIconSize(QSize(30, 30))
        self.adv_btn = QToolButton(self.header_right)
        self.adv_btn.setObjectName(u"adv_btn")
        self.adv_btn.setGeometry(QRect(90, 30, 51, 41))
        self.adv_btn.setFont(font)
        self.adv_btn.setStyleSheet(u"background-color:none;\n"
"border:none\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.adv_btn.setIcon(icon4)
        self.adv_btn.setIconSize(QSize(30, 30))
        self.prev_btn = QToolButton(self.header_right)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setGeometry(QRect(30, 30, 51, 41))
        self.prev_btn.setFont(font)
        self.prev_btn.setStyleSheet(u"background-color:none;\n"
"border:none\n"
"\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_btn.setIcon(icon5)
        self.prev_btn.setIconSize(QSize(36, 36))
        self.home_btn = QToolButton(self.header_right)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setGeometry(QRect(190, 20, 81, 51))
        self.home_btn.setFont(font)
        self.home_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Icons/home_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon6)
        self.home_btn.setIconSize(QSize(30, 30))
        self.frame_4 = QFrame(self.header_right)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(900, 0, 191, 101))
        self.frame_4.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: none\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_design2 = QFrame(self.frame_4)
        self.frame_design2.setObjectName(u"frame_design2")
        self.frame_design2.setEnabled(False)
        self.frame_design2.setGeometry(QRect(10, 0, 181, 16))
        self.frame_design2.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design2.setFrameShape(QFrame.StyledPanel)
        self.frame_design2.setFrameShadow(QFrame.Raised)
        self.frame_design3 = QFrame(self.frame_4)
        self.frame_design3.setObjectName(u"frame_design3")
        self.frame_design3.setEnabled(False)
        self.frame_design3.setGeometry(QRect(10, 80, 181, 16))
        self.frame_design3.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design3.setFrameShape(QFrame.StyledPanel)
        self.frame_design3.setFrameShadow(QFrame.Raised)
        self.help_btn = QToolButton(self.frame_4)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setGeometry(QRect(80, 20, 41, 51))
        self.help_btn.setFont(font)
        self.help_btn.setStyleSheet(u"background-color:none;\n"
"border:none\n"
"\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Icons/circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btn.setIcon(icon7)
        self.help_btn.setIconSize(QSize(25, 25))
        self.exit_btn = QToolButton(self.frame_4)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(130, 10, 41, 61))
        self.exit_btn.setStyleSheet(u"background-color:none;\n"
"border:none\n"
"\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon8)
        self.exit_btn.setIconSize(QSize(35, 35))
        self.minimize_btn = QToolButton(self.frame_4)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setGeometry(QRect(40, 32, 31, 41))
        self.minimize_btn.setFont(font)
        self.minimize_btn.setStyleSheet(u"background-color:none;\n"
"border:none\n"
"\n"
"\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Icons/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon9)
        self.minimize_btn.setIconSize(QSize(25, 25))
        self.frame_design1 = QFrame(self.frame_4)
        self.frame_design1.setObjectName(u"frame_design1")
        self.frame_design1.setEnabled(False)
        self.frame_design1.setGeometry(QRect(170, 0, 16, 101))
        self.frame_design1.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design1.setFrameShape(QFrame.StyledPanel)
        self.frame_design1.setFrameShadow(QFrame.Raised)
        self.frame_design4 = QFrame(self.frame_4)
        self.frame_design4.setObjectName(u"frame_design4")
        self.frame_design4.setEnabled(False)
        self.frame_design4.setGeometry(QRect(0, 0, 31, 101))
        self.frame_design4.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design4.setFrameShape(QFrame.StyledPanel)
        self.frame_design4.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.header_right)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(False)
        self.frame_3.setGeometry(QRect(280, 0, 31, 101))
        self.frame_3.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: none\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(False)
        self.frame_5.setGeometry(QRect(0, 0, 31, 101))
        self.frame_5.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: none\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_design16 = QFrame(self.frame_5)
        self.frame_design16.setObjectName(u"frame_design16")
        self.frame_design16.setEnabled(False)
        self.frame_design16.setGeometry(QRect(0, 0, 31, 101))
        self.frame_design16.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(27, 0, 122, 255), stop:0.05 rgba(57, 25, 173, 255), stop:0.352273 rgba(90, 37, 66, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design16.setFrameShape(QFrame.StyledPanel)
        self.frame_design16.setFrameShadow(QFrame.Raised)
        self.frame_design13 = QFrame(self.header_right)
        self.frame_design13.setObjectName(u"frame_design13")
        self.frame_design13.setEnabled(False)
        self.frame_design13.setGeometry(QRect(430, 0, 31, 101))
        self.frame_design13.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(27, 196, 122, 255), stop:0.05 rgba(57, 210, 173, 255), stop:0.352273 rgba(90, 37, 66, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design13.setFrameShape(QFrame.StyledPanel)
        self.frame_design13.setFrameShadow(QFrame.Raised)
        self.frame_design10 = QFrame(self.header_right)
        self.frame_design10.setObjectName(u"frame_design10")
        self.frame_design10.setEnabled(False)
        self.frame_design10.setGeometry(QRect(580, 0, 31, 101))
        self.frame_design10.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(126, 27, 122, 255), stop:0.05 rgba(167, 55, 173, 255), stop:0.352273 rgba(90, 37, 66, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design10.setFrameShape(QFrame.StyledPanel)
        self.frame_design10.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.header_right)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(False)
        self.frame_9.setGeometry(QRect(730, 0, 31, 101))
        self.frame_9.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(230, 252, 93, 255), stop:0.05 rgba(185, 182, 48, 255), stop:0.352273 rgba(90, 37, 66, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_design7 = QFrame(self.frame_9)
        self.frame_design7.setObjectName(u"frame_design7")
        self.frame_design7.setEnabled(False)
        self.frame_design7.setGeometry(QRect(0, 0, 31, 101))
        self.frame_design7.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(230, 252, 93, 255), stop:0.05 rgba(185, 182, 48, 255), stop:0.352273 rgba(90, 37, 66, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design7.setFrameShape(QFrame.StyledPanel)
        self.frame_design7.setFrameShadow(QFrame.Raised)
        self.frame_design19 = QFrame(self.header_right)
        self.frame_design19.setObjectName(u"frame_design19")
        self.frame_design19.setEnabled(False)
        self.frame_design19.setGeometry(QRect(151, 0, 31, 101))
        self.frame_design19.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design19.setFrameShape(QFrame.StyledPanel)
        self.frame_design19.setFrameShadow(QFrame.Raised)
        self.frame_design5 = QFrame(self.header_right)
        self.frame_design5.setObjectName(u"frame_design5")
        self.frame_design5.setEnabled(False)
        self.frame_design5.setGeometry(QRect(760, 0, 141, 16))
        self.frame_design5.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design5.setFrameShape(QFrame.StyledPanel)
        self.frame_design5.setFrameShadow(QFrame.Raised)
        self.frame_design6 = QFrame(self.header_right)
        self.frame_design6.setObjectName(u"frame_design6")
        self.frame_design6.setEnabled(False)
        self.frame_design6.setGeometry(QRect(760, 80, 141, 16))
        self.frame_design6.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design6.setFrameShape(QFrame.StyledPanel)
        self.frame_design6.setFrameShadow(QFrame.Raised)
        self.frame_design9 = QFrame(self.header_right)
        self.frame_design9.setObjectName(u"frame_design9")
        self.frame_design9.setEnabled(False)
        self.frame_design9.setGeometry(QRect(610, 80, 121, 16))
        self.frame_design9.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design9.setFrameShape(QFrame.StyledPanel)
        self.frame_design9.setFrameShadow(QFrame.Raised)
        self.frame_design8 = QFrame(self.header_right)
        self.frame_design8.setObjectName(u"frame_design8")
        self.frame_design8.setEnabled(False)
        self.frame_design8.setGeometry(QRect(610, 0, 121, 16))
        self.frame_design8.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design8.setFrameShape(QFrame.StyledPanel)
        self.frame_design8.setFrameShadow(QFrame.Raised)
        self.frame_design12 = QFrame(self.header_right)
        self.frame_design12.setObjectName(u"frame_design12")
        self.frame_design12.setEnabled(False)
        self.frame_design12.setGeometry(QRect(460, 80, 121, 16))
        self.frame_design12.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design12.setFrameShape(QFrame.StyledPanel)
        self.frame_design12.setFrameShadow(QFrame.Raised)
        self.frame_design11 = QFrame(self.header_right)
        self.frame_design11.setObjectName(u"frame_design11")
        self.frame_design11.setEnabled(False)
        self.frame_design11.setGeometry(QRect(460, 0, 121, 16))
        self.frame_design11.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design11.setFrameShape(QFrame.StyledPanel)
        self.frame_design11.setFrameShadow(QFrame.Raised)
        self.frame_design15 = QFrame(self.header_right)
        self.frame_design15.setObjectName(u"frame_design15")
        self.frame_design15.setEnabled(False)
        self.frame_design15.setGeometry(QRect(310, 80, 121, 16))
        self.frame_design15.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design15.setFrameShape(QFrame.StyledPanel)
        self.frame_design15.setFrameShadow(QFrame.Raised)
        self.frame_design14 = QFrame(self.header_right)
        self.frame_design14.setObjectName(u"frame_design14")
        self.frame_design14.setEnabled(False)
        self.frame_design14.setGeometry(QRect(310, 0, 121, 16))
        self.frame_design14.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design14.setFrameShape(QFrame.StyledPanel)
        self.frame_design14.setFrameShadow(QFrame.Raised)
        self.frame_design17 = QFrame(self.header_right)
        self.frame_design17.setObjectName(u"frame_design17")
        self.frame_design17.setEnabled(False)
        self.frame_design17.setGeometry(QRect(180, 0, 101, 16))
        self.frame_design17.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design17.setFrameShape(QFrame.StyledPanel)
        self.frame_design17.setFrameShadow(QFrame.Raised)
        self.frame_design18 = QFrame(self.header_right)
        self.frame_design18.setObjectName(u"frame_design18")
        self.frame_design18.setEnabled(False)
        self.frame_design18.setGeometry(QRect(180, 80, 101, 20))
        self.frame_design18.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design18.setFrameShape(QFrame.StyledPanel)
        self.frame_design18.setFrameShadow(QFrame.Raised)
        self.frame_design22 = QFrame(self.header_right)
        self.frame_design22.setObjectName(u"frame_design22")
        self.frame_design22.setEnabled(False)
        self.frame_design22.setGeometry(QRect(0, 0, 16, 101))
        self.frame_design22.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design22.setFrameShape(QFrame.StyledPanel)
        self.frame_design22.setFrameShadow(QFrame.Raised)
        self.frame_design21 = QFrame(self.header_right)
        self.frame_design21.setObjectName(u"frame_design21")
        self.frame_design21.setEnabled(False)
        self.frame_design21.setGeometry(QRect(10, 80, 141, 16))
        self.frame_design21.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design21.setFrameShape(QFrame.StyledPanel)
        self.frame_design21.setFrameShadow(QFrame.Raised)
        self.frame_design20 = QFrame(self.header_right)
        self.frame_design20.setObjectName(u"frame_design20")
        self.frame_design20.setEnabled(False)
        self.frame_design20.setGeometry(QRect(10, 0, 141, 16))
        self.frame_design20.setStyleSheet(u"border:solid black;\n"
"border-color:rgb(0,0,0);\n"
"border-width:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.05 rgba(255, 255, 255, 255), stop:0.352273 rgba(255, 255, 255, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.frame_design20.setFrameShape(QFrame.StyledPanel)
        self.frame_design20.setFrameShadow(QFrame.Raised)
        self.frame_4.raise_()
        self.velocity_btn.raise_()
        self.train_btn.raise_()
        self.measure_btn.raise_()
        self.segment_btn.raise_()
        self.adv_btn.raise_()
        self.prev_btn.raise_()
        self.home_btn.raise_()
        self.frame_3.raise_()
        self.frame_design13.raise_()
        self.frame_design10.raise_()
        self.frame_9.raise_()
        self.frame_design19.raise_()
        self.frame_design5.raise_()
        self.frame_design6.raise_()
        self.frame_design9.raise_()
        self.frame_design8.raise_()
        self.frame_design12.raise_()
        self.frame_design11.raise_()
        self.frame_design15.raise_()
        self.frame_design14.raise_()
        self.frame_design17.raise_()
        self.frame_design18.raise_()
        self.frame_design22.raise_()
        self.frame_design21.raise_()
        self.frame_design20.raise_()
        self.main_frame = QCustomSlideMenu(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(30, 130, 1131, 751))
        self.main_frame.setMaximumSize(1920, 1200)
        self.main_frame.setStyleSheet(u"border:solid black;\n"
"background-color: rgb(0,0,0);\n"
"border-width:1px;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        #self.main_frame.setFrameShape(QFrame.StyledPanel)
        #self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.main_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.main_container = QCustomSlideMenu(self.main_frame)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setMaximumSize(QSize(1900,1200))
        self.main_container.setGeometry(QRect(10, -14, 1200, 900))
        self.main_container.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));\n"
"border-width:3px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0))\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.main_container)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.middle_widget = QFrame(self.main_container)
        self.middle_widget.setObjectName(u"middle_widget")
        self.middle_widget.setMaximumSize(QSize(16777215, 16777215))
        self.middle_widget.setStyleSheet(u"border-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.middle_widget.setFrameShape(QFrame.StyledPanel)
        self.middle_widget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.middle_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_frame_middle_widget = QFrame(self.middle_widget)
        self.left_frame_middle_widget.setObjectName(u"left_frame_middle_widget")
        self.left_frame_middle_widget.setMinimumSize(QSize(300, 516))
        self.left_frame_middle_widget.setMaximumSize(QSize(300, 900))
        self.left_frame_middle_widget.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 0, 0, 69), stop:0.375 rgba(160, 165, 59, 69), stop:0.414773 rgba(234, 183, 39, 145), stop:0.448864 rgba(144, 138, 0, 208), stop:0.477581 rgba(173, 151, 36, 130), stop:0.511364 rgba(144, 120, 109, 130), stop:0.539773 rgba(151, 146, 34, 130), stop:0.545455 rgba(178, 178, 73, 130), stop:0.556818 rgba(174, 156, 55, 255), stop:0.602273 rgba(165, 133, 0, 130), stop:0.625 rgba(144, 128, 0, 69), stop:1 rgba(0, 0, 0, 69));\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.left_frame_middle_widget.setFrameShape(QFrame.StyledPanel)
        self.left_frame_middle_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.left_frame_middle_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_image_pg = QLabel(self.left_frame_middle_widget)
        self.lb_image_pg.setObjectName(u"lb_image_pg")
        self.lb_image_pg.setMaximumSize(QSize(16777215, 16777215))
        self.lb_image_pg.setPixmap(QPixmap(u":/Imgs/Icons/Imagem.png"))
        self.lb_image_pg.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.lb_image_pg)


        self.horizontalLayout_2.addWidget(self.left_frame_middle_widget)

        self.welcome = QCustomSlideMenu(self.middle_widget)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setMinimumSize(QSize(0, 0))
        self.welcome.setMaximumSize(QSize(16777215, 16777215))
        self.welcome.setSizeIncrement(QSize(0, 0))
        self.welcome.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.welcome)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_lb_tutorial = QFrame(self.welcome)
        self.frame_lb_tutorial.setObjectName(u"frame_lb_tutorial")
        self.frame_lb_tutorial.setFrameShape(QFrame.StyledPanel)
        self.frame_lb_tutorial.setFrameShadow(QFrame.Raised)
        self.frame_lb_tutorial.setMinimumSize(QSize(0, 500))
        self.frame_lb_tutorial.setMaximumSize(QSize(800, 500))
        self.train_tutorial_lb = QLabel(self.frame_lb_tutorial)
        self.train_tutorial_lb.setObjectName(u"train_tutorial_lb")
        self.train_tutorial_lb.setGeometry(QRect(20, 240, 171, 41))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(16)
        self.train_tutorial_lb.setFont(font1)
        self.train_tutorial_lb.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.segment_tutorial_lb = QLabel(self.frame_lb_tutorial)
        self.segment_tutorial_lb.setObjectName(u"segment_tutorial_lb")
        self.segment_tutorial_lb.setGeometry(QRect(210, 240, 171, 41))
        self.segment_tutorial_lb.setFont(font1)
        self.segment_tutorial_lb.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.measure_tutorial_lb = QLabel(self.frame_lb_tutorial)
        self.measure_tutorial_lb.setObjectName(u"measure_tutorial_lb")
        self.measure_tutorial_lb.setGeometry(QRect(400, 240, 171, 41))
        self.measure_tutorial_lb.setFont(font1)
        self.measure_tutorial_lb.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.velocity_tutorial_lb = QLabel(self.frame_lb_tutorial)
        self.velocity_tutorial_lb.setObjectName(u"velocity_tutorial_lb")
        self.velocity_tutorial_lb.setGeometry(QRect(590, 240, 171, 41))
        self.velocity_tutorial_lb.setFont(font1)
        self.velocity_tutorial_lb.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_welcome = QLabel(self.frame_lb_tutorial)
        self.lb_welcome.setObjectName(u"lb_welcome")
        self.lb_welcome.setGeometry(QRect(230, 10, 271, 21))
        self.lb_welcome.setMaximumSize(QSize(16777200, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.lb_welcome.setFont(font2)
        self.lb_welcome.setLayoutDirection(Qt.LeftToRight)
        self.lb_welcome.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"border:none;")
        self.lb_welcome.setScaledContents(False)
        self.lb_welcome.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.measure_tutorial_btn = QToolButton(self.frame_lb_tutorial)
        self.measure_tutorial_btn.setObjectName(u"measure_tutorial_btn")
        self.measure_tutorial_btn.setGeometry(QRect(590, 50, 171, 181))
        icon10 = QIcon()
        icon10.addFile(u":/Imgs/F:/Menu/Icons/Imagem1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.measure_tutorial_btn.setIcon(icon10)
        self.measure_tutorial_btn.setIconSize(QSize(200, 200))
        self.segment_tutorial_btn = QToolButton(self.frame_lb_tutorial)
        self.segment_tutorial_btn.setObjectName(u"segment_tutorial_btn")
        self.segment_tutorial_btn.setGeometry(QRect(210, 50, 171, 181))
        self.segment_tutorial_btn.setIcon(icon10)
        self.segment_tutorial_btn.setIconSize(QSize(200, 200))
        self.velocity_tutorial_btn = QToolButton(self.frame_lb_tutorial)
        self.velocity_tutorial_btn.setObjectName(u"velocity_tutorial_btn")
        self.velocity_tutorial_btn.setGeometry(QRect(400, 50, 171, 181))
        self.velocity_tutorial_btn.setIcon(icon10)
        self.velocity_tutorial_btn.setIconSize(QSize(200, 200))
        self.train_tutorial_btn = QToolButton(self.frame_lb_tutorial)
        self.train_tutorial_btn.setObjectName(u"train_tutorial_btn")
        self.train_tutorial_btn.setGeometry(QRect(20, 50, 171, 181))
        self.train_tutorial_btn.setIcon(icon10)
        self.train_tutorial_btn.setIconSize(QSize(217, 239))

        self.verticalLayout_5.addWidget(self.frame_lb_tutorial)

        self.frame_8 = QFrame(self.welcome)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: none;\n"
"border-color:none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.start_btn = QToolButton(self.frame_8)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(340, 100, 103, 103))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy)
        self.start_btn.setFont(font2)
        self.start_btn.setStyleSheet(u"\n"
"border:none;\n"
"background-color:none;")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/F:/Menu/Icons/play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon11)
        self.start_btn.setIconSize(QSize(100, 100))
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 40, 341, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:none;")

        self.verticalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.welcome)

        self.pages = QCustomSlideMenu(self.middle_widget)
        self.pages.setObjectName(u"pages")
        self.pages.setMaximumSize(QSize(0, 16777215))
        self.pages.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));")
        self.verticalLayout_6 = QVBoxLayout(self.pages)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.pages)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"border-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0));")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 22, 22))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.trade_page_stacked_widget = QCustomQStackedWidget(self.scrollAreaWidgetContents)
        self.trade_page_stacked_widget.setObjectName(u"trade_page_stacked_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.trade_page_stacked_widget.sizePolicy().hasHeightForWidth())
        self.trade_page_stacked_widget.setSizePolicy(sizePolicy1)
        self.trade_page_stacked_widget.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setStrikeOut(False)
        self.trade_page_stacked_widget.setFont(font3)
        self.trade_page_stacked_widget.setAutoFillBackground(False)
        self.trade_page_stacked_widget.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0852273 rgba(185, 63, 88, 255), stop:0.221591 rgba(156, 34, 68, 255), stop:0.278409 rgba(167, 43, 75, 255), stop:0.386364 rgba(162, 39, 79, 255), stop:0.5 rgba(155, 34, 54, 255), stop:0.653409 rgba(147, 41, 61, 255), stop:0.857955 rgba(0, 0, 0, 255), stop:0.965909 rgba(0, 0, 0, 255));\n"
"background-color: rgb(208, 208, 208);")
        self.trade_page_stacked_widget.setLineWidth(1)
        self.trade_page_stacked_widget.setMidLineWidth(0)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        font4 = QFont()
        font4.setPointSize(8)
        self.home_page.setFont(font4)

        self.lb_title_train_from_start = QLabel(self.home_page)
        self.lb_title_train_from_start.setObjectName(u"lb_title_train_from_start")
        self.lb_title_train_from_start.setGeometry(QRect(10, 0, 211, 42))
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(28)
        font5.setBold(True)
        self.lb_title_train_from_start.setFont(font5)
        self.lb_title_train_from_start.setStyleSheet(u"background-color:none;\n"
"color: rgb(0, 0, 0);\n"
"border:none\n"
"\n"
"")
        self.trade_page_stacked_widget.addWidget(self.home_page)
        self.train_page = QWidget()
        self.train_page.setObjectName(u"train_page")
        self.lb_title_train_from_start_2 = QLabel(self.train_page)
        self.lb_title_train_from_start_2.setObjectName(u"lb_title_train_from_start_2")
        self.lb_title_train_from_start_2.setGeometry(QRect(10, 0, 211, 42))
        self.lb_title_train_from_start_2.setFont(font5)
        self.lb_title_train_from_start_2.setStyleSheet(u"background-color:none;\n"
                                                       "color: rgb(0, 0, 0);\n"
                                                       "border:none\n"
                                                       "")
        self.open_dir_with_imgs_mask_btn = QToolButton(self.train_page)
        self.open_dir_with_imgs_mask_btn.setObjectName(u"open_dir_with_imgs_mask_btn")
        self.open_dir_with_imgs_mask_btn.setGeometry(QRect(20, 70, 51, 51))
        self.open_dir_with_imgs_mask_btn.setStyleSheet(u"background-color: none;\n"
                                                       "border-color: none;\n"
                                                       "")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/Icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_dir_with_imgs_mask_btn.setIcon(icon12)
        self.open_dir_with_imgs_mask_btn.setIconSize(QSize(30, 30))
        self.lb_open_dir_with_imgs_mask = QLabel(self.train_page)
        self.lb_open_dir_with_imgs_mask.setObjectName(u"lb_open_dir_with_imgs_mask")
        self.lb_open_dir_with_imgs_mask.setGeometry(QRect(70, 80, 311, 31))
        self.lb_open_dir_with_imgs_mask.setFont(font)
        self.lb_open_dir_with_imgs_mask.setStyleSheet(u"background-color: none;\n"
                                                      "border-color:none;")
        self.open_model_pre_trained_btn = QToolButton(self.train_page)
        self.open_model_pre_trained_btn.setObjectName(u"open_model_pre_trained_btn")
        self.open_model_pre_trained_btn.setGeometry(QRect(20, 140, 51, 51))
        self.open_model_pre_trained_btn.setStyleSheet(u"background-color: none;\n"
                                                      "border-color: none;\n"
                                                      "")
        icon13 = QIcon()
        icon13.addFile(u":/Icons/Icons/archive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_model_pre_trained_btn.setIcon(icon13)
        self.open_model_pre_trained_btn.setIconSize(QSize(30, 30))
        self.lb_open_model_pre_trained = QLabel(self.train_page)
        self.lb_open_model_pre_trained.setObjectName(u"lb_open_model_pre_trained")
        self.lb_open_model_pre_trained.setGeometry(QRect(70, 150, 291, 31))
        self.lb_open_model_pre_trained.setFont(font)
        self.lb_open_model_pre_trained.setStyleSheet(u"background-color: none;\n"
                                                     "border-color:none;")
        self.nepochs_label=QLabel(self.train_page)
        self.nepochs_label.setObjectName(u"nepochs_label")
        self.nepochs_label.setGeometry(QRect(140, 225, 61, 20))
        self.nepochs_label.setFont(font)
        self.nepochs_label.setStyleSheet(u"background-color: none;\n"
                                                     "border-color:none;")
        self.nepochs = QLineEdit(self.train_page)
        self.nepochs.setObjectName(u"nepochs")
        self.nepochs.setGeometry(QRect(140, 225, 61, 20))



        self.open_directory_rename_btn = QToolButton(self.home_page)
        self.open_directory_rename_btn.setObjectName(u"open_directory_rename_btn")
        self.open_directory_rename_btn.setGeometry(QRect(560, 50, 51, 51))
        self.open_directory_rename_btn.setStyleSheet(u"background-color: none;\n"
                                                 "border-color: none;\n"
                                                 "")
        self.open_directory_rename_btn.setIcon(icon12)
        self.open_directory_rename_btn.setIconSize(QSize(30, 30))
        self.open_directory_rename = QLabel(self.home_page)
        self.open_directory_rename.setObjectName((u"open_directory_rename"))
        self.open_directory_rename.setGeometry(QRect(600, 60, 131, 31))
        self.open_directory_rename.setFont(font)
        self.open_directory_rename.setStyleSheet((u"background-color: none;\n"
                                                           "border-color:none;"))
        self.rename_files_btn = QToolButton(self.home_page)
        self.rename_files_btn.setObjectName((u"rename_files_btn"))
        self.rename_files_btn.setGeometry(QRect(580, 110, 131, 41))
        self.rename_files_btn.setFont(font)
        self.rename_files_btn.setStyleSheet((u""))

        self.lb_train = QLabel(self.train_page)
        self.lb_train.setObjectName(u"lb_train")
        self.lb_train.setGeometry(QRect(70, 220, 51, 31))
        self.lb_train.setFont(font)
        self.lb_train.setStyleSheet(u"background-color: none;\n"
                                    "border-color:none;")
        self.train_btn_2 = QToolButton(self.train_page)
        self.train_btn_2.setObjectName(u"train_btn_2")
        self.train_btn_2.setGeometry(QRect(20, 210, 51, 51))
        self.train_btn_2.setStyleSheet(u"background-color: none;\n"
                                       "border-color: none;\n"
                                       "")
        icon14 = QIcon()
        icon14.addFile(u":/Icons/Icons/train_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.train_btn_2.setIcon(icon14)
        self.train_btn_2.setIconSize(QSize(30, 30))
        self.lb_clear = QLabel(self.train_page)
        self.lb_clear.setObjectName(u"lb_clear")
        self.lb_clear.setGeometry(QRect(680, 570, 51, 31))
        self.lb_clear.setFont(font)
        self.lb_clear.setStyleSheet(u"background-color: none;\n"
                                    "border-color:none;")
        self.clear_btn = QToolButton(self.train_page)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(20, 230, 51, 51))
        self.clear_btn.setStyleSheet(u"background-color: none;\n"
                                     "border-color: none;\n"
                                     "")
        icon15 = QIcon()
        icon15.addFile(u":/Icons/Icons/broom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_btn.setIcon(icon15)
        self.clear_btn.setIconSize(QSize(30, 30))
        self.fm_train_results = QScrollArea(self.train_page)
        self.fm_train_results.setObjectName(u"fm_train_results")
        self.fm_train_results.setGeometry(QRect(30, 500, 591, 331))
        self.fm_train_results.setWidgetResizable(True)
        self.fm_train_results_area=QWidget()
        self.fm_train_results_area.setObjectName(u"fm_train_results_area")
        self.fm_train_results.setGeometry(QRect(30, 500, 450, 300))
        self.vertical_layout_train = QVBoxLayout(self.fm_train_results_area)
        self.vertical_layout_train.setObjectName(u"vertical_layout_train")
        self.horizontal_layout_train = QHBoxLayout(self.fm_train_results_area)
        self.horizontal_layout_train.setObjectName(u"horizontal_layout_train")
        self.fm_train_results.setWidget(self.fm_train_results_area)

        #self.fm_train_results.setFrameShape(QFrame.StyledPanel)
        #self.fm_train_results.setFrameShadow(QFrame.Raised)
        self.trade_page_stacked_widget.addWidget(self.train_page)
        self.segment_page = QWidget()
        self.segment_page.setObjectName(u"segment_page")
        self.lb_title_train_from_start_3 = QLabel(self.segment_page)
        self.lb_title_train_from_start_3.setObjectName(u"lb_title_train_from_start_3")
        self.lb_title_train_from_start_3.setGeometry(QRect(10, 0, 231, 42))
        self.lb_title_train_from_start_3.setFont(font5)
        self.lb_title_train_from_start_3.setStyleSheet(u"background-color:none;\n"
                                                       "color: rgb(0, 0, 0);\n"
                                                       "border:none\n"
                                                       "\n"
                                                       "")
        self.open_model_seg_btn = QToolButton(self.segment_page)
        self.open_model_seg_btn.setObjectName(u"open_model_seg_btn")
        self.open_model_seg_btn.setGeometry(QRect(300, 60, 51, 51))
        self.open_model_seg_btn.setStyleSheet(u"background-color: none;\n"
                                              "border-color: none;\n"
                                              "")
        self.open_model_seg_btn.setIcon(icon13)
        self.open_model_seg_btn.setIconSize(QSize(30, 30))
        self.lb_clear_seg = QLabel(self.segment_page)
        self.lb_clear_seg.setObjectName(u"lb_clear_seg")
        self.lb_clear_seg.setGeometry(QRect(680, 580, 51, 31))
        self.lb_clear_seg.setFont(font)
        self.lb_clear_seg.setStyleSheet(u"background-color: none;\n"
                                        "border-color:none;")
        self.lb_open_dir_with_imgs_seg = QLabel(self.segment_page)
        self.lb_open_dir_with_imgs_seg.setObjectName(u"lb_open_dir_with_imgs_seg")
        self.lb_open_dir_with_imgs_seg.setGeometry(QRect(60, 70, 231, 31))
        self.lb_open_dir_with_imgs_seg.setFont(font)
        self.lb_open_dir_with_imgs_seg.setStyleSheet(u"background-color: none;\n"
                                                     "border-color:none;")
        self.clear_seg_btn = QToolButton(self.segment_page)
        self.clear_seg_btn.setObjectName(u"clear_seg_btn")
        self.clear_seg_btn.setGeometry(QRect(630, 570, 51, 51))
        self.clear_seg_btn.setStyleSheet(u"background-color: none;\n"
                                         "border-color: none;\n"
                                         "")
        self.clear_seg_btn.setIcon(icon15)
        self.clear_seg_btn.setIconSize(QSize(30, 30))
        self.open_dir_with_imgs_seg_btn = QToolButton(self.segment_page)
        self.open_dir_with_imgs_seg_btn.setObjectName(u"open_dir_with_imgs_seg_btn")
        self.open_dir_with_imgs_seg_btn.setGeometry(QRect(20, 60, 51, 51))
        self.open_dir_with_imgs_seg_btn.setStyleSheet(u"background-color: none;\n"
                                                      "border-color: none;\n"
                                                      "")
        self.open_dir_with_imgs_seg_btn.setIcon(icon12)
        self.open_dir_with_imgs_seg_btn.setIconSize(QSize(30, 30))
        self.lb_open_model_seg = QLabel(self.segment_page)
        self.lb_open_model_seg.setObjectName(u"lb_open_model_seg")
        self.lb_open_model_seg.setGeometry(QRect(340, 70, 111, 31))
        self.lb_open_model_seg.setFont(font)
        self.lb_open_model_seg.setStyleSheet(u"background-color: none;\n"
                                             "border-color:none;")
        self.fm_image_result = QLabel(self.segment_page)
        self.fm_image_result.setObjectName(u"fm_image_result")
        self.fm_image_result.setGeometry(QRect(460, 110, 261, 391))
        #self.fm_image_result.setFrameShape(QLabel.StyledPanel)
        #self.fm_image_result.setFrameShadow(QLabel.Raised)
        self.fm_image_overlay = QLabel(self.segment_page)
        self.fm_image_overlay.setObjectName(u"fm_image_overlay")
        self.fm_image_overlay.setGeometry(QRect(20, 110, 391, 391))
        #self.fm_image_overlay.setFrameShape(QFrame.StyledPanel)
        #self.fm_image_overlay.setFrameShadow(QFrame.Raised)
        self.lb_seg = QLabel(self.segment_page)
        self.lb_seg.setObjectName(u"lb_seg")
        self.lb_seg.setGeometry(QRect(510, 70, 81, 31))
        self.lb_seg.setFont(font)
        self.lb_seg.setStyleSheet(u"background-color: none;\n"
                                  "border-color:none;")
        self.seg_btn = QToolButton(self.segment_page)
        self.seg_btn.setObjectName(u"seg_btn")
        self.seg_btn.setGeometry(QRect(470, 60, 51, 51))
        self.seg_btn.setStyleSheet(u"background-color: none;\n"
                                   "border-color: none;\n"
                                   "")
        icon16 = QIcon()
        icon16.addFile(u":/Icons/Icons/segment_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.seg_btn.setIcon(icon16)
        self.seg_btn.setIconSize(QSize(30, 30))
        self.scrollArea_2 = QScrollArea(self.segment_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(20, 530, 421, 91))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 391, 111))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.lb_results_Seg = QLabel(self.segment_page)
        self.lb_results_Seg.setObjectName(u"lb_results_Seg")
        self.lb_results_Seg.setGeometry(QRect(570, 520, 71, 31))
        self.lb_results_Seg.setFont(font)
        self.lb_results_Seg.setStyleSheet(u"background-color: none;\n"
                                          "border-color:none;")
        self.trade_page_stacked_widget.addWidget(self.segment_page)
        self.measure_page = QWidget()
        self.measure_page.setObjectName(u"measure_page")
        self.lb_title_train_from_start_4 = QLabel(self.measure_page)
        self.lb_title_train_from_start_4.setObjectName(u"lb_title_train_from_start_4")
        self.lb_title_train_from_start_4.setGeometry(QRect(10, 0, 231, 42))
        self.lb_title_train_from_start_4.setFont(font5)
        self.lb_title_train_from_start_4.setStyleSheet(u"background-color:none;\n"
                                                       "color: rgb(0, 0, 0);\n"
                                                       "border:none\n"
                                                       "")
        self.lb_open_dir_with_predicts = QLabel(self.measure_page)
        self.lb_open_dir_with_predicts.setObjectName(u"lb_open_dir_with_predicts")
        self.lb_open_dir_with_predicts.setGeometry(QRect(40, 50, 251, 31))
        self.lb_open_dir_with_predicts.setFont(font)
        self.lb_open_dir_with_predicts.setStyleSheet(u"background-color: none;\n"
                                                     "border-color:none;")

        self.scale_train = QLabel(self.measure_page)
        self.scale_train.setObjectName(u"scale_train")
        self.scale_train.setGeometry(QRect(140, 225, 61, 20))
        self.scale_train.setFont(font)
        self.scale_train.setStyleSheet(u"background-color: none;\n"
                                       "border-color:none;")

        self.lb_or = QLabel(self.measure_page)
        self.lb_or.setObjectName(u"lb_or")
        self.lb_or.setGeometry(QRect(140, 225, 61, 20))
        self.lb_or.setFont(font)
        self.lb_or.setStyleSheet(u"background-color: none;\n"
                                       "border-color:none;")


        self.scale_train_line = QLineEdit(self.measure_page)
        self.scale_train_line.setObjectName(u"scale_train_line")
        self.scale_train_line.setGeometry(QRect(140, 225, 61, 20))

        font_px_mm = QFont()
        font_px_mm.setFamilies([u"Times New Roman"])
        font_px_mm.setPointSize(12)

        self.px_mm = QLabel(self.measure_page)
        self.px_mm.setObjectName(u"px_mm")
        self.px_mm.setGeometry(QRect(140, 225, 61, 20))
        self.px_mm.setFont(font_px_mm)
        self.px_mm.setStyleSheet(u"background-color: none;\n"
                                 "border-color:none;")

        self.open_dir_with_predicts_btn = QToolButton(self.measure_page)
        self.open_dir_with_predicts_btn.setObjectName(u"open_dir_with_predicts_btn")
        self.open_dir_with_predicts_btn.setGeometry(QRect(0, 40, 51, 51))
        self.open_dir_with_predicts_btn.setStyleSheet(u"background-color: none;\n"
                                                      "border-color: none;\n"
                                                      "")
        self.open_dir_with_predicts_btn.setIcon(icon12)
        self.open_dir_with_predicts_btn.setIconSize(QSize(30, 30))

        self.lb_filters = QLabel(self.measure_page)
        self.lb_filters.setObjectName(u"lb_filters")
        self.lb_filters.setGeometry(QRect(90, 90, 61, 31))
        self.lb_filters.setFont(font)
        self.lb_filters.setStyleSheet(u"background-color: none;\n"
                                      "border-color:none;")
        self.lb_edges = QLabel(self.measure_page)
        self.lb_edges.setObjectName(u"lb_edges")
        self.lb_edges.setGeometry(QRect(10, 130, 51, 31))
        self.lb_edges.setFont(font)
        self.lb_edges.setStyleSheet(u"background-color: none;\n"
                                    "border-color:none;")
        self.lb_cut = QLabel(self.measure_page)
        self.lb_cut.setObjectName(u"lb_cut")
        self.lb_cut.setGeometry(QRect(10, 170, 41, 31))
        self.lb_cut.setFont(font)
        self.lb_cut.setStyleSheet(u"background-color: none;\n"
                                  "border-color:none;")
        self.set_values_filters_btn = QPushButton(self.measure_page)
        self.set_values_filters_btn.setObjectName(u"set_values_filters_btn")
        self.set_values_filters_btn.setGeometry(QRect(90, 210, 75, 23))

        self.lb_image_distance = QLabel(self.measure_page)
        self.lb_image_distance.setObjectName(u"lb_image_distance")
        self.lb_image_distance.setGeometry(QRect(10, 280, 141, 31))
        self.lb_image_distance.setFont(font)
        self.lb_image_distance.setStyleSheet(u"background-color: none;\n"
                                             "border-color:none;")

        self.lb_unit_image_distance = QLabel(self.measure_page)
        self.lb_unit_image_distance.setObjectName(u"lb_unit_image_distance")
        self.lb_unit_image_distance.setGeometry(QRect(250, 275, 141, 31))
        self.lb_unit_image_distance.setFont(font)
        self.lb_unit_image_distance.setStyleSheet(u"background-color: none;\n"
                                                  "border-color:none;")

        self.lb_focal_lenght = QLabel(self.measure_page)
        self.lb_focal_lenght.setObjectName(u"lb_focal_lenght")
        self.lb_focal_lenght.setGeometry(QRect(10, 320, 111, 31))
        self.lb_focal_lenght.setFont(font)
        self.lb_focal_lenght.setStyleSheet(u"background-color: none;\n"
                                           "border-color:none;")

        self.lb_focal_lenght_unit = QLabel(self.measure_page)
        self.lb_focal_lenght_unit.setObjectName(u"lb_focal_lenght_unit")
        self.lb_focal_lenght_unit.setGeometry(QRect(250, 315, 141, 31))
        self.lb_focal_lenght_unit.setFont(font)
        self.lb_focal_lenght_unit.setStyleSheet(u"background-color: none;\n"
                                                  "border-color:none;")

        self.lb_sensor_height = QLabel(self.measure_page)
        self.lb_sensor_height.setObjectName(u"lb_sensor_height")
        self.lb_sensor_height.setGeometry(QRect(10, 360, 121, 31))
        self.lb_sensor_height.setFont(font)
        self.lb_sensor_height.setStyleSheet(u"background-color: none;\n"
                                            "border-color:none;")

        self.lb_sensor_height_unit = QLabel(self.measure_page)
        self.lb_sensor_height_unit.setObjectName(u"lb_sensor_height_unit")
        self.lb_sensor_height_unit.setGeometry(QRect(250, 355, 121, 31))
        self.lb_sensor_height_unit.setFont(font)
        self.lb_sensor_height_unit.setStyleSheet(u"background-color: none;\n"
                                            "border-color:none;")

        self.lb_pixel_height = QLabel(self.measure_page)
        self.lb_pixel_height.setObjectName(u"lb_pixel_height")
        self.lb_pixel_height.setGeometry(QRect(10, 480, 111, 31))
        self.lb_pixel_height.setFont(font)
        self.lb_pixel_height.setStyleSheet(u"background-color: none;\n"
                                           "border-color:none;")

        self.lb_pixel_height_unit = QLabel(self.measure_page)
        self.lb_pixel_height_unit.setObjectName(u"lb_pixel_height_unit")
        self.lb_pixel_height_unit.setGeometry(QRect(250, 475, 111, 31))
        self.lb_pixel_height_unit.setFont(font)
        self.lb_pixel_height_unit.setStyleSheet(u"background-color: none;\n"
                                           "border-color:none;")

        self.lb_pixel_width = QLabel(self.measure_page)
        self.lb_pixel_width.setObjectName(u"lb_pixel_width")
        self.lb_pixel_width.setGeometry(QRect(10, 440, 101, 31))
        self.lb_pixel_width.setFont(font)
        self.lb_pixel_width.setStyleSheet(u"background-color: none;\n"
                                          "border-color:none;")

        self.lb_pixel_width_unit = QLabel(self.measure_page)
        self.lb_pixel_width_unit.setObjectName(u"lb_pixel_width_unit")
        self.lb_pixel_width_unit.setGeometry(QRect(250, 435, 101, 31))
        self.lb_pixel_width_unit.setFont(font)
        self.lb_pixel_width_unit.setStyleSheet(u"background-color: none;\n"
                                          "border-color:none;")

        self.lb_sensor_width = QLabel(self.measure_page)
        self.lb_sensor_width.setObjectName(u"lb_sensor_width")
        self.lb_sensor_width.setGeometry(QRect(10, 400, 121, 31))
        self.lb_sensor_width.setFont(font)
        self.lb_sensor_width.setStyleSheet(u"background-color: none;\n"
                                           "border-color:none;")

        self.lb_sensor_width_unit = QLabel(self.measure_page)
        self.lb_sensor_width_unit.setObjectName(u"lb_sensor_width_unit")
        self.lb_sensor_width_unit.setGeometry(QRect(250, 395, 121, 31))
        self.lb_sensor_width_unit.setFont(font)
        self.lb_sensor_width_unit.setStyleSheet(u"background-color: none;\n"
                                           "border-color:none;")

        self.set_values_parameters_btn = QPushButton(self.measure_page)
        self.set_values_parameters_btn.setObjectName(u"set_values_parameters_btn")
        self.set_values_parameters_btn.setGeometry(QRect(100, 520, 75, 23))
        self.lb_measure = QLabel(self.measure_page)
        self.lb_measure.setObjectName(u"lb_measure")
        self.lb_measure.setGeometry(QRect(50, 570, 81, 31))
        self.lb_measure.setFont(font)
        self.lb_measure.setStyleSheet(u"background-color: none;\n"
                                      "border-color:none;")
        self.lb_clear_measure = QLabel(self.measure_page)
        self.lb_clear_measure.setObjectName(u"lb_clear_measure")
        self.lb_clear_measure.setGeometry(QRect(170, 570, 51, 31))
        self.lb_clear_measure.setFont(font)
        self.lb_clear_measure.setStyleSheet(u"background-color: none;\n"
                                            "border-color:none;")
        self.clear_measure_btn = QToolButton(self.measure_page)
        self.clear_measure_btn.setObjectName(u"clear_measure_btn")
        self.clear_measure_btn.setGeometry(QRect(140, 560, 41, 41))
        self.clear_measure_btn.setStyleSheet(u"background-color: none;\n"
                                             "border-color: none;\n"
                                             "")
        self.clear_measure_btn.setIcon(icon15)
        self.clear_measure_btn.setIconSize(QSize(30, 30))
        self.fm_image_measure = QLabel(self.measure_page)
        self.fm_image_measure.setObjectName(u"fm_image_measure")
        self.fm_image_measure.setGeometry(QRect(310, 10, 301, 301))
        #self.fm_image_measure.setFrameShape(QFrame.StyledPanel)
        #self.fm_image_measure.setFrameShadow(QFrame.Raised)
        self.fm_graph_result_measure = QLabel(self.measure_page)
        self.fm_graph_result_measure.setObjectName(u"fm_graph_result_measure")
        self.fm_graph_result_measure.setGeometry(QRect(270, 320, 461, 281))
        #self.fm_graph_result_measure.setFrameShape(QFrame.StyledPanel)
        #self.fm_graph_result_measure.setFrameShadow(QFrame.Raised)
        self.line_image_distance = QLineEdit(self.measure_page)
        self.line_image_distance.setObjectName(u"line_image_distance")
        self.line_image_distance.setGeometry(QRect(140, 280, 113, 20))
        self.line_focal_lenght = QLineEdit(self.measure_page)
        self.line_focal_lenght.setObjectName(u"line_focal_lenght")
        self.line_focal_lenght.setGeometry(QRect(140, 320, 113, 21))
        self.line_sensor_height = QLineEdit(self.measure_page)
        self.line_sensor_height.setObjectName(u"line_sensor_height")
        self.line_sensor_height.setGeometry(QRect(140, 360, 113, 21))
        self.line_sensor_width = QLineEdit(self.measure_page)
        self.line_sensor_width.setObjectName(u"line_sensor_width")
        self.line_sensor_width.setGeometry(QRect(140, 400, 113, 21))
        self.line_pixel_width = QLineEdit(self.measure_page)
        self.line_pixel_width.setObjectName(u"line_pixel_width")
        self.line_pixel_width.setGeometry(QRect(140, 440, 113, 21))
        self.line_pixel_height = QLineEdit(self.measure_page)
        self.line_pixel_height.setObjectName(u"line_pixel_height")
        self.line_pixel_height.setGeometry(QRect(140, 480, 113, 21))
        self.line_edge = QLineEdit(self.measure_page)
        self.line_edge.setObjectName(u"line_edge")
        self.line_edge.setGeometry(QRect(70, 130, 113, 20))
        self.line_cut = QLineEdit(self.measure_page)
        self.line_cut.setObjectName(u"line_cut")
        self.line_cut.setGeometry(QRect(70, 170, 113, 20))
        self.scrollArea_3 = QScrollArea(self.measure_page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(619, 9, 121, 301))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 115, 295))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)
        self.measure_btn_2 = QToolButton(self.measure_page)
        self.measure_btn_2.setObjectName(u"measure_btn_2")
        self.measure_btn_2.setGeometry(QRect(10, 560, 51, 51))
        self.measure_btn_2.setStyleSheet(u"background-color: none;\n"
                                         "border-color: none;\n"
                                         "")
        icon17 = QIcon()
        icon17.addFile(u":/Icons/Icons/measure_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.measure_btn_2.setIcon(icon17)
        self.measure_btn_2.setIconSize(QSize(30, 30))
        self.lb_parameters = QLabel(self.measure_page)
        self.lb_parameters.setObjectName(u"lb_parameters")
        self.lb_parameters.setGeometry(QRect(20, 245, 91, 31))
        self.lb_parameters.setFont(font)
        self.lb_parameters.setStyleSheet(u"background-color: none;\n"
                                         "border-color:none;")
        self.clear_values_filters_btn = QPushButton(self.measure_page)
        self.clear_values_filters_btn.setObjectName(u"clear_values_filters_btn")
        self.clear_values_filters_btn.setGeometry(QRect(160, 210, 75, 23))
        self.clear_values_parameters_btn = QPushButton(self.measure_page)
        self.clear_values_parameters_btn.setObjectName(u"clear_values_parameters_btn")
        self.clear_values_parameters_btn.setGeometry(QRect(150, 520, 101, 23))
        self.trade_page_stacked_widget.addWidget(self.measure_page)
        self.velocity_page = QWidget()
        self.velocity_page.setObjectName(u"page")
        self.icon_sphere = QIcon()
        self.icon_sphere.addFile(u":/Imgs/Icons/sphere.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.icon_sphere.addFile(u":/Imgs/Icons/sphere.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.icon_sphere.addFile(u":/Imgs/Icons/sphere_enabled.png", QSize(), QIcon.Active, QIcon.On)
        #self.icon_sphere.addFile(u":/Imgs/Icons/sphere_enabled.png", QSize(), QIcon.Selected, QIcon.On)
        self.lb_title_train_from_start_5 = QLabel(self.velocity_page)
        self.lb_title_train_from_start_5.setObjectName(u"lb_title_train_from_start_5")
        self.lb_title_train_from_start_5.setGeometry(QRect(10, 0, 231, 42))
        self.lb_title_train_from_start_5.setFont(font5)
        self.lb_title_train_from_start_5.setStyleSheet(u"background-color:none;\n"
                                                       "color: rgb(0, 0, 0);\n"
                                                       "border:none\n"
                                                       "")
        self.lb_coordinates_points = QLabel(self.velocity_page)
        self.lb_coordinates_points.setObjectName(u"lb_coordinates_points")
        self.lb_coordinates_points.setGeometry(QRect(10, 70, 161, 31))
        font_velocity = QFont()
        font_velocity.setFamilies([u"Times New Roman"])
        font_velocity.setPointSize(13)
        self.lb_coordinates_points.setFont(font_velocity)
        self.lb_coordinates_points.setStyleSheet(u"\n"
                                                 "background-color: none;\n"
                                                 "border-color:none;")
        self.lb_movie = QWidget(self.velocity_page)
        self.lb_movie.setObjectName(u"lb_movie")
        self.lb_movie.setGeometry(QRect(280, 100, 441, 350))
        self.lb_movie.setStyleSheet(u"\n"
                                    "background-color: none;\n"
                                    "")


        self.lb_open_movie = QLabel(self.velocity_page)
        self.lb_open_movie.setObjectName(u"lb_open_movie")
        self.lb_open_movie.setGeometry(QRect(310, 50, 111, 31))
        self.lb_open_movie.setFont(font)
        self.lb_open_movie.setStyleSheet(u"background-color: none;\n"
                                         "border-color:none;")
        self.open_movie = QToolButton(self.velocity_page)
        self.open_movie.setObjectName(u"open_movie")
        self.open_movie.setGeometry(QRect(270, 40, 51, 51))
        self.open_movie.setStyleSheet(u"background-color: none;\n"
                                      "border-color: none;\n"
                                      "")
        self.open_movie.setIcon(icon12)
        self.open_movie.setIconSize(QSize(30, 30))
        self.add_point = QPushButton(self.velocity_page)
        self.add_point.setObjectName(u"add_point")
        self.add_point.setGeometry(QRect(10, 450, 81, 21))
        font8 = QFont()
        font8.setFamilies([u"Times New Roman"])
        font8.setPointSize(11)
        self.add_point.setFont(font8)
        self.clear_point = QPushButton(self.velocity_page)
        self.clear_point.setObjectName(u"clear_point")
        self.clear_point.setGeometry(QRect(170, 450, 81, 21))
        self.clear_point.setFont(font8)

        self.next_camera=QPushButton(self.velocity_page)
        self.next_camera.setObjectName(u"next_camera")
        self.next_camera.setGeometry(QRect(470, 455, 100, 20))
        self.next_camera.setFont(font8)

        self.previous_camera=QPushButton(self.velocity_page)
        self.previous_camera.setObjectName(u"previous_camera")
        self.previous_camera.setGeometry(QRect(340, 455, 120, 20))
        self.previous_camera.setFont(font8)

        self.set_coordinates = QPushButton(self.velocity_page)
        self.set_coordinates.setObjectName(u"set_coordinates")
        self.set_coordinates.setGeometry(QRect(255, 495, 51, 21))
        self.set_coordinates.setFont(font8)
        self.table_coordinates_point = QTableWidget(self.velocity_page)
        if (self.table_coordinates_point.columnCount() < 4):
                self.table_coordinates_point.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_coordinates_point.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_coordinates_point.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_coordinates_point.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_coordinates_point.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_coordinates_point.setObjectName(u"table_coordinates_point")
        self.table_coordinates_point.setGeometry(QRect(10, 100, 241, 341))
        self.table_coordinates_point.setStyleSheet(u"background-color: none")
        self.scrollArea_4_objects = QScrollArea(self.velocity_page)
        self.scrollArea_4_objects.setObjectName(u"scrollArea_4_objects")
        self.scrollArea_4_objects.setGeometry(QRect(280, 485, 331, 71))
        self.scrollArea_4_objects.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6_objects = QWidget()
        self.scrollAreaWidgetContents_6_objects.setObjectName(u"scrollAreaWidgetContents_6_objects")
        self.scrollAreaWidgetContents_6_objects.setGeometry(QRect(0, 0, 435, 85))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_6_objects)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea_4_objects.setWidget(self.scrollAreaWidgetContents_6_objects)
        self.identify_check_box = QCheckBox(self.velocity_page)
        self.identify_check_box.setObjectName(u"identify_check_box")
        self.identify_check_box.setStyleSheet(u"background-color: none;\n"
                                       "border-color: none;")
        self.identify_check_box.setGeometry(QRect(320, 530, 70, 17))
        self.list_models=QListWidget(self.velocity_page)
        self.list_models.setGeometry(QRect(725,453,55,100))
        self.list_models.setObjectName(u"list_models")
        self.update_models=QToolButton(self.velocity_page)
        self.update_models.setObjectName(u"update_models")
        self.update_models.setGeometry(QRect(350, 500, 30, 30))
        self.update_models.setStyleSheet(u"background-color: none;\n"
                       "border-color: none;")
        self.icon_update_models = QIcon()
        self.icon_update_models.addFile(u":/Icons/Icons/update.png", QSize(30,30), QIcon.Normal, QIcon.Off)
        self.update_models.setIcon(self.icon_update_models)
        self.update_models.setIconSize(QSize(30,30))

        self.delete_models = QToolButton(self.velocity_page)
        self.delete_models.setObjectName(u"update_models")
        self.delete_models.setGeometry(QRect(350, 500, 20, 20))
        self.delete_models.setStyleSheet(u"background-color: none;\n"
                                         "border-color: none;")

        self.icon_delete_models = QIcon()
        self.icon_delete_models.addFile(u":/Icons/Icons/cross (1).png", QSize(30, 30), QIcon.Normal, QIcon.Off)
        self.delete_models.setIcon(self.icon_delete_models)
        self.delete_models.setIconSize(QSize(20, 20))

        self.camera = QToolButton(self.velocity_page)
        self.camera.setObjectName(u"camera")
        self.camera.setGeometry(QRect(460, 60, 61, 41))
        self.camera.setStyleSheet(u"background-color: none;\n"
                                         "border-color: none;")

        self.camera_icon = QIcon()
        self.camera_icon.addFile(u":/Imgs/Icons/camera.png", QSize(30, 30), QIcon.Normal, QIcon.Off)
        self.camera.setIcon(self.camera_icon)
        self.camera.setIconSize(QSize(20, 20))

        self.list_camera=QListWidget(self.velocity_page)
        self.list_camera.setObjectName("list_camera")
        self.list_camera.setGeometry(QRect(280, 235,55,70))

        self.line_camera=QLineEdit(self.velocity_page)
        self.line_camera.setObjectName("line_camera")
        self.line_camera.setGeometry(QRect(280, 310, 55, 20))

        self.add_camera = QPushButton(self.velocity_page)
        self.add_camera.setObjectName(u"add_camera")
        self.add_camera.setGeometry(QRect(240, 310, 55, 20))
        self.add_camera.setStyleSheet(u"background-color: none;\n"
                                  "border-color: none;")

        self.add_camera_icon = QIcon()
        self.add_camera_icon.addFile(u":/Imgs/Icons/addphoto.png", QSize(30, 30), QIcon.Normal, QIcon.Off)
        self.add_camera.setIcon(self.add_camera_icon)
        self.add_camera.setIconSize(QSize(20, 20))

        self.rd_btn_sfiv = QRadioButton(self.velocity_page)
        self.rd_btn_sfiv.setObjectName(u"rd_btn_sfiv")
        self.rd_btn_sfiv.setGeometry(QRect(20, 500, 82, 31))
        self.rd_btn_sfiv.setFont(font)
        self.rd_btn_sfiv.setStyleSheet(u"background-color: none;\n"
                                       "border-color: none;")

        self.rd_btn_direct = QRadioButton(self.velocity_page)
        self.rd_btn_direct.setObjectName(u"rd_btn_direct")
        self.rd_btn_direct.setGeometry(QRect(50, 500, 82, 31))
        self.rd_btn_direct.setFont(font)
        self.rd_btn_direct.setStyleSheet(u"background-color: none;\n"
                                       "border-color: none;")

        self.rd_btn_ignored = QRadioButton(self.velocity_page)
        self.rd_btn_ignored.setObjectName(u"rd_btn_ignored")
        self.rd_btn_ignored.setGeometry(QRect(20, 500, 82, 31))
        self.rd_btn_ignored.setFont(font)
        self.rd_btn_ignored.setStyleSheet(u"background-color: none;\n"
                                       "border-color: none;")

        self.rd_btn_keep = QRadioButton(self.velocity_page)
        self.rd_btn_keep.setObjectName(u"rd_btn_keep")
        self.rd_btn_keep.setGeometry(QRect(20, 500, 82, 31))
        self.rd_btn_keep.setFont(font)
        self.rd_btn_keep.setStyleSheet(u"background-color: none;\n"
                                          "border-color: none;")

        self.rd_btn_keep_expand = QRadioButton(self.velocity_page)
        self.rd_btn_keep_expand.setObjectName(u"rd_btn_keep_expand")
        self.rd_btn_keep_expand.setGeometry(QRect(20, 500, 82, 31))
        self.rd_btn_keep_expand.setFont(font)
        self.rd_btn_keep_expand.setStyleSheet(u"background-color: none;\n"
                                       "border-color: none;")

        self.lb_method = QLabel(self.velocity_page)
        self.lb_method.setObjectName(u"lb_method")
        self.lb_method.setGeometry(QRect(20, 480, 71, 31))
        self.lb_method.setFont(font_velocity)
        self.lb_method.setStyleSheet(u"\n"
                                     "background-color: none;\n"
                                     "border-color:none;")
        self.btn_stabilization_movie = QToolButton(self.velocity_page)
        self.btn_stabilization_movie.setObjectName(u"btn_stabilization_movie")
        self.btn_stabilization_movie.setGeometry(QRect(530, 20, 181, 31))
        self.btn_stabilization_movie.setFont(font)
        self.btn_estimate_velocity = QToolButton(self.velocity_page)
        self.btn_estimate_velocity.setObjectName(u"btn_estimate_velocity")
        self.btn_estimate_velocity.setGeometry(QRect(530, 60, 181, 31))
        self.btn_estimate_velocity.setFont(font)
        self.lb_objects = QLabel(self.velocity_page)
        self.lb_objects.setObjectName(u"lb_objects")
        self.lb_objects.setGeometry(QRect(200, 510, 71, 31))
        self.lb_objects.setFont(font_velocity)
        self.lb_objects.setStyleSheet(u"\n"
                                      "background-color: none;\n"
                                      "border-color:none;")

        font_direct = QFont()
        font_direct.setFamilies([u"Times New Roman"])
        font_direct.setPointSize(12)

        font8 = QFont()
        font8.setFamilies([u"Times New Roman"])
        font8.setPointSize(11)



        self.x_coordinate = QLineEdit(self.velocity_page)
        self.x_coordinate.setObjectName(u"x_coordinate")
        self.x_coordinate.setGeometry(QRect(50, 480, 61, 20))
        self.y_coordinate = QLineEdit(self.velocity_page)
        self.y_coordinate.setObjectName(u"y_coordinate")
        self.y_coordinate.setGeometry(QRect(150, 480, 61, 20))
        self.x_label = QLabel(self.velocity_page)
        self.x_label.setObjectName(u"x_label")
        self.x_label.setGeometry(QRect(30, 480, 21, 16))
        self.x_label.setStyleSheet(u"\n"
                                   "background-color: none;\n"
                                   "border-color:none;")
        self.x2_label = QLabel(self.velocity_page)
        self.x2_label.setObjectName(u"x2_label")
        self.x2_label.setGeometry(QRect(30, 480, 21, 16))
        self.x2_label.setStyleSheet(u"\n"
                                   "background-color: none;\n"
                                   "border-color:none;")
        self.y_label = QLabel(self.velocity_page)
        self.y_label.setObjectName(u"y_label")
        self.y_label.setGeometry(QRect(130, 480, 21, 20))
        self.y_label.setStyleSheet(u"\n"
                                   "background-color: none;\n"
                                   "border-color:none;")
        self.y2_label = QLabel(self.velocity_page)
        self.y2_label.setObjectName(u"y2_label")
        self.y2_label.setGeometry(QRect(130, 480, 21, 20))
        self.y2_label.setStyleSheet(u"\n"
                                   "background-color: none;\n"
                                   "border-color:none;")
        self.Ok_method = QPushButton(self.velocity_page)
        self.Ok_method.setObjectName(u"Ok_method")
        self.Ok_method.setGeometry(QRect(190, 530, 31, 21))
        self.Ok_method.setFont(font8)
        self.lb_time_actual = QLabel(self.velocity_page)
        self.lb_time_actual.setObjectName(u"lb_time_actual")
        self.lb_time_actual.setGeometry(QRect(280, 60, 61, 41))
        sizePolicy1.setHeightForWidth(self.lb_time_actual.sizePolicy().hasHeightForWidth())
        self.lb_time_actual.setSizePolicy(sizePolicy1)
        font9 = QFont()
        font9.setPointSize(10)
        self.lb_time_actual.setFont(font9)
        self.lb_time_actual.setStyleSheet(u"border-color: none;\n"
                                          "background-color: none;")
        self.lb_total_time = QLabel(self.velocity_page)
        self.lb_total_time.setObjectName(u"lb_total_time")
        self.lb_total_time.setGeometry(QRect(460, 60, 61, 41))
        sizePolicy1.setHeightForWidth(self.lb_total_time.sizePolicy().hasHeightForWidth())
        self.lb_total_time.setSizePolicy(sizePolicy1)
        self.lb_total_time.setFont(font9)
        self.lb_total_time.setStyleSheet(u"border-color: none;\n"
                                         "background-color: none;")
        self.slider_time = QSlider(self.velocity_page)
        self.slider_time.setObjectName(u"slider_time")
        self.slider_time.setGeometry(QRect(350, 70, 111, 22))
        self.slider_time.setStyleSheet(u"border-color: none;\n"
                                       "background-color: none;")
        self.slider_time.setOrientation(Qt.Horizontal)
        self.volume_slider = QSlider(self.velocity_page)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setGeometry(QRect(270, 320, 22, 91))
        self.volume_slider.setStyleSheet(u"border-color: none;\n"
                                         "background-color: none;")
        self.volume_slider.setOrientation(Qt.Vertical)
        self.sound = QPushButton(self.velocity_page)
        self.sound.setObjectName(u"sound")
        self.sound.setGeometry(QRect(270, 420, 21, 23))
        self.sound.setStyleSheet(u"border-color: none;\n"
                                         "background-color: none;")
        icon18 = QIcon()
        icon18.addFile(u":/Icons/Icons/volume.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sound.setIcon(icon18)
        self.mute_sound = QPushButton(self.velocity_page)
        self.mute_sound.setObjectName(u"mute_sound")
        self.mute_sound.setGeometry(QRect(270, 420, 21, 23))
        self.mute_sound.setStyleSheet(u"border-color: none;\n"
                                 "background-color: none;")
        icon24 = QIcon()
        icon24.addFile(u":/Icons/Icons/mute.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mute_sound.setIcon(icon24)
        self.stop_button = QPushButton(self.velocity_page)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(270, 150, 21, 23))
        self.stop_button.setStyleSheet(u"border-color: none;\n"
                                       "background-color: none;")
        icon19 = QIcon()
        icon19.addFile(u":/Icons/Icons/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon19)
        self.pause_button = QPushButton(self.velocity_page)
        self.pause_button.setObjectName(u"pause_button")
        self.pause_button.setGeometry(QRect(270, 120, 21, 23))
        self.pause_button.setStyleSheet(u"border-color: none;\n"
                                             "background-color: none;")
        icon20 = QIcon()
        icon20.addFile(u":/Icons/Icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_button.setIcon(icon20)
        self.play_button = QPushButton(self.velocity_page)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(270, 120, 21, 23))
        self.play_button.setStyleSheet(u"border-color: none;\n"
                                             "background-color: none;")
        icon23 = QIcon()
        icon23.addFile(u":/Icons/Icons/play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon23)
        self.back_time_button = QPushButton(self.velocity_page)
        self.back_time_button.setObjectName(u"back_time_button")
        self.back_time_button.setGeometry(QRect(270, 210, 21, 23))
        self.back_time_button.setStyleSheet(u"border-color: none;\n"
                                            "background-color: none;")
        icon21 = QIcon()
        icon21.addFile(u":/Icons/Icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_time_button.setIcon(icon21)
        self.foward_time_button = QPushButton(self.velocity_page)
        self.foward_time_button.setObjectName(u"foward_time_button")
        self.foward_time_button.setGeometry(QRect(270, 180, 21, 23))
        self.foward_time_button.setStyleSheet(u"border-color: none;\n"
                                              "background-color: none;")
        icon22 = QIcon()
        icon22.addFile(u":/Icons/Icons/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.foward_time_button.setIcon(icon22)
        self.trade_page_stacked_widget.addWidget(self.velocity_page)

        self.verticalLayout_7.addWidget(self.trade_page_stacked_widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.horizontalLayout_2.addWidget(self.pages)


        self.verticalLayout.addWidget(self.middle_widget)

        self.progress_indicato_frame = QFrame(self.main_container)
        self.progress_indicato_frame.setObjectName(u"progress_indicato_frame")
        self.progress_indicato_frame.setMaximumSize(QSize(16777215, 16777215))
        self.progress_indicato_frame.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.progress_indicato_frame.setFrameShape(QFrame.StyledPanel)
        self.progress_indicato_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.progress_indicato_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progress_indicator = QCustomProgressIndicator(self.progress_indicato_frame)
        self.progress_indicator.setObjectName(u"progress_indicator")
        sizePolicy1.setHeightForWidth(self.progress_indicator.sizePolicy().hasHeightForWidth())
        self.progress_indicator.setSizePolicy(sizePolicy1)
        self.progress_indicator.setMinimumSize(QSize(0, 50))
        self.progress_indicator.setMaximumSize(QSize(16777215, 16777215))
        self.progress_indicator.setStyleSheet(u"background-color: none;\n"
"border:none;")

        self.verticalLayout_3.addWidget(self.progress_indicator, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.progress_indicato_frame, 0, Qt.AlignHCenter)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMaximumSize(QSize(16777215, 16777215))
        self.footer_frame.setStyleSheet(u"border-color: none;")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.footer_frame)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.widget_insider_footer_with_btns = QCustomSlideMenu(self.main_container)
        self.widget_insider_footer_with_btns.setObjectName(u"widget_insider_footer_with_btns")
        self.widget_insider_footer_with_btns.setMinimumSize(QSize(5, 0))
        self.widget_insider_footer_with_btns.setMaximumSize(QSize(16777215, 16777215))
        self.widget_insider_footer_with_btns.setStyleSheet(u"\n"
"border-color: none;")
        self.horizontalLayout = QHBoxLayout(self.widget_insider_footer_with_btns)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.back_btn = QPushButton(self.widget_insider_footer_with_btns)
        self.back_btn.setObjectName(u"back_btn")
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(17)
        self.back_btn.setFont(font6)
        self.back_btn.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));\n"
"color: rgb(255, 255, 255);")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/Icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon12)
        self.back_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.back_btn, 0, Qt.AlignTop)

        self.cancel_btn = QPushButton(self.widget_insider_footer_with_btns)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setFont(font6)
        self.cancel_btn.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));\n"
"color: rgb(255, 255, 255);")
        icon13 = QIcon()
        icon13.addFile(u":/Icons/Icons/cross (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_btn.setIcon(icon13)
        self.cancel_btn.setIconSize(QSize(35, 30))

        self.horizontalLayout.addWidget(self.cancel_btn, 0, Qt.AlignTop)

        self.next_btn = QPushButton(self.widget_insider_footer_with_btns)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setFont(font6)
        self.next_btn.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));\n"
"color: rgb(255, 255, 255);")
        icon14 = QIcon()
        icon14.addFile(u":/Icons/Icons/next-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon14)
        self.next_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.next_btn, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.widget_insider_footer_with_btns)


        self.verticalLayout_10.addWidget(self.main_container)

        self.exit_container = QCustomSlideMenu(self.main_frame)
        self.exit_container.setObjectName(u"exit_container")

        self.exit_container.setMinimumSize(QSize(363, 383))
        self.exit_container.setMaximumSize(QSize(363, 383))
        self.exit_container.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-width:3px;\n"
"background-color: none;")
        self.main_frame_exit = QFrame(self.exit_container)
        self.main_frame_exit.setObjectName(u"main_frame_exit")
        self.main_frame_exit.setGeometry(QRect(9, 9, 363, 383))
        self.main_frame_exit.setMinimumSize(QSize(363, 383))
        self.main_frame_exit.setMaximumSize(QSize(363, 383))
        self.main_frame_exit.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0852273 rgba(185, 63, 88, 255), stop:0.221591 rgba(156, 34, 68, 255), stop:0.278409 rgba(167, 43, 75, 255), stop:0.386364 rgba(162, 39, 79, 255), stop:0.5 rgba(155, 34, 54, 255), stop:0.653409 rgba(147, 41, 61, 255), stop:0.857955 rgba(147, 30, 41, 255), stop:0.965909 rgba(140, 54, 55, 255));\n"
"border-width:3px;")
        self.main_frame_exit.setFrameShape(QFrame.StyledPanel)
        self.main_frame_exit.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.main_frame_exit)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 248, 22))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"")
        self.yes_exit = QPushButton(self.main_frame_exit)
        self.yes_exit.setObjectName(u"yes_exit")
        self.yes_exit.setGeometry(QRect(20, 190, 151, 51))
        self.yes_exit.setMinimumSize(QSize(151, 51))
        self.yes_exit.setMaximumSize(QSize(151, 51))
        font7 = QFont()
        font7.setFamilies([u"Times New Roman"])
        font7.setPointSize(12)
        self.yes_exit.setFont(font7)
        self.yes_exit.setStyleSheet(u"border:solid black;\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0));\n"
"color:rgb(255, 255, 255);\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.no_exit = QPushButton(self.main_frame_exit)
        self.no_exit.setObjectName(u"no_exit")
        self.no_exit.setGeometry(QRect(190, 190, 151, 51))
        self.no_exit.setMinimumSize(QSize(151, 51))
        self.no_exit.setMaximumSize(QSize(151, 51))
        self.no_exit.setFont(font7)
        self.no_exit.setStyleSheet(u"border:solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0));\n"
"color:rgb(255,255,255);\n"
"border-width:2px;\n"
"border-radius:10px;")

        self.verticalLayout_10.addWidget(self.exit_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 31, 901))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));\n"
"border-radius:5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(1170, 0, 31, 901))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));\n"
"border-radius:5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 1201, 20))
        self.frame_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));\n"
"border-radius:5px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 880, 1201, 20))
        self.frame_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(0, 0, 0, 255), stop:0.352273 rgba(0, 0, 0, 255), stop:0.602273 rgba(156, 34, 68, 255), stop:0.75 rgba(167, 43, 75, 255), stop:0.79 rgba(162, 39, 79, 255), stop:0.86 rgba(155, 34, 54, 255), stop:0.935 rgba(147, 41, 61, 255));\n"
"border-radius:5px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(880, 890, 21, 20))
        self.label_9.setMinimumSize(QSize(21, 20))
        self.label_9.setMaximumSize(QSize(21, 20))
        self.label_9.setStyleSheet(u"\n"
                                   "background-color: none;\n"
                                   "border-color:none;")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(1068, 891, 69, 19))
        font10 = QFont()
        font10.setPointSize(7)
        self.radioButton_2.setFont(font10)
        self.radioButton_2.setStyleSheet(u"background-color: none;\n"
                                         "border-color: none;")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(974, 890, 21, 20))
        self.label_10.setMinimumSize(QSize(21, 20))
        self.label_10.setMaximumSize(QSize(21, 20))
        self.label_10.setStyleSheet(u"\n"
                                    "background-color: none;\n"
                                    "border-color:none;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.trade_page_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
            MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
            self.velocity_btn.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
            self.train_btn.setText(QCoreApplication.translate("MainWindow", u"Train", None))
            self.measure_btn.setText(QCoreApplication.translate("MainWindow", u"Measure", None))
            self.segment_btn.setText(QCoreApplication.translate("MainWindow", u"Segment", None))
            self.adv_btn.setText("")
            self.prev_btn.setText("")
            self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
            self.help_btn.setText("")
            self.exit_btn.setText("")
            self.minimize_btn.setText("")
            self.label.setText(QCoreApplication.translate("MainWindow", u"Are you sure you want to exit?", None))
            self.yes_exit.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
            self.no_exit.setText(QCoreApplication.translate("MainWindow", u"No", None))
            self.lb_image_pg.setText("")
            self.train_tutorial_lb.setText(QCoreApplication.translate("MainWindow", u"   Train Tutorial", None))
            self.segment_tutorial_lb.setText(QCoreApplication.translate("MainWindow", u"  Segment Tutorial", None))
            self.measure_tutorial_lb.setText(QCoreApplication.translate("MainWindow", u"  Measure Tutorial", None))
            self.velocity_tutorial_lb.setText(QCoreApplication.translate("MainWindow", u"  Velocity Tutorial", None))
            self.lb_welcome.setText(QCoreApplication.translate("MainWindow",
                                                               u"<html><head/><body><p>WELCOME TO VISION SED!</p><p><br/></p><p><br/></p></body></html>",
                                                               None))
            self.measure_tutorial_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.segment_tutorial_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.velocity_tutorial_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.train_tutorial_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.start_btn.setText("")
            self.label_2.setText(
                    QCoreApplication.translate("MainWindow", u"Click the start button to initialize the program!",
                                               None))
            self.lb_title_train_from_start.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
            self.lb_title_train_from_start_2.setText(QCoreApplication.translate("MainWindow", u"Train Page", None))
            self.open_dir_with_imgs_mask_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.lb_open_dir_with_imgs_mask.setText(
                    QCoreApplication.translate("MainWindow", u"Open Directory With Images and Masks", None))
            self.open_model_pre_trained_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.lb_open_model_pre_trained.setText(
                    QCoreApplication.translate("MainWindow", u"Open Model Pre-Trained (Optional)", None))
            self.lb_train.setText(QCoreApplication.translate("MainWindow", u"Train", None))
            self.train_btn_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.lb_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
            self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.lb_title_train_from_start_3.setText(QCoreApplication.translate("MainWindow", u"Segment Page", None))
            self.open_directory_rename_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.open_directory_rename.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
            self.rename_files_btn.setText(QCoreApplication.translate("MainWindow", u"Rename Files", None))
            self.open_model_seg_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.lb_clear_seg.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
            self.lb_open_dir_with_imgs_seg.setText(
                    QCoreApplication.translate("MainWindow", u"Open Directory With Images", None))
            self.clear_seg_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.open_dir_with_imgs_seg_btn.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
            self.lb_open_model_seg.setText(QCoreApplication.translate("MainWindow", u"Open Model", None))
            self.lb_seg.setText(QCoreApplication.translate("MainWindow", u"Segment", None))
            self.seg_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.lb_results_Seg.setText(QCoreApplication.translate("MainWindow", u"Results", None))
            self.lb_title_train_from_start_4.setText(QCoreApplication.translate("MainWindow", u"Measure Page", None))
            self.lb_open_dir_with_predicts.setText(
                    QCoreApplication.translate("MainWindow", u"Open Directory With Predicts", None))
            self.open_dir_with_predicts_btn.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
            self.lb_filters.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
            self.lb_edges.setText(QCoreApplication.translate("MainWindow", u"Edge:", None))
            self.lb_cut.setText(QCoreApplication.translate("MainWindow", u"Cut:", None))
            self.set_values_filters_btn.setText(QCoreApplication.translate("MainWindow", u"Set Values", None))
            self.lb_image_distance.setText(QCoreApplication.translate("MainWindow", u"Image Distance:", None))
            self.lb_unit_image_distance.setText(QCoreApplication.translate("MainWindow", u"m", None))
            self.lb_focal_lenght.setText(QCoreApplication.translate("MainWindow", u"Focal Lenght:", None))
            self.lb_focal_lenght_unit.setText(QCoreApplication.translate("MainWindow", u"mm", None))
            self.lb_sensor_height.setText(QCoreApplication.translate("MainWindow", u"Sensor Height:", None))
            self.lb_sensor_height_unit.setText(QCoreApplication.translate("MainWindow", u"mm", None))
            self.lb_pixel_height.setText(QCoreApplication.translate("MainWindow", u"Pixel Height:", None))
            self.lb_pixel_height_unit.setText(QCoreApplication.translate("MainWindow", u"px", None))
            self.lb_pixel_width.setText(QCoreApplication.translate("MainWindow", u"Pixel Width:", None))
            self.lb_pixel_width_unit.setText(QCoreApplication.translate("MainWindow", u"px", None))
            self.lb_sensor_width.setText(QCoreApplication.translate("MainWindow", u"Sensor Width:", None))
            self.lb_sensor_width_unit.setText(QCoreApplication.translate("MainWindow", u"mm", None))
            self.set_values_parameters_btn.setText(QCoreApplication.translate("MainWindow", u"Set Values", None))
            self.lb_measure.setText(QCoreApplication.translate("MainWindow", u"Measure", None))
            self.lb_clear_measure.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
            self.clear_measure_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.line_image_distance.setText("")
            self.line_focal_lenght.setText("")
            self.line_sensor_height.setText("")
            self.line_sensor_width.setText("")
            self.line_pixel_width.setText("")
            self.line_pixel_height.setText("")
            self.line_edge.setText("")
            self.line_cut.setText("")
            self.nepochs.setText("")
            self.measure_btn_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.lb_parameters.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
            self.clear_values_filters_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
            self.clear_values_parameters_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Parameters", None))
            self.lb_title_train_from_start_5.setText(QCoreApplication.translate("MainWindow", u"Velocity Page", None))
            self.lb_coordinates_points.setText(QCoreApplication.translate("MainWindow", u"Coordinates of points", None))
            self.lb_open_movie.setText(QCoreApplication.translate("MainWindow", u"Open Movie", None))
            self.next_camera.setText(QCoreApplication.translate("MainWindow", u"Next Camera", None))
            self.previous_camera.setText(QCoreApplication.translate("MainWindow", u"Previous Camera", None))
            self.open_movie.setText(QCoreApplication.translate("MainWindow", u"Open Directory", None))
            self.add_point.setText(QCoreApplication.translate("MainWindow", u"Add Point", None))
            self.clear_point.setText(QCoreApplication.translate("MainWindow", u"Clear Point", None))
            self.set_coordinates.setText(QCoreApplication.translate("MainWindow", u"Set Coordinates", None))
            ___qtablewidgetitem = self.table_coordinates_point.horizontalHeaderItem(0)
            ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X1", None))
            ___qtablewidgetitem1 = self.table_coordinates_point.horizontalHeaderItem(1)
            ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y1", None))
            ___qtablewidgetitem2 = self.table_coordinates_point.horizontalHeaderItem(2)
            ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"X2", None))
            ___qtablewidgetitem3 = self.table_coordinates_point.horizontalHeaderItem(3)
            ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Y2", None))
            self.rd_btn_sfiv.setText(QCoreApplication.translate("MainWindow", u"SFIV", None))
            self.rd_btn_direct.setText(QCoreApplication.translate("MainWindow", u"Direct", None))
            self.rd_btn_ignored.setText(QCoreApplication.translate("MainWindow", u"Ignored Aspect", None))
            self.rd_btn_keep.setText(QCoreApplication.translate("MainWindow", u"Keep Aspect", None))
            self.rd_btn_keep_expand.setText(QCoreApplication.translate("MainWindow", u"Keep Aspect and Expand", None))
            self.lb_method.setText(QCoreApplication.translate("MainWindow", u"Method", None))
            self.nepochs_label.setText(QCoreApplication.translate("MainWindow", u"Number of Epochs:", None))
            self.scale_train.setText(QCoreApplication.translate("MainWindow", u"Scale:", None))
            self.px_mm.setText(QCoreApplication.translate("MainWindow", u"px/mm", None))
            self.lb_or.setText(QCoreApplication.translate("MainWindow", u"Or", None))
            self.btn_stabilization_movie.setText(
                    QCoreApplication.translate("MainWindow", u"Stabilization of Movie", None))
            self.btn_estimate_velocity.setText(QCoreApplication.translate("MainWindow", u"Estimate velocity", None))
            self.lb_objects.setText(QCoreApplication.translate("MainWindow", u"Objects:", None))
            self.x_label.setText(QCoreApplication.translate("MainWindow", u"X1:", None))
            self.y_label.setText(QCoreApplication.translate("MainWindow", u"Y1:", None))
            self.x2_label.setText(QCoreApplication.translate("MainWindow", u"X2:", None))
            self.y2_label.setText(QCoreApplication.translate("MainWindow", u"Y2:", None))
            self.Ok_method.setText(QCoreApplication.translate("MainWindow", u"OK", None))
            self.lb_time_actual.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
            self.lb_total_time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
            self.sound.setText("")
            self.mute_sound.setText("")
            self.stop_button.setText("")
            self.pause_button.setText("")
            self.play_button.setText("")
            self.back_time_button.setText("")
            self.foward_time_button.setText("")
            self.label_9.setText(QCoreApplication.translate("MainWindow", u"X:", None))
            self.radioButton_2.setText("")
            self.label_10.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
            self.identify_check_box.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
            self.update_models.setText("")
            self.back_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
            self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
            self.next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))

    # retranslateUi

