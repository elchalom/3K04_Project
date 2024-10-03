# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setMinimumSize(QSize(800, 600))
        Widget.setMaximumSize(QSize(800, 600))
        Widget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet(u"QWidget {\n"
"	background-color: #121212;\n"
"}")
        self.login_screen = QWidget(Widget)
        self.login_screen.setObjectName(u"login_screen")
        self.login_screen.setGeometry(QRect(250, 80, 301, 421))
        self.login_screen.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border-radius: 10px;\n"
"}")
        self.Logo = QLabel(self.login_screen)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(100, 20, 91, 31))
        font = QFont()
        font.setPointSize(24)
        self.Logo.setFont(font)
        self.Logo.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.layoutWidget = QWidget(self.login_screen)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 230, 241, 63))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.password_label = QLabel(self.layoutWidget)
        self.password_label.setObjectName(u"password_label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.password_label.setFont(font1)
        self.password_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.password_label)

        self.password_input = QLineEdit(self.layoutWidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #3f3f3f;\n"
"	padding: 10px 20px;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.password_input)

        self.login_button = QPushButton(self.login_screen)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(110, 330, 81, 31))
        font2 = QFont()
        font2.setBold(True)
        self.login_button.setFont(font2)
        self.login_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #f5968d;\n"
"	border-radius: 15px;\n"
"}")
        self.register_button = QPushButton(self.login_screen)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(110, 370, 81, 31))
        self.register_button.setFont(font2)
        self.register_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.register_button.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(129, 255, 247);\n"
"}")
        self.register_button.setCheckable(False)
        self.widget = QWidget(self.login_screen)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 70, 241, 80))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLabel {\n"
"color: #faaca3;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(11)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"QLabel {\n"
"color: white;\n"
"}")

        self.verticalLayout.addWidget(self.label_2)

        self.widget1 = QWidget(self.login_screen)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 160, 241, 63))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.username_label = QLabel(self.widget1)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setFont(font1)
        self.username_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.username_label)

        self.username_input = QLineEdit(self.widget1)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #3f3f3f;\n"
"	padding: 10px 20px;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.username_input)

        self.label_2.raise_()
        self.label.raise_()
        self.Logo.raise_()
        self.username_label.raise_()
        self.username_input.raise_()
        self.layoutWidget.raise_()
        self.login_button.raise_()
        self.register_button.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"The Fitness\u00ae: Pacemaker Monitor", None))
        self.Logo.setText(QCoreApplication.translate("Widget", u"LOGO", None))
        self.password_label.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("Widget", u"LOGIN", None))
        self.register_button.setText(QCoreApplication.translate("Widget", u"REGISTER", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Log in / Register", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Welcome back! Glad to see you. \n"
"Again!", None))
        self.username_label.setText(QCoreApplication.translate("Widget", u"Username", None))
    # retranslateUi

