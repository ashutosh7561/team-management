# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowYyhYUM.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.28866, y1:0.295, x2:1, y2:1, stop:0 rgba(229, 9, 20, 255), stop:1 rgba(0, 0, 0, 255));\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(450, 80, 380, 480))
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(455, 170, 141, 31))
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(600, 170, 201, 31))
        self.textEdit.setStyleSheet(u"background-color: rgb(213, 213, 213);\n"
"border-style: outset;")
        self.textEdit.setFrameShape(QFrame.StyledPanel)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(455, 230, 141, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(600, 230, 201, 31))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(213, 213, 213);\n"
"border-style: outset;")
        self.textEdit_2.setFrameShape(QFrame.StyledPanel)
        self.textEdit_2.setFrameShadow(QFrame.Sunken)
        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(600, 300, 81, 20))
        self.radioButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(700, 300, 95, 20))
        self.radioButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(455, 290, 141, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(580, 380, 121, 51))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(572, 450, 131, 28))
        font2 = QFont()
        font2.setFamily(u"MS Sans Serif")
        font2.setPointSize(8)
        font2.setItalic(True)
        font2.setUnderline(True)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(232, 232, 232);")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Manager", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login as", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
    # retranslateUi

