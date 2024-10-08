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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import rc_images

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(800, 600)
        LoginScreen.setMinimumSize(QSize(800, 600))
        LoginScreen.setMaximumSize(QSize(800, 600))
        LoginScreen.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        LoginScreen.setAutoFillBackground(False)
        LoginScreen.setStyleSheet(u"QWidget {\n"
"	background-color: #121212;\n"
"}")
        self.login_screen = QWidget(LoginScreen)
        self.login_screen.setObjectName(u"login_screen")
        self.login_screen.setGeometry(QRect(250, 90, 301, 401))
        self.login_screen.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border-radius: 10px;\n"
"}")
        self.layoutWidget = QWidget(self.login_screen)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 230, 241, 63))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.password_label = QLabel(self.layoutWidget)
        self.password_label.setObjectName(u"password_label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.password_label.setFont(font)
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
        self.login_button.setGeometry(QRect(110, 310, 81, 31))
        font1 = QFont()
        font1.setBold(True)
        self.login_button.setFont(font1)
        self.login_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #f5968d;\n"
"	border-radius: 15px;\n"
"}")
        self.layoutWidget1 = QWidget(self.login_screen)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 70, 241, 80))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"color: #faaca3;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(11)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel {\n"
"color: white;\n"
"}")

        self.verticalLayout.addWidget(self.label_2)

        self.layoutWidget2 = QWidget(self.login_screen)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 160, 241, 63))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.username_label = QLabel(self.layoutWidget2)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setFont(font)
        self.username_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.username_label)

        self.username_input = QLineEdit(self.layoutWidget2)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #3f3f3f;\n"
"	padding: 10px 20px;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.username_input)

        self.layoutWidget3 = QWidget(self.login_screen)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(50, 350, 184, 18))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.register_screen_button = QPushButton(self.layoutWidget3)
        self.register_screen_button.setObjectName(u"register_screen_button")
        self.register_screen_button.setFont(font1)
        self.register_screen_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.register_screen_button.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(129, 255, 247);\n"
"}")
        self.register_screen_button.setCheckable(False)

        self.horizontalLayout.addWidget(self.register_screen_button)

        self.register_screen_button_2 = QPushButton(self.layoutWidget3)
        self.register_screen_button_2.setObjectName(u"register_screen_button_2")
        self.register_screen_button_2.setFont(font1)
        self.register_screen_button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.register_screen_button_2.setStyleSheet(u"QPushButton {\n"
"	color: #ea6a63;\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(129, 255, 247);\n"
"}")
        self.register_screen_button_2.setCheckable(False)

        self.horizontalLayout.addWidget(self.register_screen_button_2)

        self.Logo_4 = QLabel(self.login_screen)
        self.Logo_4.setObjectName(u"Logo_4")
        self.Logo_4.setGeometry(QRect(190, 20, 91, 71))
        font4 = QFont()
        font4.setPointSize(24)
        self.Logo_4.setFont(font4)
        self.Logo_4.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.Logo_4.setPixmap(QPixmap(u":/logo/logo.png"))
        self.Logo_4.setScaledContents(True)
        self.layoutWidget1.raise_()
        self.layoutWidget1.raise_()
        self.layoutWidget1.raise_()
        self.layoutWidget1.raise_()
        self.login_button.raise_()
        self.Logo_4.raise_()
        self.register_screen = QWidget(LoginScreen)
        self.register_screen.setObjectName(u"register_screen")
        self.register_screen.setEnabled(True)
        self.register_screen.setGeometry(QRect(250, 40, 301, 491))
        self.register_screen.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border-radius: 10px;\n"
"}")
        self.Logo_3 = QLabel(self.register_screen)
        self.Logo_3.setObjectName(u"Logo_3")
        self.Logo_3.setGeometry(QRect(190, 10, 91, 71))
        self.Logo_3.setFont(font4)
        self.Logo_3.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.Logo_3.setPixmap(QPixmap(u":/logo/logo.png"))
        self.Logo_3.setScaledContents(True)
        self.layoutWidget_5 = QWidget(self.register_screen)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(30, 230, 241, 85))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.password_label_3 = QLabel(self.layoutWidget_5)
        self.password_label_3.setObjectName(u"password_label_3")
        self.password_label_3.setFont(font)
        self.password_label_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.password_label_3.setMargin(0)

        self.verticalLayout_7.addWidget(self.password_label_3)

        self.label_7 = QLabel(self.layoutWidget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"	color: #999999;\n"
"	margin-top: -9;\n"
"}")
        self.label_7.setLineWidth(0)
        self.label_7.setMargin(0)

        self.verticalLayout_7.addWidget(self.label_7)

        self.reg_password_input_1 = QLineEdit(self.layoutWidget_5)
        self.reg_password_input_1.setObjectName(u"reg_password_input_1")
        self.reg_password_input_1.setStyleSheet(u"QLineEdit {\n"
"	background-color: #3f3f3f;\n"
"	padding: 10px 20px;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}")

        self.verticalLayout_7.addWidget(self.reg_password_input_1)

        self.register_button = QPushButton(self.register_screen)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(110, 400, 81, 31))
        self.register_button.setFont(font1)
        self.register_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.register_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #f5968d;\n"
