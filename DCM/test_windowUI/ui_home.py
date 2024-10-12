# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import rc_images

class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        if not HomeScreen.objectName():
            HomeScreen.setObjectName(u"HomeScreen")
        HomeScreen.resize(1034, 625)
        HomeScreen.setMinimumSize(QSize(1034, 625))
        HomeScreen.setMaximumSize(QSize(1034, 625))
        HomeScreen.setStyleSheet(u"QWidget {\n"
"	background-color: #121212;\n"
"}")
        self.sidebar = QWidget(HomeScreen)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(0, 0, 231, 631))
        self.sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: #282828;\n"
"}")
        self.connection_box = QWidget(self.sidebar)
        self.connection_box.setObjectName(u"connection_box")
        self.connection_box.setGeometry(QRect(0, 550, 231, 81))
        self.connection_box.setStyleSheet(u"QWidget {\n"
"	background-color: #313131;\n"
"}")
        self.connect_button = QPushButton(self.connection_box)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setGeometry(QRect(20, 20, 42, 42))
        self.connect_button.setStyleSheet(u"QPushButton {\n"
"      background-color: #00b075; /* Green background */\n"
"      border: 2px solid #00bf7c; /* Darker green border */\n"
"      border-radius: 21px;       /* Half of width/height (42/2 = 21) */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"      background-color: #00a86d;  /* Darker green when pressed */\n"
"      border: 2px solid #2E7031;  /* Even darker border when pressed */\n"
"}")
        self.disconnect_button = QPushButton(self.connection_box)
        self.disconnect_button.setObjectName(u"disconnect_button")
        self.disconnect_button.setGeometry(QRect(20, 20, 42, 42))
        self.disconnect_button.setStyleSheet(u"QPushButton {\n"
"      border-radius: 21px;       /* Half of width/height (42/2 = 21) */\n"
"      border: 2px solid #282828; /* Darker green border */\n"
"}")
        self.serial_label = QLabel(self.connection_box)
        self.serial_label.setObjectName(u"serial_label")
        self.serial_label.setGeometry(QRect(70, 50, 159, 16))
        self.serial_label.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"}")
        self.serial_name_label = QLabel(self.connection_box)
        self.serial_name_label.setObjectName(u"serial_name_label")
        self.serial_name_label.setGeometry(QRect(70, 30, 159, 16))
        self.serial_name_label.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"}")
        self.connect_label = QLabel(self.connection_box)
        self.connect_label.setObjectName(u"connect_label")
        self.connect_label.setGeometry(QRect(70, 10, 159, 13))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.connect_label.setFont(font)
        self.connect_label.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"}")
        self.user_box = QWidget(self.sidebar)
        self.user_box.setObjectName(u"user_box")
        self.user_box.setGeometry(QRect(0, 0, 231, 51))
        self.user_box.setStyleSheet(u"QWidget {\n"
"	background-color: #313131;\n"
"}")
        self.username = QLabel(self.user_box)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(20, 10, 141, 31))
        self.username.setFont(font)
        self.username.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"}")
        self.signout = QPushButton(self.user_box)
        self.signout.setObjectName(u"signout")
        self.signout.setGeometry(QRect(190, 10, 31, 31))
        self.signout.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/logo/logout_icon.png);\n"
