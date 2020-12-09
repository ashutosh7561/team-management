# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Splash_screenqqVpqk.ui'
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

import view.resource1_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(782, 500)
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
"		\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(30, 59, 81, 255), stop:1 rgba(230, 136, 136, 255));\n"
"		border-radius: 5px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 411, 280))
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label.setPixmap(QPixmap(u":/logo/res/logo@4.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 430, 761, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"border-style: sunken\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(230, 136, 136);\n"
"}")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.dropShadowFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 390, 300, 20))
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.dropShadowFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 340, 311, 40))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.progressBar.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label.raise_()

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Scepter", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_4.setText(QCoreApplication.translate("SplashScreen", u"Welcome to the system", None))
    # retranslateUi