"	border-radius: 15px;\n"
"}")
        self.layoutWidget_6 = QWidget(self.register_screen)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(30, 70, 241, 80))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"QLabel {\n"
"color: #faaca3;\n"
"}")

        self.verticalLayout_8.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"QLabel {\n"
"color: white;\n"
"}")

        self.verticalLayout_8.addWidget(self.label_6)

        self.layoutWidget_7 = QWidget(self.register_screen)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(30, 160, 241, 63))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.username_label_3 = QLabel(self.layoutWidget_7)
        self.username_label_3.setObjectName(u"username_label_3")
        self.username_label_3.setFont(font)
        self.username_label_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.username_label_3)

        self.reg_username_input = QLineEdit(self.layoutWidget_7)
        self.reg_username_input.setObjectName(u"reg_username_input")
        self.reg_username_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #3f3f3f;\n"
"	padding: 10px 20px;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}")

        self.verticalLayout_9.addWidget(self.reg_username_input)

        self.layoutWidget_8 = QWidget(self.register_screen)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(30, 320, 241, 63))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.username_label_4 = QLabel(self.layoutWidget_8)
        self.username_label_4.setObjectName(u"username_label_4")
        self.username_label_4.setFont(font)
        self.username_label_4.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.username_label_4)

        self.reg_password_input_2 = QLineEdit(self.layoutWidget_8)
        self.reg_password_input_2.setObjectName(u"reg_password_input_2")
        self.reg_password_input_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #3f3f3f;\n"
"	padding: 10px 20px;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}")

        self.verticalLayout_10.addWidget(self.reg_password_input_2)

        self.layoutWidget_9 = QWidget(self.register_screen)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(60, 440, 181, 18))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.login_screen_button = QPushButton(self.layoutWidget_9)
        self.login_screen_button.setObjectName(u"login_screen_button")
        self.login_screen_button.setFont(font1)
        self.login_screen_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_screen_button.setStyleSheet(u"QPushButton {\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(129, 255, 247);\n"
"}")
        self.login_screen_button.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.login_screen_button)

        self.login_screen_button_2 = QPushButton(self.layoutWidget_9)
        self.login_screen_button_2.setObjectName(u"login_screen_button_2")
        self.login_screen_button_2.setFont(font1)
        self.login_screen_button_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_screen_button_2.setStyleSheet(u"QPushButton {\n"
"	color: #ea6a63;\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"	background-color: rgb(129, 255, 247);\n"
"}")
        self.login_screen_button_2.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.login_screen_button_2)

        self.layoutWidget_5.raise_()
        self.register_button.raise_()
        self.layoutWidget_6.raise_()
        self.layoutWidget_7.raise_()
        self.layoutWidget_8.raise_()
        self.layoutWidget_9.raise_()
        self.Logo_3.raise_()

        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"The Fitness\u00ae: Pacemaker Monitor", None))
        self.password_label.setText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("LoginScreen", u"LOGIN", None))
        self.label.setText(QCoreApplication.translate("LoginScreen", u"Log in", None))
        self.label_2.setText(QCoreApplication.translate("LoginScreen", u"Welcome back! Glad to see you. \n"
"Again!", None))
        self.username_label.setText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.username_input.setPlaceholderText("")
        self.register_screen_button.setText(QCoreApplication.translate("LoginScreen", u"Don't have an account?", None))
        self.register_screen_button_2.setText(QCoreApplication.translate("LoginScreen", u"Register", None))
        self.Logo_4.setText("")
        self.Logo_3.setText("")
        self.password_label_3.setText(QCoreApplication.translate("LoginScreen", u"Create a password", None))
        self.label_7.setText(QCoreApplication.translate("LoginScreen", u"Must have at least 6 characters", None))
        self.register_button.setText(QCoreApplication.translate("LoginScreen", u"REGISTER", None))
        self.label_5.setText(QCoreApplication.translate("LoginScreen", u"Register", None))
        self.label_6.setText(QCoreApplication.translate("LoginScreen", u"Join us today! We're excited to have\n"
"you on board.", None))
        self.username_label_3.setText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.reg_username_input.setPlaceholderText("")
        self.username_label_4.setText(QCoreApplication.translate("LoginScreen", u"Confirm a password", None))
        self.reg_password_input_2.setPlaceholderText("")
        self.login_screen_button.setText(QCoreApplication.translate("LoginScreen", u"Already have an account?", None))
        self.login_screen_button_2.setText(QCoreApplication.translate("LoginScreen", u"Log in", None))
    # retranslateUi

