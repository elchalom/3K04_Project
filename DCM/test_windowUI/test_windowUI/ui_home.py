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
"	\n"
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
        self.label = QLabel(self.connection_box)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 101, 21))
        self.label.setStyleSheet(u"QLabel {\n"
"	color: #ffffff;\n"
"}")

        self.retranslateUi(HomeScreen)

        QMetaObject.connectSlotsByName(HomeScreen)
    # setupUi

    def retranslateUi(self, HomeScreen):
        HomeScreen.setWindowTitle(QCoreApplication.translate("HomeScreen", u"The Fitness\u00ae: Pacemaker Monitor", None))
        self.connect_button.setText("")
        self.label.setText(QCoreApplication.translate("HomeScreen", u"Device Connected", None))
    # retranslateUi

