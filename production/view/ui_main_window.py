# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowuVMIgW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import view.resource1_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 651, 700))
        self.frame.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(30, 59, 81, 255), stop:1 rgba(230, 136, 136, 255));\n"
            "border-radius: 10px;"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 620, 397))
        self.label_5.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n" "border-radius: 40px;"
        )
        self.label_5.setPixmap(QPixmap(u":/logo/res/logo@4.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 450, 250, 250))
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_6.setPixmap(QPixmap(u":/user/res/icons1.png"))
        self.label_6.setScaledContents(True)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(650, 10, 640, 700))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 280, 181, 41))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
            u"color: rgb(30, 59, 81);\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            ""
        )
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 540, 131, 28))
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(10)
        font1.setItalic(True)
        font1.setUnderline(True)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_2.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n" "color: rgb(0, 0, 0);"
        )
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 450, 121, 51))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(247, 247, 247, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(160, 160, 160, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
        # endif
        self.pushButton.setPalette(palette)
        font2 = QFont()
        font2.setFamily(u"MS Sans Serif")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setFocusPolicy(Qt.ClickFocus)
        self.pushButton.setStyleSheet(u"")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.username_field = QLineEdit(self.frame_2)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(240, 200, 350, 41))
        font3 = QFont()
        font3.setFamily(u"MS Sans Serif")
        font3.setPointSize(14)
        self.username_field.setFont(font3)
        self.username_field.setFocusPolicy(Qt.StrongFocus)
        self.username_field.setLayoutDirection(Qt.LeftToRight)
        self.username_field.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\n"
            "border:1px solid rgb(0, 0, 0);\n"
            ""
        )
        self.username_field.setInputMethodHints(Qt.ImhNone)
        self.password_field = QLineEdit(self.frame_2)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(240, 280, 350, 41))
        self.password_field.setFont(font3)
        self.password_field.setFocusPolicy(Qt.ClickFocus)
        self.password_field.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\n" "border:1px solid rgb(0, 0, 0);"
        )
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 621, 701))
        font4 = QFont()
        font4.setFamily(u"MS Sans Serif")
        font4.setPointSize(22)
        font4.setBold(False)
        font4.setWeight(50)
        self.label.setFont(font4)
        self.label.setFocusPolicy(Qt.ClickFocus)
        self.label.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 0);\n"
            "border-radius: 10px;"
        )
        self.label.setPixmap(QPixmap(u":/bg/res/meeting_BG.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 200, 181, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(30, 59, 81);\n"
            "\n"
            ""
        )
        self.label_2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 620, 161, 41))
        font5 = QFont()
        font5.setPointSize(15)
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n" "color: rgb(186, 186, 186);"
        )
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 50, 350, 100))
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(45)
        font6.setItalic(False)
        font6.setUnderline(True)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"color: rgb(30, 59, 81);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.password_field.raise_()
        self.username_field.raise_()
        self.label_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.username_field, self.password_field)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"Password", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Forgot Password", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"LOG IN", None)
        )
        self.label.setText("")
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"Username", None)
        )
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", u"Or Login with", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", u"User Login", None)
        )

    # retranslateUi
