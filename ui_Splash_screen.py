# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Splash_screenGUchLP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resource1_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(1280, 720)
        icon = QIcon()
        icon.addFile(u"../logo_2_rGp_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setEnabled(True)
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.28866, y1:0.295, x2:1, y2:1, stop:0 rgba(229, 9, 20, 255), stop:1 rgba(0, 0, 0, 255));\n"
"	border-radius: 20px;\n"
"\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 100, 200, 200))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setPixmap(QPixmap(u":/logo/LOGO@2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.dropShadowFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 370, 441, 40))
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 520, 1180, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"border-style: sunken\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.116, y1:0.579591, x2:1, y2:0.545, stop:0.633508 rgba(229, 9, 20, 255), stop:1 rgba(0, 0, 0, 200));\n"
"}")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.dropShadowFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 550, 300, 20))
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Scepter", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"Hey there! Welcome to the system.", None))
        self.label_3.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
    # retranslateUi