"}")
        self.AOO_mode = QPushButton(self.sidebar)
        self.AOO_mode.setObjectName(u"AOO_mode")
        self.AOO_mode.setGeometry(QRect(0, 110, 221, 61))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.AOO_mode.setFont(font1)
        self.AOO_mode.setStyleSheet(u"QPushButton {\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 30px;\n"
"	color: #ffffff;	\n"
"	/*background-color: #00b075;*/\n"
"	background-color: #f64d59;\n"
"}")
        self.AAI_mode = QPushButton(self.sidebar)
        self.AAI_mode.setObjectName(u"AAI_mode")
        self.AAI_mode.setGeometry(QRect(0, 270, 221, 61))
        self.AAI_mode.setFont(font1)
        self.AAI_mode.setStyleSheet(u"QPushButton {\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 30px;\n"
"	background-color:  #393939;\n"
"	color: #ffffff;	\n"
"}")
        self.VOO_mode = QPushButton(self.sidebar)
        self.VOO_mode.setObjectName(u"VOO_mode")
        self.VOO_mode.setGeometry(QRect(0, 190, 221, 61))
        self.VOO_mode.setFont(font1)
        self.VOO_mode.setStyleSheet(u"QPushButton {\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 30px;\n"
"	background-color: #393939;\n"
"	color: #ffffff;	\n"
"}")
        self.VVI_mode = QPushButton(self.sidebar)
        self.VVI_mode.setObjectName(u"VVI_mode")
        self.VVI_mode.setGeometry(QRect(0, 350, 221, 61))
        self.VVI_mode.setFont(font1)
        self.VVI_mode.setStyleSheet(u"QPushButton {\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 30px;\n"
"	background-color: #393939;\n"
"	color: #ffffff;	\n"
"}")
        self.AOO_screen = QWidget(HomeScreen)
        self.AOO_screen.setObjectName(u"AOO_screen")
        self.AOO_screen.setGeometry(QRect(240, 20, 781, 591))
        self.AOO_screen.setStyleSheet(u"QWidget {\n"
"	background-color: #282828;\n"
"	border-radius: 9px;\n"
"}")
        self.Logo_3 = QLabel(self.AOO_screen)
        self.Logo_3.setObjectName(u"Logo_3")
        self.Logo_3.setGeometry(QRect(690, 0, 91, 71))
        font2 = QFont()
        font2.setPointSize(24)
        self.Logo_3.setFont(font2)
        self.Logo_3.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.Logo_3.setPixmap(QPixmap(u":/logo/logo.png"))
        self.Logo_3.setScaledContents(True)
        self.widget = QWidget(self.AOO_screen)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 181, 241))
        self.widget.setStyleSheet(u"QWidget {\n"
"	border: 2px solid #db333c;\n"
"}")
        self.AOO_lower_rate_limit = QLineEdit(self.widget)
        self.AOO_lower_rate_limit.setObjectName(u"AOO_lower_rate_limit")
        self.AOO_lower_rate_limit.setGeometry(QRect(10, 60, 161, 21))
        self.AOO_lower_rate_limit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 101, 16))
        font3 = QFont()
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 141, 21))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: #db333c;\n"
"border: none;\n"
"}")
        self.AOO_upper_rate_limit = QLineEdit(self.widget)
        self.AOO_upper_rate_limit.setObjectName(u"AOO_upper_rate_limit")
        self.AOO_upper_rate_limit.setGeometry(QRect(10, 110, 161, 21))
        self.AOO_upper_rate_limit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 101, 16))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.AOO_atrial_amplitude = QLineEdit(self.widget)
        self.AOO_atrial_amplitude.setObjectName(u"AOO_atrial_amplitude")
        self.AOO_atrial_amplitude.setGeometry(QRect(10, 160, 161, 21))
        self.AOO_atrial_amplitude.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 101, 16))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.AOO_atrial_pulse_width = QLineEdit(self.widget)
        self.AOO_atrial_pulse_width.setObjectName(u"AOO_atrial_pulse_width")
        self.AOO_atrial_pulse_width.setGeometry(QRect(10, 210, 161, 21))
        self.AOO_atrial_pulse_width.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 190, 101, 16))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.graph_widget_AOO = QWidget(self.AOO_screen)
        self.graph_widget_AOO.setObjectName(u"graph_widget_AOO")
        self.graph_widget_AOO.setGeometry(QRect(200, 90, 571, 321))
        self.graph_widget_AOO.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.AOO_submit = QPushButton(self.AOO_screen)
        self.AOO_submit.setObjectName(u"AOO_submit")
        self.AOO_submit.setGeometry(QRect(50, 260, 101, 30))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setKerning(True)
        self.AOO_submit.setFont(font5)
        self.AOO_submit.setStyleSheet(u"QPushButton {\n"
"	background-color: #faaca3;\n"
"	border-radius: 15px;\n"
"	border: 2px solid #db333c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"      background-color: #00a86d;  /* Darker green when pressed */\n"
"      border: 2px solid #2E7031;  /* Even darker border when pressed */\n"
"}")
        self.AOO_retrieve = QPushButton(self.AOO_screen)
        self.AOO_retrieve.setObjectName(u"AOO_retrieve")
        self.AOO_retrieve.setGeometry(QRect(50, 300, 101, 30))
        self.AOO_retrieve.setFont(font5)
        self.AOO_retrieve.setStyleSheet(u"QPushButton {\n"
"	background-color: #faaca3;\n"
"	border-radius: 15px;\n"
"	border: 2px solid #db333c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"      background-color: #00a86d;  /* Darker green when pressed */\n"
"      border: 2px solid #2E7031;  /* Even darker border when pressed */\n"
"}")
        self.Logo_3.raise_()
        self.widget.raise_()
        self.AOO_submit.raise_()
        self.AOO_retrieve.raise_()
        self.graph_widget_AOO.raise_()
        self.VOO_screen = QWidget(HomeScreen)
        self.VOO_screen.setObjectName(u"VOO_screen")
        self.VOO_screen.setGeometry(QRect(240, 20, 781, 591))
        self.VOO_screen.setStyleSheet(u"QWidget {\n"
"	background-color: #282828;\n"
"	border-radius: 9px;\n"
"}")
        self.Logo_4 = QLabel(self.VOO_screen)
        self.Logo_4.setObjectName(u"Logo_4")
        self.Logo_4.setGeometry(QRect(690, 0, 91, 71))
        self.Logo_4.setFont(font2)
        self.Logo_4.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.Logo_4.setPixmap(QPixmap(u":/logo/logo.png"))
        self.Logo_4.setScaledContents(True)
        self.widget_2 = QWidget(self.VOO_screen)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 10, 181, 241))
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	border: 2px solid #db333c;\n"
"}")
        self.VOO_lower_rate_limit = QLineEdit(self.widget_2)
        self.VOO_lower_rate_limit.setObjectName(u"VOO_lower_rate_limit")
        self.VOO_lower_rate_limit.setGeometry(QRect(10, 60, 161, 21))
        self.VOO_lower_rate_limit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 40, 101, 16))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 141, 21))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"QLabel {\n"
