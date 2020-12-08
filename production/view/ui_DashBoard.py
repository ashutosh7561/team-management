# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashBoardolWHIw.ui'
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

class Ui_DashBoard(object):
    def setupUi(self, DashBoard):
        if DashBoard.objectName():
            DashBoard.setObjectName(u"DashBoard")
        DashBoard.resize(1280, 720)
        icon = QIcon()
        icon.addFile(u"logo_2_rGp_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        DashBoard.setWindowIcon(icon)
        DashBoard.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.centralwidget = QWidget(DashBoard)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(852, 480))
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(200, 720))
        self.frame_2.setMaximumSize(QSize(200, 1980))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(30, 59, 81);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 240, 150, 40))
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 290, 150, 40))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 1px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover {     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 390, 150, 40))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"border-bottom: 1px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover {     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 340, 150, 40))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 1px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover {     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 590, 150, 40))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"border-bottom: 1px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover {     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 490, 150, 40))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 1px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover {     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 440, 150, 40))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 1px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover {     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 540, 150, 40))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"border: none; \n"
"border-bottom: 1px solid rgb(230, 136, 136);\n"
"}\n"
"QPushButton:hover {     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 670, 150, 40))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"border-bottom: 1px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover {     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 125, 125))
        self.label.setPixmap(QPixmap(u":/usericon/usericon.png"))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 160, 160, 40))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"\n"
"color: rgb(230, 136, 136);")

        self.horizontalLayout.addWidget(self.frame_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(1080, 34))
        self.frame_3.setMaximumSize(QSize(2160, 34))
        self.frame_3.setStyleSheet(u"background-color: rgb(230, 136, 136);\n"
"border-radius:1px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.frame_3.setMidLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.empty = QFrame(self.frame_3)
        self.empty.setObjectName(u"empty")
        self.empty.setMinimumSize(QSize(960, 34))
        self.empty.setMaximumSize(QSize(1920, 34))
        self.empty.setFrameShape(QFrame.StyledPanel)
        self.empty.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.empty)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(120, 34))
        self.frame_11.setMaximumSize(QSize(120, 34))
        self.frame_11.setStyleSheet(u"background-color: rgb(30, 59, 81);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.max = QPushButton(self.frame_11)
        self.max.setObjectName(u"max")
        self.max.setGeometry(QRect(5, 1, 30, 30))
        sizePolicy1.setHeightForWidth(self.max.sizePolicy().hasHeightForWidth())
        self.max.setSizePolicy(sizePolicy1)
        self.max.setStyleSheet(u"QPushButton:hover{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/button/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.max.setIcon(icon1)
        self.max.setIconSize(QSize(30, 30))
        self.min = QPushButton(self.frame_11)
        self.min.setObjectName(u"min")
        self.min.setGeometry(QRect(45, 1, 30, 30))
        sizePolicy1.setHeightForWidth(self.min.sizePolicy().hasHeightForWidth())
        self.min.setSizePolicy(sizePolicy1)
        self.min.setStyleSheet(u"QPushButton:hover{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/button/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min.setIcon(icon2)
        self.min.setIconSize(QSize(30, 30))
        self.close = QPushButton(self.frame_11)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(85, 1, 30, 30))
        sizePolicy1.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy1)
        self.close.setStyleSheet(u"QPushButton:hover{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/button/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon3)
        self.close.setIconSize(QSize(30, 30))
        self.min.raise_()
        self.max.raise_()
        self.close.raise_()

        self.horizontalLayout_2.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_3)

        self.centralMainFrame = QFrame(self.centralwidget)
        self.centralMainFrame.setObjectName(u"centralMainFrame")
        sizePolicy1.setHeightForWidth(self.centralMainFrame.sizePolicy().hasHeightForWidth())
        self.centralMainFrame.setSizePolicy(sizePolicy1)
        self.centralMainFrame.setMinimumSize(QSize(1080, 686))
        self.centralMainFrame.setMaximumSize(QSize(2160, 1372))
        self.centralMainFrame.setFrameShape(QFrame.StyledPanel)
        self.centralMainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.centralMainFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralMainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1080, 686))
        self.stackedWidget.setMaximumSize(QSize(2160, 1372))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"")
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setMinimumSize(QSize(1080, 686))
        self.Dashboard.setMaximumSize(QSize(2160, 1370))
        self.gridLayout_3 = QGridLayout(self.Dashboard)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.frame_4 = QFrame(self.Dashboard)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(360, 150))
        self.frame_4.setMaximumSize(QSize(720, 300))
        self.frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 101, 31))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(16)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"color: rgb(30, 59, 81);")

        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.Dashboard)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(360, 300))
        self.frame_5.setMaximumSize(QSize(720, 600))
        self.frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 171, 31))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"color: rgb(30, 59, 81);")

        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.Dashboard)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(320, 300))
        self.frame_7.setMaximumSize(QSize(640, 700))
        self.frame_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 171, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"color: rgb(30, 59, 81);")

        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.Dashboard)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(350, 320))
        self.frame_8.setMaximumSize(QSize(700, 600))
        self.frame_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_8.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 171, 31))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"color: rgb(30, 59, 81);")

        self.verticalLayout_4.addWidget(self.frame_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.Dashboard)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(320, 150))
        self.frame_6.setMaximumSize(QSize(700, 300))
        self.frame_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 171, 31))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"color: rgb(30, 59, 81);")

        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.Dashboard)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(320, 320))
        self.frame_9.setMaximumSize(QSize(700, 640))
        self.frame_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 171, 31))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"color: rgb(30, 59, 81);")

        self.verticalLayout_3.addWidget(self.frame_9)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Dashboard)
        self.Projects = QWidget()
        self.Projects.setObjectName(u"Projects")
        self.Projects.setMinimumSize(QSize(1080, 686))
        self.Projects.setMaximumSize(QSize(2160, 1400))
        self.horizontalLayout_4 = QHBoxLayout(self.Projects)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.Projects)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(200, 200))
        self.frame.setMaximumSize(QSize(900, 900))
        self.frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 200, 30))
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"color: rgb(30, 59, 81);")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.Projects)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setMinimumSize(QSize(200, 200))
        self.frame_10.setMaximumSize(QSize(900, 900))
        self.frame_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 200, 30))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"border:none;\n"
