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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
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
        self.connection_box.setGeometry(QRect(0, 560, 231, 71))
        self.connection_box.setStyleSheet(u"QWidget {\n"
"	background-color: #313131;\n"
"}")
        self.connect_button = QPushButton(self.connection_box)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setGeometry(QRect(20, 10, 42, 42))
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
        self.connect_label = QLabel(self.connection_box)
        self.connect_label.setObjectName(u"connect_label")
        self.connect_label.setGeometry(QRect(70, 20, 161, 21))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.connect_label.setFont(font)
        self.connect_label.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"}")
        self.disconnect_button = QPushButton(self.connection_box)
        self.disconnect_button.setObjectName(u"disconnect_button")
        self.disconnect_button.setGeometry(QRect(20, 10, 42, 42))
        self.disconnect_button.setStyleSheet(u"QPushButton {\n"
"      border-radius: 21px;       /* Half of width/height (42/2 = 21) */\n"
"      border: 2px solid #282828; /* Darker green border */\n"
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
"	background-color: #00b075;\n"
"}")
        self.AAI_mode = QPushButton(self.sidebar)
        self.AAI_mode.setObjectName(u"AAI_mode")
        self.AAI_mode.setGeometry(QRect(0, 190, 221, 61))
        self.AAI_mode.setFont(font1)
        self.AAI_mode.setStyleSheet(u"QPushButton {\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 30px;\n"
"	background-color:  #393939;\n"
"	color: #ffffff;	\n"
"}")
        self.VOO_mode = QPushButton(self.sidebar)
        self.VOO_mode.setObjectName(u"VOO_mode")
        self.VOO_mode.setGeometry(QRect(0, 270, 221, 61))
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
        self.Logo_3 = QLabel(HomeScreen)
        self.Logo_3.setObjectName(u"Logo_3")
        self.Logo_3.setGeometry(QRect(940, 10, 91, 71))
        font2 = QFont()
        font2.setPointSize(24)
        self.Logo_3.setFont(font2)
        self.Logo_3.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.Logo_3.setPixmap(QPixmap(u":/logo/logo.png"))
        self.Logo_3.setScaledContents(True)
        self.AOO_screen = QWidget(HomeScreen)
        self.AOO_screen.setObjectName(u"AOO_screen")
        self.AOO_screen.setGeometry(QRect(310, 70, 561, 111))
        self.AOO_screen.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 0, 4);\n"
"}")
        self.AAI_screen = QWidget(HomeScreen)
        self.AAI_screen.setObjectName(u"AAI_screen")
        self.AAI_screen.setGeometry(QRect(310, 200, 561, 111))
        self.AAI_screen.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 0, 255);\n"
"}")
        self.VOO_screen = QWidget(HomeScreen)
        self.VOO_screen.setObjectName(u"VOO_screen")
        self.VOO_screen.setGeometry(QRect(310, 330, 561, 111))
        self.VOO_screen.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 0);\n"
"}")
        self.VVI_screen = QWidget(HomeScreen)
        self.VVI_screen.setObjectName(u"VVI_screen")
        self.VVI_screen.setGeometry(QRect(310, 460, 561, 111))
        self.VVI_screen.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 255);\n"
"}")

        self.retranslateUi(HomeScreen)

        QMetaObject.connectSlotsByName(HomeScreen)
    # setupUi

    def retranslateUi(self, HomeScreen):
        HomeScreen.setWindowTitle(QCoreApplication.translate("HomeScreen", u"The Fitness\u00ae: Pacemaker Monitor", None))
        self.connect_button.setText("")
        self.connect_label.setText(QCoreApplication.translate("HomeScreen", u"Device Connected", None))
        self.disconnect_button.setText("")
        self.username.setText(QCoreApplication.translate("HomeScreen", u"username", None))
        self.signout.setText("")
        self.AOO_mode.setText(QCoreApplication.translate("HomeScreen", u"AOO Mode", None))
        self.AAI_mode.setText(QCoreApplication.translate("HomeScreen", u"AAI Mode", None))
        self.VOO_mode.setText(QCoreApplication.translate("HomeScreen", u"VOO Mode", None))
        self.VVI_mode.setText(QCoreApplication.translate("HomeScreen", u"VVI Mode", None))
        self.Logo_3.setText("")
    # retranslateUi