"	color: #db333c;\n"
"border: none;\n"
"}")
        self.VOO_upper_rate_limit = QLineEdit(self.widget_2)
        self.VOO_upper_rate_limit.setObjectName(u"VOO_upper_rate_limit")
        self.VOO_upper_rate_limit.setGeometry(QRect(10, 110, 161, 21))
        self.VOO_upper_rate_limit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 90, 101, 16))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.VOO_ventrical_amplitude = QLineEdit(self.widget_2)
        self.VOO_ventrical_amplitude.setObjectName(u"VOO_ventrical_amplitude")
        self.VOO_ventrical_amplitude.setGeometry(QRect(10, 160, 161, 21))
        self.VOO_ventrical_amplitude.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 140, 111, 16))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.VOO_ventrical_pulse_width = QLineEdit(self.widget_2)
        self.VOO_ventrical_pulse_width.setObjectName(u"VOO_ventrical_pulse_width")
        self.VOO_ventrical_pulse_width.setGeometry(QRect(10, 210, 161, 21))
        self.VOO_ventrical_pulse_width.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 190, 121, 16))
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.graph_widget_VOO = QWidget(self.VOO_screen)
        self.graph_widget_VOO.setObjectName(u"graph_widget_VOO")
        self.graph_widget_VOO.setGeometry(QRect(200, 90, 571, 321))
        self.graph_widget_VOO.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.VOO_submit = QPushButton(self.VOO_screen)
        self.VOO_submit.setObjectName(u"VOO_submit")
        self.VOO_submit.setGeometry(QRect(50, 260, 101, 30))
        self.VOO_submit.setFont(font5)
        self.VOO_submit.setStyleSheet(u"QPushButton {\n"
"	background-color: #faaca3;\n"
"	border-radius: 15px;\n"
"	border: 2px solid #db333c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"      background-color: #00a86d;  /* Darker green when pressed */\n"
"      border: 2px solid #2E7031;  /* Even darker border when pressed */\n"
"}")
        self.VOO_retrieve = QPushButton(self.VOO_screen)
        self.VOO_retrieve.setObjectName(u"VOO_retrieve")
        self.VOO_retrieve.setGeometry(QRect(50, 300, 101, 30))
        self.VOO_retrieve.setFont(font5)
        self.VOO_retrieve.setStyleSheet(u"QPushButton {\n"
"	background-color: #faaca3;\n"
"	border-radius: 15px;\n"
"	border: 2px solid #db333c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"      background-color: #00a86d;  /* Darker green when pressed */\n"
"      border: 2px solid #2E7031;  /* Even darker border when pressed */\n"
"}")
        self.VVI_screen = QWidget(HomeScreen)
        self.VVI_screen.setObjectName(u"VVI_screen")
        self.VVI_screen.setGeometry(QRect(240, 20, 781, 591))
        self.VVI_screen.setStyleSheet(u"QWidget {\n"
"	background-color: #282828;\n"
"	border-radius: 9px;\n"
"}")
        self.Logo_5 = QLabel(self.VVI_screen)
        self.Logo_5.setObjectName(u"Logo_5")
        self.Logo_5.setGeometry(QRect(690, 0, 91, 71))
        self.Logo_5.setFont(font2)
        self.Logo_5.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.Logo_5.setPixmap(QPixmap(u":/logo/logo.png"))
        self.Logo_5.setScaledContents(True)
        self.widget_3 = QWidget(self.VVI_screen)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 10, 181, 441))
        self.widget_3.setStyleSheet(u"QWidget {\n"
"	border: 2px solid #db333c;\n"
"}")
        self.VVI_lower_rate_limit = QLineEdit(self.widget_3)
        self.VVI_lower_rate_limit.setObjectName(u"VVI_lower_rate_limit")
        self.VVI_lower_rate_limit.setGeometry(QRect(10, 60, 161, 21))
        self.VVI_lower_rate_limit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 40, 101, 16))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 10, 141, 21))
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"QLabel {\n"
"	color: #db333c;\n"
"border: none;\n"
"}")
        self.VVI_upper_rate_limit = QLineEdit(self.widget_3)
        self.VVI_upper_rate_limit.setObjectName(u"VVI_upper_rate_limit")
        self.VVI_upper_rate_limit.setGeometry(QRect(10, 110, 161, 21))
        self.VVI_upper_rate_limit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 90, 101, 16))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.VVI_ventrical_amplitude = QLineEdit(self.widget_3)
        self.VVI_ventrical_amplitude.setObjectName(u"VVI_ventrical_amplitude")
        self.VVI_ventrical_amplitude.setGeometry(QRect(10, 160, 161, 21))
        self.VVI_ventrical_amplitude.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 140, 111, 16))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.VVI_ventrical_pulse_width = QLineEdit(self.widget_3)
        self.VVI_ventrical_pulse_width.setObjectName(u"VVI_ventrical_pulse_width")
        self.VVI_ventrical_pulse_width.setGeometry(QRect(10, 210, 161, 21))
        self.VVI_ventrical_pulse_width.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 190, 121, 16))
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.VVI_ventrical_sensitivity = QLineEdit(self.widget_3)
        self.VVI_ventrical_sensitivity.setObjectName(u"VVI_ventrical_sensitivity")
        self.VVI_ventrical_sensitivity.setGeometry(QRect(10, 260, 161, 21))
        self.VVI_ventrical_sensitivity.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 240, 121, 16))
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.VVI_vrp = QLineEdit(self.widget_3)
        self.VVI_vrp.setObjectName(u"VVI_vrp")
        self.VVI_vrp.setGeometry(QRect(10, 310, 161, 21))
        self.VVI_vrp.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 290, 121, 16))
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.VVI_hysteresis = QLineEdit(self.widget_3)
        self.VVI_hysteresis.setObjectName(u"VVI_hysteresis")
        self.VVI_hysteresis.setGeometry(QRect(10, 360, 161, 21))
        self.VVI_hysteresis.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_18 = QLabel(self.widget_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 340, 121, 16))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.VVI_rate_smoothing = QLineEdit(self.widget_3)
        self.VVI_rate_smoothing.setObjectName(u"VVI_rate_smoothing")
        self.VVI_rate_smoothing.setGeometry(QRect(10, 410, 161, 21))
        self.VVI_rate_smoothing.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_19 = QLabel(self.widget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 390, 121, 16))
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.graph_widget_VVI = QWidget(self.VVI_screen)
        self.graph_widget_VVI.setObjectName(u"graph_widget_VVI")
        self.graph_widget_VVI.setGeometry(QRect(200, 90, 571, 321))
        self.graph_widget_VVI.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.VVI_submit = QPushButton(self.VVI_screen)
        self.VVI_submit.setObjectName(u"VVI_submit")
        self.VVI_submit.setGeometry(QRect(50, 460, 101, 30))
        self.VVI_submit.setFont(font5)
        self.VVI_submit.setStyleSheet(u"QPushButton {\n"
"	background-color: #faaca3;\n"
"	border-radius: 15px;\n"
"	border: 2px solid #db333c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"      background-color: #00a86d;  /* Darker green when pressed */\n"
"      border: 2px solid #2E7031;  /* Even darker border when pressed */\n"
"}")
        self.VVI_retrieve = QPushButton(self.VVI_screen)
        self.VVI_retrieve.setObjectName(u"VVI_retrieve")
        self.VVI_retrieve.setGeometry(QRect(50, 500, 101, 30))
        self.VVI_retrieve.setFont(font5)
        self.VVI_retrieve.setStyleSheet(u"QPushButton {\n"
"	background-color: #faaca3;\n"
"	border-radius: 15px;\n"
"	border: 2px solid #db333c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"      background-color: #00a86d;  /* Darker green when pressed */\n"
"      border: 2px solid #2E7031;  /* Even darker border when pressed */\n"
"}")
        self.AAI_screen = QWidget(HomeScreen)
        self.AAI_screen.setObjectName(u"AAI_screen")
        self.AAI_screen.setGeometry(QRect(240, 20, 781, 591))
        self.AAI_screen.setStyleSheet(u"QWidget {\n"
"	background-color: #282828;\n"
"	border-radius: 9px;\n"
"}")
        self.Logo_6 = QLabel(self.AAI_screen)
        self.Logo_6.setObjectName(u"Logo_6")
        self.Logo_6.setGeometry(QRect(690, 0, 91, 71))
        self.Logo_6.setFont(font2)
        self.Logo_6.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.Logo_6.setPixmap(QPixmap(u":/logo/logo.png"))
        self.Logo_6.setScaledContents(True)
        self.widget_4 = QWidget(self.AAI_screen)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 10, 181, 491))
        self.widget_4.setStyleSheet(u"QWidget {\n"
"	border: 2px solid #db333c;\n"
"}")
        self.AAI_lower_rate_limit = QLineEdit(self.widget_4)
        self.AAI_lower_rate_limit.setObjectName(u"AAI_lower_rate_limit")
        self.AAI_lower_rate_limit.setGeometry(QRect(10, 60, 161, 21))
        self.AAI_lower_rate_limit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 40, 101, 16))
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.label_21 = QLabel(self.widget_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 10, 141, 21))
        self.label_21.setFont(font4)
        self.label_21.setStyleSheet(u"QLabel {\n"
"	color: #db333c;\n"
"border: none;\n"
"}")
        self.AAI_upper_rate_limit = QLineEdit(self.widget_4)
        self.AAI_upper_rate_limit.setObjectName(u"AAI_upper_rate_limit")
        self.AAI_upper_rate_limit.setGeometry(QRect(10, 110, 161, 21))
        self.AAI_upper_rate_limit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_22 = QLabel(self.widget_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 90, 101, 16))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.AAI_atrial_amplitude = QLineEdit(self.widget_4)
        self.AAI_atrial_amplitude.setObjectName(u"AAI_atrial_amplitude")
        self.AAI_atrial_amplitude.setGeometry(QRect(10, 160, 161, 21))
        self.AAI_atrial_amplitude.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_23 = QLabel(self.widget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 140, 111, 16))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.AAI_atrial_pulse_width = QLineEdit(self.widget_4)
        self.AAI_atrial_pulse_width.setObjectName(u"AAI_atrial_pulse_width")
        self.AAI_atrial_pulse_width.setGeometry(QRect(10, 210, 161, 21))
        self.AAI_atrial_pulse_width.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_24 = QLabel(self.widget_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 190, 121, 16))
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.AAI_atrial_sensitivity = QLineEdit(self.widget_4)
        self.AAI_atrial_sensitivity.setObjectName(u"AAI_atrial_sensitivity")
        self.AAI_atrial_sensitivity.setGeometry(QRect(10, 260, 161, 21))
        self.AAI_atrial_sensitivity.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_25 = QLabel(self.widget_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 240, 121, 16))
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.AAI_arp = QLineEdit(self.widget_4)
        self.AAI_arp.setObjectName(u"AAI_arp")
        self.AAI_arp.setGeometry(QRect(10, 310, 161, 21))
        self.AAI_arp.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_26 = QLabel(self.widget_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 290, 121, 16))
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.AAI_hysteresis = QLineEdit(self.widget_4)
        self.AAI_hysteresis.setObjectName(u"AAI_hysteresis")
        self.AAI_hysteresis.setGeometry(QRect(10, 410, 161, 21))
        self.AAI_hysteresis.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_27 = QLabel(self.widget_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 390, 121, 16))
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.AAI_rate_smoothing = QLineEdit(self.widget_4)
        self.AAI_rate_smoothing.setObjectName(u"AAI_rate_smoothing")
        self.AAI_rate_smoothing.setGeometry(QRect(10, 460, 161, 21))
        self.AAI_rate_smoothing.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.label_28 = QLabel(self.widget_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 440, 121, 16))
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.label_29 = QLabel(self.widget_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 340, 121, 16))
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"border: none;\n"
"}")
        self.AAI_pvarp = QLineEdit(self.widget_4)
        self.AAI_pvarp.setObjectName(u"AAI_pvarp")
        self.AAI_pvarp.setGeometry(QRect(10, 360, 161, 21))
        self.AAI_pvarp.setStyleSheet(u"QLineEdit {\n"
"	background-color: #efefef;\n"
"	border: none;\n"
"}")
        self.graph_widget_AAI = QWidget(self.AAI_screen)
        self.graph_widget_AAI.setObjectName(u"graph_widget_AAI")
        self.graph_widget_AAI.setGeometry(QRect(200, 90, 571, 321))
        self.graph_widget_AAI.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.AAI_submit = QPushButton(self.AAI_screen)
        self.AAI_submit.setObjectName(u"AAI_submit")
        self.AAI_submit.setGeometry(QRect(50, 510, 101, 30))
        self.AAI_submit.setFont(font5)
        self.AAI_submit.setStyleSheet(u"QPushButton {\n"
"	background-color: #faaca3;\n"
"	border-radius: 15px;\n"
"	border: 2px solid #db333c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"      background-color: #00a86d;  /* Darker green when pressed */\n"
"      border: 2px solid #2E7031;  /* Even darker border when pressed */\n"
"}")
        self.AAI_retrieve = QPushButton(self.AAI_screen)
        self.AAI_retrieve.setObjectName(u"AAI_retrieve")
        self.AAI_retrieve.setGeometry(QRect(50, 550, 101, 30))
        self.AAI_retrieve.setFont(font5)
        self.AAI_retrieve.setStyleSheet(u"QPushButton {\n"
"	background-color: #faaca3;\n"
"	border-radius: 15px;\n"
"	border: 2px solid #db333c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"      background-color: #00a86d;  /* Darker green when pressed */\n"
"      border: 2px solid #2E7031;  /* Even darker border when pressed */\n"
"}")

        self.retranslateUi(HomeScreen)

        QMetaObject.connectSlotsByName(HomeScreen)
    # setupUi

    def retranslateUi(self, HomeScreen):
        HomeScreen.setWindowTitle(QCoreApplication.translate("HomeScreen", u"The Fitness\u00ae: Pacemaker Monitor", None))
        self.connect_button.setText("")
        self.disconnect_button.setText("")
        self.serial_label.setText(QCoreApplication.translate("HomeScreen", u"Serial Number", None))
        self.serial_name_label.setText(QCoreApplication.translate("HomeScreen", u"Device Name", None))
        self.connect_label.setText(QCoreApplication.translate("HomeScreen", u"Device Connected", None))
        self.username.setText(QCoreApplication.translate("HomeScreen", u"username", None))
        self.signout.setText("")
        self.AOO_mode.setText(QCoreApplication.translate("HomeScreen", u"AOO Mode", None))
        self.AAI_mode.setText(QCoreApplication.translate("HomeScreen", u"AAI Mode", None))
        self.VOO_mode.setText(QCoreApplication.translate("HomeScreen", u"VOO Mode", None))
        self.VVI_mode.setText(QCoreApplication.translate("HomeScreen", u"VVI Mode", None))
        self.Logo_3.setText("")
        self.label.setText(QCoreApplication.translate("HomeScreen", u"Lower Rate Limit", None))
        self.label_2.setText(QCoreApplication.translate("HomeScreen", u"PARAMETERS", None))
        self.label_3.setText(QCoreApplication.translate("HomeScreen", u"Upper Rate Limit", None))
        self.label_4.setText(QCoreApplication.translate("HomeScreen", u"Atrial Amplitude", None))
        self.label_5.setText(QCoreApplication.translate("HomeScreen", u"Atrial Pulse Width", None))
        self.AOO_submit.setText(QCoreApplication.translate("HomeScreen", u"Submit Data", None))
        self.AOO_retrieve.setText(QCoreApplication.translate("HomeScreen", u"Retrieve Data", None))
        self.Logo_4.setText("")
        self.label_6.setText(QCoreApplication.translate("HomeScreen", u"Lower Rate Limit", None))
        self.label_7.setText(QCoreApplication.translate("HomeScreen", u"PARAMETERS", None))
        self.label_8.setText(QCoreApplication.translate("HomeScreen", u"Upper Rate Limit", None))
        self.label_9.setText(QCoreApplication.translate("HomeScreen", u"Ventrical Amplitude", None))
        self.label_10.setText(QCoreApplication.translate("HomeScreen", u"Ventrical Pulse Width", None))
        self.VOO_submit.setText(QCoreApplication.translate("HomeScreen", u"Submit Data", None))
        self.VOO_retrieve.setText(QCoreApplication.translate("HomeScreen", u"Retrieve Data", None))
        self.Logo_5.setText("")
        self.label_11.setText(QCoreApplication.translate("HomeScreen", u"Lower Rate Limit", None))
        self.label_12.setText(QCoreApplication.translate("HomeScreen", u"PARAMETERS", None))
        self.label_13.setText(QCoreApplication.translate("HomeScreen", u"Upper Rate Limit", None))
        self.label_14.setText(QCoreApplication.translate("HomeScreen", u"Ventrical Amplitude", None))
        self.label_15.setText(QCoreApplication.translate("HomeScreen", u"Ventrical Pulse Width", None))
        self.label_16.setText(QCoreApplication.translate("HomeScreen", u"Ventrical Sensitivity", None))
        self.label_17.setText(QCoreApplication.translate("HomeScreen", u"VRP", None))
        self.label_18.setText(QCoreApplication.translate("HomeScreen", u"Hysteresis", None))
        self.label_19.setText(QCoreApplication.translate("HomeScreen", u"Rate Smoothing", None))
        self.VVI_submit.setText(QCoreApplication.translate("HomeScreen", u"Submit Data", None))
        self.VVI_retrieve.setText(QCoreApplication.translate("HomeScreen", u"Retrieve Data", None))
        self.Logo_6.setText("")
        self.label_20.setText(QCoreApplication.translate("HomeScreen", u"Lower Rate Limit", None))
        self.label_21.setText(QCoreApplication.translate("HomeScreen", u"PARAMETERS", None))
        self.label_22.setText(QCoreApplication.translate("HomeScreen", u"Upper Rate Limit", None))
        self.label_23.setText(QCoreApplication.translate("HomeScreen", u"Atrial Amplitude", None))
        self.label_24.setText(QCoreApplication.translate("HomeScreen", u"Atrial Pulse Width", None))
        self.label_25.setText(QCoreApplication.translate("HomeScreen", u"Atrial Sensitivity", None))
        self.label_26.setText(QCoreApplication.translate("HomeScreen", u"ARP", None))
        self.label_27.setText(QCoreApplication.translate("HomeScreen", u"Hysteresis", None))
        self.label_28.setText(QCoreApplication.translate("HomeScreen", u"Rate Smoothing", None))
        self.label_29.setText(QCoreApplication.translate("HomeScreen", u"PVARP", None))
        self.AAI_submit.setText(QCoreApplication.translate("HomeScreen", u"Submit Data", None))
        self.AAI_retrieve.setText(QCoreApplication.translate("HomeScreen", u"Retrieve Data", None))
    # retranslateUi