"border-radius:0px;\n"
"color: rgb(30, 59, 81);")

        self.gridLayout.addWidget(self.frame_10, 0, 1, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.Projects)
        self.Tickets = QWidget()
        self.Tickets.setObjectName(u"Tickets")
        self.Tickets.setMinimumSize(QSize(1080, 700))
        self.Tickets.setMaximumSize(QSize(2160, 1400))
        self.frame_12 = QFrame(self.Tickets)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(140, 60, 801, 461))
        self.frame_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.pushButton_10 = QPushButton(self.frame_12)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(310, 160, 150, 50))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(14)
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.stackedWidget.addWidget(self.Tickets)
        self.Boards = QWidget()
        self.Boards.setObjectName(u"Boards")
        self.Boards.setMinimumSize(QSize(1080, 700))
        self.Boards.setMaximumSize(QSize(2160, 1400))
        self.Boards.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_13 = QFrame(self.Boards)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(170, 100, 801, 461))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.pushButton_11 = QPushButton(self.frame_13)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_11.setFont(font3)
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.stackedWidget.addWidget(self.Boards)
        self.Calendar = QWidget()
        self.Calendar.setObjectName(u"Calendar")
        self.Calendar.setMinimumSize(QSize(1080, 700))
        self.Calendar.setMaximumSize(QSize(2160, 1400))
        self.Calendar.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_14 = QFrame(self.Calendar)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(160, 100, 801, 461))
        self.frame_14.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.pushButton_12 = QPushButton(self.frame_14)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_12.setFont(font3)
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.stackedWidget.addWidget(self.Calendar)
        self.Analysis = QWidget()
        self.Analysis.setObjectName(u"Analysis")
        self.Analysis.setMinimumSize(QSize(1080, 700))
        self.Analysis.setMaximumSize(QSize(2160, 1400))
        self.Analysis.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_15 = QFrame(self.Analysis)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(170, 70, 801, 461))
        self.frame_15.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.pushButton_13 = QPushButton(self.frame_15)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.stackedWidget.addWidget(self.Analysis)
        self.Messages = QWidget()
        self.Messages.setObjectName(u"Messages")
        self.Messages.setMinimumSize(QSize(1080, 700))
        self.Messages.setMaximumSize(QSize(2160, 1400))
        self.Messages.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_16 = QFrame(self.Messages)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(150, 70, 801, 461))
        self.frame_16.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.pushButton_14 = QPushButton(self.frame_16)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_14.setFont(font3)
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.stackedWidget.addWidget(self.Messages)
        self.Worklog = QWidget()
        self.Worklog.setObjectName(u"Worklog")
        self.Worklog.setMinimumSize(QSize(1080, 700))
        self.Worklog.setMaximumSize(QSize(2160, 1400))
        self.frame_17 = QFrame(self.Worklog)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(110, 90, 801, 461))
        self.frame_17.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.pushButton_15 = QPushButton(self.frame_17)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_15.setFont(font3)
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.stackedWidget.addWidget(self.Worklog)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.Settings.setMinimumSize(QSize(1080, 700))
        self.Settings.setMaximumSize(QSize(2160, 1400))
        self.Settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_18 = QFrame(self.Settings)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(160, 90, 801, 461))
        self.frame_18.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid;\n"
"}\n"
"QFrame:hover{     \n"
"	border:2px solid rgb(230, 136, 136);\n"
" }")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.pushButton_16 = QPushButton(self.frame_18)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_16.setFont(font3)
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.stackedWidget.addWidget(self.Settings)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.centralMainFrame)


        self.horizontalLayout.addLayout(self.verticalLayout)

        DashBoard.setCentralWidget(self.centralwidget)

        self.retranslateUi(DashBoard)

        QMetaObject.connectSlotsByName(DashBoard)
    # setupUi

    def retranslateUi(self, DashBoard):
        DashBoard.setWindowTitle(QCoreApplication.translate("DashBoard", u"Scepter", None))
        self.pushButton.setText(QCoreApplication.translate("DashBoard", u"Dashboard", None))
        self.pushButton_2.setText(QCoreApplication.translate("DashBoard", u"Projects", None))
        self.pushButton_4.setText(QCoreApplication.translate("DashBoard", u"Boards", None))
        self.pushButton_3.setText(QCoreApplication.translate("DashBoard", u"Tickets", None))
        self.pushButton_8.setText(QCoreApplication.translate("DashBoard", u"Worklog", None))
        self.pushButton_6.setText(QCoreApplication.translate("DashBoard", u"Analysis", None))
        self.pushButton_5.setText(QCoreApplication.translate("DashBoard", u"Calendar", None))
        self.pushButton_7.setText(QCoreApplication.translate("DashBoard", u"Messages", None))
        self.pushButton_9.setText(QCoreApplication.translate("DashBoard", u"Settings", None))
        self.label.setText("")
        self.label_8.setText(QCoreApplication.translate("DashBoard", u"User Name", None))
        self.max.setText("")
        self.min.setText("")
        self.close.setText("")
        self.label_2.setText(QCoreApplication.translate("DashBoard", u"Projects", None))
        self.label_3.setText(QCoreApplication.translate("DashBoard", u"Progress Reports", None))
        self.label_5.setText(QCoreApplication.translate("DashBoard", u"Schedules", None))
        self.label_6.setText(QCoreApplication.translate("DashBoard", u"Files", None))
        self.label_4.setText(QCoreApplication.translate("DashBoard", u"Recent Charts", None))
        self.label_7.setText(QCoreApplication.translate("DashBoard", u"Flags", None))
        self.label_9.setText(QCoreApplication.translate("DashBoard", u"Ongoing Projects", None))
        self.label_10.setText(QCoreApplication.translate("DashBoard", u"Past Projects", None))
        self.pushButton_10.setText(QCoreApplication.translate("DashBoard", u"Tickets Page", None))
        self.pushButton_11.setText(QCoreApplication.translate("DashBoard", u"Boards Page", None))
        self.pushButton_12.setText(QCoreApplication.translate("DashBoard", u"Calendar Page", None))
        self.pushButton_13.setText(QCoreApplication.translate("DashBoard", u"Analysis Page", None))
        self.pushButton_14.setText(QCoreApplication.translate("DashBoard", u"Messages Page", None))
        self.pushButton_15.setText(QCoreApplication.translate("DashBoard", u"Worklog Page", None))
        self.pushButton_16.setText(QCoreApplication.translate("DashBoard", u"Settings", None))
    # retranslateUi

