# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashBoardplJBHL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import view.resource1_rc

class Ui_DashBoard(object):
    def setupUi(self, DashBoard):
        if not DashBoard.objectName():
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
        self.dashboard = QPushButton(self.frame_2)
        self.dashboard.setObjectName(u"dashboard")
        self.dashboard.setGeometry(QRect(20, 240, 150, 40))
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dashboard.setFont(font)
        self.dashboard.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: white;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-left: 2px solid rgb(230, 136, 136);;\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.projects = QPushButton(self.frame_2)
        self.projects.setObjectName(u"projects")
        self.projects.setGeometry(QRect(20, 340, 150, 40))
        self.projects.setFont(font)
        self.projects.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: white;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-left: 2px solid rgb(230, 136, 136);;\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.messages = QPushButton(self.frame_2)
        self.messages.setObjectName(u"messages")
        self.messages.setGeometry(QRect(20, 460, 150, 40))
        self.messages.setFont(font)
        self.messages.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: white;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-left: 2px solid rgb(230, 136, 136);;\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.settings = QPushButton(self.frame_2)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(20, 580, 150, 40))
        self.settings.setFont(font)
        self.settings.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: white;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-left: 2px solid rgb(230, 136, 136);;\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.user_avatar = QLabel(self.frame_2)
        self.user_avatar.setObjectName(u"user_avatar")
        self.user_avatar.setGeometry(QRect(40, 20, 125, 125))
        self.user_avatar.setPixmap(QPixmap(u":/usericon/res/usericon.png"))
        self.user_handle = QLabel(self.frame_2)
        self.user_handle.setObjectName(u"user_handle")
        self.user_handle.setGeometry(QRect(20, 160, 160, 40))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.user_handle.setFont(font1)
        self.user_handle.setStyleSheet(u"\n"
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
        icon1.addFile(u":/button/res/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u":/button/res/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u":/button/res/close.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 5, 20, 5)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.frame_4 = QFrame(self.Dashboard)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(320, 150))
        self.frame_4.setMaximumSize(QSize(700, 300))
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
        self.frame_5.setMinimumSize(QSize(320, 150))
        self.frame_5.setMaximumSize(QSize(700, 300))
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
        self.frame_7.setMinimumSize(QSize(320, 150))
        self.frame_7.setMaximumSize(QSize(700, 300))
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
        self.frame_8.setMinimumSize(QSize(320, 150))
        self.frame_8.setMaximumSize(QSize(700, 300))
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
        self.frame.setMaximumSize(QSize(300, 300))
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
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(29, 120, 241, 50))
        self.pushButton_3.setMinimumSize(QSize(200, 50))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: white;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-left: 2px solid rgb(230, 136, 136);;\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.Projects)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setMinimumSize(QSize(200, 200))
        self.frame_10.setMaximumSize(QSize(300, 300))
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
        self.pushButton_4 = QPushButton(self.frame_10)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 120, 200, 50))
        self.pushButton_4.setMinimumSize(QSize(200, 50))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: white;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-left: 2px solid rgb(230, 136, 136);;\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")

        self.gridLayout.addWidget(self.frame_10, 0, 1, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.Projects)
        self.Messages = QWidget()
        self.Messages.setObjectName(u"Messages")
        self.Messages.setMinimumSize(QSize(1080, 686))
        self.Messages.setMaximumSize(QSize(2160, 2058))
        self.Messages.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout_6 = QHBoxLayout(self.Messages)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.Messages)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(780, 686))
        self.stackedWidget_2.setMaximumSize(QSize(2340, 2058))
        self.welcome = QWidget()
        self.welcome.setObjectName(u"welcome")
        self.welcome.setMinimumSize(QSize(780, 686))
        self.welcome.setMaximumSize(QSize(2340, 2058))
        self.verticalLayout_8 = QVBoxLayout(self.welcome)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.welcome)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(780, 686))
        self.frame_24.setMaximumSize(QSize(2340, 2058))
        self.frame_24.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_24)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(780, 150))
        self.frame_25.setMaximumSize(QSize(2340, 450))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.label_20 = QLabel(self.frame_25)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(440, 110, 20, 20))
        self.label_20.setMinimumSize(QSize(20, 20))
        self.label_20.setMaximumSize(QSize(60, 60))
        self.label_20.setStyleSheet(u"border-radius:8px;\n"
"background-color: rgb(0, 255, 0);\n"
"border: 2px solid rgb(255,255,255);")
        self.pushButton_19 = QPushButton(self.frame_25)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(315, 0, 150, 150))
        self.pushButton_19.setMinimumSize(QSize(150, 150))
        self.pushButton_19.setMaximumSize(QSize(450, 450))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_19.setFont(font3)
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border-radius:75px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(152, 199, 255);\n"
"}\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_19.raise_()
        self.label_20.raise_()

        self.verticalLayout_7.addWidget(self.frame_25, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(780, 150))
        self.frame_26.setMaximumSize(QSize(2340, 450))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_26)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 20, 0, 20)
        self.label_21 = QLabel(self.frame_26)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(780, 51))
        self.label_21.setMaximumSize(QSize(2340, 153))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(28)
        self.label_21.setFont(font4)
        self.label_21.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_26)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(780, 51))
        self.label_22.setMaximumSize(QSize(2340, 153))
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(28)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_22.setFont(font5)
        self.label_22.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.label_22)


        self.verticalLayout_7.addWidget(self.frame_26)

        self.label_25 = QLabel(self.frame_24)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(780, 100))
        self.label_25.setMaximumSize(QSize(2340, 300))
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(10)
        self.label_25.setFont(font6)
        self.label_25.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_7.addWidget(self.label_25)

        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(780, 246))
        self.frame_27.setMaximumSize(QSize(2340, 240))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_7.setSpacing(86)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(80, 100, 80, 150)
        self.pushButton_20 = QPushButton(self.frame_27)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy1.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy1)
        self.pushButton_20.setMinimumSize(QSize(150, 51))
        self.pushButton_20.setMaximumSize(QSize(450, 153))
        self.pushButton_20.setFont(font3)
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 59, 81);\n"
"}\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.frame_27)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy1.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy1)
        self.pushButton_21.setMinimumSize(QSize(150, 51))
        self.pushButton_21.setMaximumSize(QSize(450, 153))
        self.pushButton_21.setFont(font3)
        self.pushButton_21.setStyleSheet(u"QPushButton{\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 59, 81);\n"
"}\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_27)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy1.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy1)
        self.pushButton_22.setMinimumSize(QSize(150, 51))
        self.pushButton_22.setMaximumSize(QSize(450, 153))
        self.pushButton_22.setFont(font3)
        self.pushButton_22.setStyleSheet(u"QPushButton{\n"
"border-radius:25px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 59, 81);\n"
"}\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_22)


        self.verticalLayout_7.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_24)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(780, 40))
        self.frame_28.setMaximumSize(QSize(2340, 900))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_28)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_28)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(780, 20))
        self.label_23.setMaximumSize(QSize(2340, 60))
        self.label_23.setFont(font6)
        self.label_23.setStyleSheet(u"\n"
"color: rgb(230, 136, 136);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_28)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(780, 20))
        self.label_24.setMaximumSize(QSize(2340, 60))
        font7 = QFont()
        font7.setFamily(u"Calibri")
        font7.setPointSize(10)
        font7.setUnderline(True)
        self.label_24.setFont(font7)
        self.label_24.setStyleSheet(u"\n"
"color: rgb(230, 136, 136);")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_24)


        self.verticalLayout_7.addWidget(self.frame_28)


        self.verticalLayout_8.addWidget(self.frame_24)

        self.stackedWidget_2.addWidget(self.welcome)
        self.member1 = QWidget()
        self.member1.setObjectName(u"member1")
        self.member1.setMinimumSize(QSize(780, 686))
        self.member1.setMaximumSize(QSize(2340, 2058))
        self.verticalLayout_10 = QVBoxLayout(self.member1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.member1)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(780, 686))
        self.frame_21.setMaximumSize(QSize(2430, 2058))
        self.frame_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_21)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(760, 80))
        self.frame_22.setMaximumSize(QSize(2280, 80))
        self.frame_22.setStyleSheet(u"border:none;\n"
"border-bottom: 2px solid rgb(238, 238, 238);")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_22)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 50, 131, 20))
        self.label_18.setMinimumSize(QSize(131, 20))
        self.label_18.setMaximumSize(QSize(393, 60))
        self.label_18.setStyleSheet(u"border:none;")
        self.label_17 = QLabel(self.frame_22)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 10, 171, 40))
        self.label_17.setMinimumSize(QSize(171, 40))
        self.label_17.setMaximumSize(QSize(513, 120))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"border:none;")

        self.verticalLayout_9.addWidget(self.frame_22)

        self.frame_29 = QFrame(self.frame_21)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(760, 520))
        self.frame_29.setMaximumSize(QSize(2280, 1560))
        self.frame_29.setStyleSheet(u"border:none;\n"
"border-bottom: 2px solid rgb(225, 225, 225);\n"
"border-radius: 5px;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_29)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(780, 86))
        self.frame_23.setMaximumSize(QSize(2280, 86))
        self.frame_23.setStyleSheet(u"border:none;\n"
"border-bottom: 2px solid rgb(225, 225, 225);\n"
"border-radius: 5px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_23)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 0, 760, 86))
        self.label_19.setMinimumSize(QSize(760, 86))
        self.label_19.setMaximumSize(QSize(2280, 86))
        self.label_19.setStyleSheet(u"border:none;")

        self.verticalLayout_9.addWidget(self.frame_23)


        self.verticalLayout_10.addWidget(self.frame_21)

        self.stackedWidget_2.addWidget(self.member1)

        self.horizontalLayout_6.addWidget(self.stackedWidget_2)

        self.frame_16 = QFrame(self.Messages)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(300, 686))
        self.frame_16.setMaximumSize(QSize(900, 2058))
        self.frame_16.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid rgb(236,236,236);\n"
"}\n"
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(10, 20, 280, 40))
        self.frame_19.setStyleSheet(u"border:1px solid rgb(236,236,236);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.frame_19)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy1.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy1)
        self.pushButton_14.setMinimumSize(QSize(50, 20))
        font8 = QFont()
        font8.setFamily(u"Calibri")
        font8.setPointSize(8)
        self.pushButton_14.setFont(font8)
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:3px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_14)

        self.pushButton_18 = QPushButton(self.frame_19)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy1.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy1)
        self.pushButton_18.setMinimumSize(QSize(50, 20))
        self.pushButton_18.setFont(font8)
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:3px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_18)

        self.pushButton_17 = QPushButton(self.frame_19)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy1.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy1)
        self.pushButton_17.setMinimumSize(QSize(50, 20))
        self.pushButton_17.setFont(font8)
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:3px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_17)

        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(10, 70, 281, 591))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.pushButton_23 = QPushButton(self.frame_20)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(40, 30, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy1)
        self.pushButton_23.setMinimumSize(QSize(50, 20))
        font9 = QFont()
        font9.setFamily(u"Calibri")
        font9.setPointSize(18)
        font9.setBold(True)
        font9.setWeight(75)
        self.pushButton_23.setFont(font9)
        self.pushButton_23.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.pushButton_24 = QPushButton(self.frame_20)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(40, 90, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy1)
        self.pushButton_24.setMinimumSize(QSize(50, 20))
        self.pushButton_24.setFont(font9)
        self.pushButton_24.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.pushButton_25 = QPushButton(self.frame_20)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(40, 140, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy1)
        self.pushButton_25.setMinimumSize(QSize(50, 20))
        self.pushButton_25.setFont(font9)
        self.pushButton_25.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.pushButton_26 = QPushButton(self.frame_20)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(40, 190, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy1)
        self.pushButton_26.setMinimumSize(QSize(50, 20))
        self.pushButton_26.setFont(font9)
        self.pushButton_26.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.pushButton_27 = QPushButton(self.frame_20)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(40, 300, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy1)
        self.pushButton_27.setMinimumSize(QSize(50, 20))
        self.pushButton_27.setFont(font9)
        self.pushButton_27.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.pushButton_28 = QPushButton(self.frame_20)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(40, 240, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy1)
        self.pushButton_28.setMinimumSize(QSize(50, 20))
        self.pushButton_28.setFont(font9)
        self.pushButton_28.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.pushButton_29 = QPushButton(self.frame_20)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(40, 350, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy1)
        self.pushButton_29.setMinimumSize(QSize(50, 20))
        self.pushButton_29.setFont(font9)
        self.pushButton_29.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.pushButton_30 = QPushButton(self.frame_20)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(40, 530, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy1)
        self.pushButton_30.setMinimumSize(QSize(50, 20))
        self.pushButton_30.setFont(font9)
        self.pushButton_30.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.pushButton_31 = QPushButton(self.frame_20)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(40, 470, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy1)
        self.pushButton_31.setMinimumSize(QSize(50, 20))
        self.pushButton_31.setFont(font9)
        self.pushButton_31.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")
        self.pushButton_32 = QPushButton(self.frame_20)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setGeometry(QRect(40, 410, 200, 40))
        sizePolicy1.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy1)
        self.pushButton_32.setMinimumSize(QSize(50, 20))
        self.pushButton_32.setFont(font9)
        self.pushButton_32.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(30, 59, 81);	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius:15px;\n"
"	border-bottom: 2px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgb(230, 136, 136);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid  rgb(30, 59, 81);	\n"
"}")

        self.horizontalLayout_6.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.Messages)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.Settings.setMinimumSize(QSize(1080, 686))
        self.Settings.setMaximumSize(QSize(2160, 1400))
        self.Settings.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout_13 = QHBoxLayout(self.Settings)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.Settings)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(880, 686))
        self.stackedWidget_3.setMaximumSize(QSize(2640, 2058))
        self.UserSettings = QWidget()
        self.UserSettings.setObjectName(u"UserSettings")
        self.UserSettings.setMinimumSize(QSize(880, 686))
        self.UserSettings.setMaximumSize(QSize(2640, 2058))
        self.stackedWidget_4 = QStackedWidget(self.UserSettings)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setGeometry(QRect(0, 0, 880, 686))
        self.stackedWidget_4.setMinimumSize(QSize(880, 686))
        self.stackedWidget_4.setMaximumSize(QSize(2640, 2058))
        self.myAccount = QWidget()
        self.myAccount.setObjectName(u"myAccount")
        self.frame_18 = QFrame(self.myAccount)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(0, 0, 880, 686))
        self.frame_18.setMinimumSize(QSize(880, 686))
        self.frame_18.setMaximumSize(QSize(880, 686))
        self.frame_18.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_34 = QFrame(self.frame_18)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(0, 0, 880, 343))
        self.frame_34.setMinimumSize(QSize(880, 343))
        self.frame_34.setMaximumSize(QSize(880, 343))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_34)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 880, 50))
        self.label_11.setMinimumSize(QSize(880, 50))
        self.label_11.setMaximumSize(QSize(880, 50))
        font10 = QFont()
        font10.setFamily(u"Calibri")
        font10.setPointSize(20)
        self.label_11.setFont(font10)
        self.label_11.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 150);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(0, 50, 880, 293))
        self.frame_36.setMinimumSize(QSize(880, 293))
        self.frame_36.setMaximumSize(QSize(880, 293))
        self.frame_36.setStyleSheet(u"\n"
"background-color: rgba(30, 59, 81, 50);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(175, 16, 530, 260))
        self.frame_37.setMinimumSize(QSize(530, 260))
        self.frame_37.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_37)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 40, 160, 50))
        self.label_12.setMinimumSize(QSize(160, 50))
        self.label_12.setMaximumSize(QSize(160, 50))
        font11 = QFont()
        font11.setFamily(u"Calibri")
        font11.setPointSize(15)
        font11.setBold(True)
        font11.setWeight(75)
        self.label_12.setFont(font11)
        self.label_12.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_14 = QLabel(self.frame_37)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 180, 160, 50))
        self.label_14.setMinimumSize(QSize(160, 50))
        self.label_14.setMaximumSize(QSize(160, 50))
        self.label_14.setFont(font11)
        self.label_14.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_13 = QLabel(self.frame_37)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 110, 160, 50))
        self.label_13.setMinimumSize(QSize(160, 50))
        self.label_13.setMaximumSize(QSize(160, 50))
        self.label_13.setFont(font11)
        self.label_13.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_16 = QLabel(self.frame_37)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(200, 40, 160, 50))
        self.label_16.setMinimumSize(QSize(160, 50))
        self.label_16.setMaximumSize(QSize(160, 50))
        font12 = QFont()
        font12.setFamily(u"Calibri Light")
        font12.setPointSize(10)
        self.label_16.setFont(font12)
        self.label_16.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"	border: none;	\n"
"\n"
" }\n"
"")
        self.label_26 = QLabel(self.frame_37)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(200, 110, 160, 50))
        self.label_26.setMinimumSize(QSize(160, 50))
        self.label_26.setMaximumSize(QSize(160, 50))
        self.label_26.setFont(font12)
        self.label_26.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"	border: none;	\n"
"\n"
" }\n"
"")
        self.label_27 = QLabel(self.frame_37)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(200, 180, 160, 50))
        self.label_27.setMinimumSize(QSize(160, 50))
        self.label_27.setMaximumSize(QSize(160, 50))
        self.label_27.setFont(font12)
        self.label_27.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"	border: none;	\n"
"\n"
" }\n"
"")
        self.pushButton_50 = QPushButton(self.frame_37)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setGeometry(QRect(460, 40, 50, 50))
        self.pushButton_50.setMinimumSize(QSize(50, 50))
        self.pushButton_50.setMaximumSize(QSize(50, 50))
        font13 = QFont()
        font13.setFamily(u"Calibri")
        font13.setPointSize(10)
        font13.setBold(False)
        font13.setWeight(50)
        self.pushButton_50.setFont(font13)
        self.pushButton_50.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_51 = QPushButton(self.frame_37)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setGeometry(QRect(460, 110, 50, 50))
        self.pushButton_51.setMinimumSize(QSize(50, 50))
        self.pushButton_51.setMaximumSize(QSize(50, 50))
        self.pushButton_51.setFont(font13)
        self.pushButton_51.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_52 = QPushButton(self.frame_37)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setGeometry(QRect(460, 180, 50, 50))
        self.pushButton_52.setMinimumSize(QSize(50, 50))
        self.pushButton_52.setMaximumSize(QSize(50, 50))
        self.pushButton_52.setFont(font13)
        self.pushButton_52.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.frame_35 = QFrame(self.frame_18)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(0, 393, 880, 293))
        self.frame_35.setMinimumSize(QSize(880, 293))
        self.frame_35.setMaximumSize(QSize(880, 293))
        self.frame_35.setStyleSheet(u"\n"
"background-color: rgba(30, 59, 81, 50);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.frame_38 = QFrame(self.frame_35)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setGeometry(QRect(170, 10, 530, 260))
        self.frame_38.setMinimumSize(QSize(530, 260))
        self.frame_38.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_38)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 40, 250, 50))
        self.label_28.setMinimumSize(QSize(250, 50))
        self.label_28.setMaximumSize(QSize(250, 50))
        font14 = QFont()
        font14.setFamily(u"Calibri")
        font14.setPointSize(15)
        self.label_28.setFont(font14)
        self.label_28.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_30 = QLabel(self.frame_38)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 110, 250, 50))
        self.label_30.setMinimumSize(QSize(250, 50))
        self.label_30.setMaximumSize(QSize(250, 50))
        self.label_30.setFont(font14)
        self.label_30.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_53 = QPushButton(self.frame_38)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setGeometry(QRect(134, 180, 250, 50))
        self.pushButton_53.setMinimumSize(QSize(250, 50))
        self.pushButton_53.setMaximumSize(QSize(250, 50))
        self.pushButton_53.setFont(font13)
        self.pushButton_53.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(220, 220, 220);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.lineEdit = QLineEdit(self.frame_38)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 40, 240, 50))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(200, 200, 200);\n"
" }\n"
"QLineEdit:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }")
        self.lineEdit_2 = QLineEdit(self.frame_38)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(280, 110, 240, 50))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(200, 200, 200);\n"
" }\n"
"QLineEdit:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }")
        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 343, 880, 50))
        self.label_15.setMinimumSize(QSize(880, 50))
        self.label_15.setMaximumSize(QSize(880, 50))
        self.label_15.setFont(font10)
        self.label_15.setStyleSheet(u"QLabel{\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);\n"
"	background-color: rgba(30, 59, 81, 150);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.stackedWidget_4.addWidget(self.myAccount)
        self.privacySafety = QWidget()
        self.privacySafety.setObjectName(u"privacySafety")
        self.frame_40 = QFrame(self.privacySafety)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setGeometry(QRect(0, 0, 880, 686))
        self.frame_40.setMinimumSize(QSize(880, 686))
        self.frame_40.setMaximumSize(QSize(880, 686))
        self.frame_40.setStyleSheet(u"background-color: rgba(30, 59, 81, 50);")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.frame_44 = QFrame(self.frame_40)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setGeometry(QRect(50, 100, 781, 531))
        self.frame_44.setMinimumSize(QSize(530, 260))
        self.frame_44.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.label_38 = QLabel(self.frame_44)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 40, 400, 50))
        self.label_38.setMinimumSize(QSize(400, 50))
        self.label_38.setMaximumSize(QSize(400, 50))
        self.label_38.setFont(font11)
        self.label_38.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_39 = QLabel(self.frame_44)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 180, 400, 50))
        self.label_39.setMinimumSize(QSize(400, 50))
        self.label_39.setMaximumSize(QSize(400, 50))
        self.label_39.setFont(font11)
        self.label_39.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_40 = QLabel(self.frame_44)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 110, 400, 50))
        self.label_40.setMinimumSize(QSize(400, 50))
        self.label_40.setMaximumSize(QSize(400, 50))
        self.label_40.setFont(font11)
        self.label_40.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_57 = QPushButton(self.frame_44)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setGeometry(QRect(700, 40, 50, 50))
        self.pushButton_57.setMinimumSize(QSize(50, 50))
        self.pushButton_57.setMaximumSize(QSize(50, 50))
        self.pushButton_57.setFont(font13)
        self.pushButton_57.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_58 = QPushButton(self.frame_44)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setGeometry(QRect(700, 110, 50, 50))
        self.pushButton_58.setMinimumSize(QSize(50, 50))
        self.pushButton_58.setMaximumSize(QSize(50, 50))
        self.pushButton_58.setFont(font13)
        self.pushButton_58.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_59 = QPushButton(self.frame_44)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setGeometry(QRect(700, 180, 50, 50))
        self.pushButton_59.setMinimumSize(QSize(50, 50))
        self.pushButton_59.setMaximumSize(QSize(50, 50))
        self.pushButton_59.setFont(font13)
        self.pushButton_59.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label_37 = QLabel(self.frame_40)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(0, 0, 880, 50))
        self.label_37.setMinimumSize(QSize(880, 50))
        self.label_37.setMaximumSize(QSize(880, 50))
        self.label_37.setFont(font10)
        self.label_37.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 120);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_37.setAlignment(Qt.AlignCenter)
        self.label_37.raise_()
        self.frame_44.raise_()
        self.stackedWidget_4.addWidget(self.privacySafety)
        self.backupRestore = QWidget()
        self.backupRestore.setObjectName(u"backupRestore")
        self.frame_41 = QFrame(self.backupRestore)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setGeometry(QRect(0, 0, 880, 686))
        self.frame_41.setMinimumSize(QSize(880, 686))
        self.frame_41.setMaximumSize(QSize(880, 686))
        self.frame_41.setStyleSheet(u"background-color: rgba(30, 59, 81, 50);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.frame_45 = QFrame(self.frame_41)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setGeometry(QRect(50, 100, 781, 531))
        self.frame_45.setMinimumSize(QSize(530, 260))
        self.frame_45.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.label_41 = QLabel(self.frame_45)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 40, 400, 50))
        self.label_41.setMinimumSize(QSize(400, 50))
        self.label_41.setMaximumSize(QSize(400, 50))
        self.label_41.setFont(font11)
        self.label_41.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_42 = QLabel(self.frame_45)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 180, 400, 50))
        self.label_42.setMinimumSize(QSize(400, 50))
        self.label_42.setMaximumSize(QSize(400, 50))
        self.label_42.setFont(font11)
        self.label_42.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_43 = QLabel(self.frame_45)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 110, 400, 50))
        self.label_43.setMinimumSize(QSize(400, 50))
        self.label_43.setMaximumSize(QSize(400, 50))
        self.label_43.setFont(font11)
        self.label_43.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_60 = QPushButton(self.frame_45)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setGeometry(QRect(700, 40, 50, 50))
        self.pushButton_60.setMinimumSize(QSize(50, 50))
        self.pushButton_60.setMaximumSize(QSize(50, 50))
        self.pushButton_60.setFont(font13)
        self.pushButton_60.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_61 = QPushButton(self.frame_45)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setGeometry(QRect(700, 110, 50, 50))
        self.pushButton_61.setMinimumSize(QSize(50, 50))
        self.pushButton_61.setMaximumSize(QSize(50, 50))
        self.pushButton_61.setFont(font13)
        self.pushButton_61.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_62 = QPushButton(self.frame_45)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setGeometry(QRect(700, 180, 50, 50))
        self.pushButton_62.setMinimumSize(QSize(50, 50))
        self.pushButton_62.setMaximumSize(QSize(50, 50))
        self.pushButton_62.setFont(font13)
        self.pushButton_62.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label_44 = QLabel(self.frame_41)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(0, 0, 880, 50))
        self.label_44.setMinimumSize(QSize(880, 50))
        self.label_44.setMaximumSize(QSize(880, 50))
        self.label_44.setFont(font10)
        self.label_44.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 120);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_44.setAlignment(Qt.AlignCenter)
        self.stackedWidget_4.addWidget(self.backupRestore)
        self.addAccount = QWidget()
        self.addAccount.setObjectName(u"addAccount")
        self.frame_42 = QFrame(self.addAccount)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setGeometry(QRect(0, 0, 880, 686))
        self.frame_42.setMinimumSize(QSize(880, 686))
        self.frame_42.setMaximumSize(QSize(880, 686))
        self.frame_42.setStyleSheet(u"background-color: rgba(30, 59, 81, 50);")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.frame_46 = QFrame(self.frame_42)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setGeometry(QRect(50, 100, 781, 531))
        self.frame_46.setMinimumSize(QSize(530, 260))
        self.frame_46.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.label_45 = QLabel(self.frame_46)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 40, 400, 50))
        self.label_45.setMinimumSize(QSize(400, 50))
        self.label_45.setMaximumSize(QSize(400, 50))
        self.label_45.setFont(font11)
        self.label_45.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_46 = QLabel(self.frame_46)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 180, 400, 50))
        self.label_46.setMinimumSize(QSize(400, 50))
        self.label_46.setMaximumSize(QSize(400, 50))
        self.label_46.setFont(font11)
        self.label_46.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_47 = QLabel(self.frame_46)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, 110, 400, 50))
        self.label_47.setMinimumSize(QSize(400, 50))
        self.label_47.setMaximumSize(QSize(400, 50))
        self.label_47.setFont(font11)
        self.label_47.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_63 = QPushButton(self.frame_46)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setGeometry(QRect(700, 40, 50, 50))
        self.pushButton_63.setMinimumSize(QSize(50, 50))
        self.pushButton_63.setMaximumSize(QSize(50, 50))
        self.pushButton_63.setFont(font13)
        self.pushButton_63.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_64 = QPushButton(self.frame_46)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setGeometry(QRect(700, 110, 50, 50))
        self.pushButton_64.setMinimumSize(QSize(50, 50))
        self.pushButton_64.setMaximumSize(QSize(50, 50))
        self.pushButton_64.setFont(font13)
        self.pushButton_64.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_65 = QPushButton(self.frame_46)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setGeometry(QRect(700, 180, 50, 50))
        self.pushButton_65.setMinimumSize(QSize(50, 50))
        self.pushButton_65.setMaximumSize(QSize(50, 50))
        self.pushButton_65.setFont(font13)
        self.pushButton_65.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label_48 = QLabel(self.frame_42)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(0, 0, 880, 50))
        self.label_48.setMinimumSize(QSize(880, 50))
        self.label_48.setMaximumSize(QSize(880, 50))
        self.label_48.setFont(font10)
        self.label_48.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 120);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_48.setAlignment(Qt.AlignCenter)
        self.stackedWidget_4.addWidget(self.addAccount)
        self.stackedWidget_3.addWidget(self.UserSettings)
        self.AppSettings = QWidget()
        self.AppSettings.setObjectName(u"AppSettings")
        self.AppSettings.setMinimumSize(QSize(880, 686))
        self.AppSettings.setMaximumSize(QSize(2640, 2058))
        self.stackedWidget_5 = QStackedWidget(self.AppSettings)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.stackedWidget_5.setGeometry(QRect(0, 0, 880, 686))
        self.stackedWidget_5.setMinimumSize(QSize(880, 686))
        self.stackedWidget_5.setMaximumSize(QSize(2640, 2058))
        self.Appearance = QWidget()
        self.Appearance.setObjectName(u"Appearance")
        self.frame_43 = QFrame(self.Appearance)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(0, 0, 880, 686))
        self.frame_43.setMinimumSize(QSize(880, 686))
        self.frame_43.setMaximumSize(QSize(880, 686))
        self.frame_43.setStyleSheet(u"background-color: rgba(30, 59, 81, 50);")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.frame_47 = QFrame(self.frame_43)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setGeometry(QRect(50, 100, 781, 531))
        self.frame_47.setMinimumSize(QSize(530, 260))
        self.frame_47.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.label_49 = QLabel(self.frame_47)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(10, 40, 400, 50))
        self.label_49.setMinimumSize(QSize(400, 50))
        self.label_49.setMaximumSize(QSize(400, 50))
        self.label_49.setFont(font11)
        self.label_49.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_50 = QLabel(self.frame_47)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 180, 400, 50))
        self.label_50.setMinimumSize(QSize(400, 50))
        self.label_50.setMaximumSize(QSize(400, 50))
        self.label_50.setFont(font11)
        self.label_50.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_51 = QLabel(self.frame_47)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(10, 110, 400, 50))
        self.label_51.setMinimumSize(QSize(400, 50))
        self.label_51.setMaximumSize(QSize(400, 50))
        self.label_51.setFont(font11)
        self.label_51.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_66 = QPushButton(self.frame_47)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setGeometry(QRect(700, 40, 50, 50))
        self.pushButton_66.setMinimumSize(QSize(50, 50))
        self.pushButton_66.setMaximumSize(QSize(50, 50))
        self.pushButton_66.setFont(font13)
        self.pushButton_66.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_67 = QPushButton(self.frame_47)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setGeometry(QRect(700, 110, 50, 50))
        self.pushButton_67.setMinimumSize(QSize(50, 50))
        self.pushButton_67.setMaximumSize(QSize(50, 50))
        self.pushButton_67.setFont(font13)
        self.pushButton_67.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_68 = QPushButton(self.frame_47)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setGeometry(QRect(700, 180, 50, 50))
        self.pushButton_68.setMinimumSize(QSize(50, 50))
        self.pushButton_68.setMaximumSize(QSize(50, 50))
        self.pushButton_68.setFont(font13)
        self.pushButton_68.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label_52 = QLabel(self.frame_43)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(0, 0, 880, 50))
        self.label_52.setMinimumSize(QSize(880, 50))
        self.label_52.setMaximumSize(QSize(880, 50))
        self.label_52.setFont(font10)
        self.label_52.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 120);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_52.setAlignment(Qt.AlignCenter)
        self.stackedWidget_5.addWidget(self.Appearance)
        self.Notification = QWidget()
        self.Notification.setObjectName(u"Notification")
        self.frame_48 = QFrame(self.Notification)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setGeometry(QRect(0, 0, 880, 686))
        self.frame_48.setMinimumSize(QSize(880, 686))
        self.frame_48.setMaximumSize(QSize(880, 686))
        self.frame_48.setStyleSheet(u"background-color: rgba(30, 59, 81, 50);")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setGeometry(QRect(50, 100, 781, 531))
        self.frame_49.setMinimumSize(QSize(530, 260))
        self.frame_49.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.label_53 = QLabel(self.frame_49)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(10, 40, 400, 50))
        self.label_53.setMinimumSize(QSize(400, 50))
        self.label_53.setMaximumSize(QSize(400, 50))
        self.label_53.setFont(font11)
        self.label_53.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_54 = QLabel(self.frame_49)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(10, 180, 400, 50))
        self.label_54.setMinimumSize(QSize(400, 50))
        self.label_54.setMaximumSize(QSize(400, 50))
        self.label_54.setFont(font11)
        self.label_54.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_55 = QLabel(self.frame_49)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(10, 110, 400, 50))
        self.label_55.setMinimumSize(QSize(400, 50))
        self.label_55.setMaximumSize(QSize(400, 50))
        self.label_55.setFont(font11)
        self.label_55.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_69 = QPushButton(self.frame_49)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setGeometry(QRect(700, 40, 50, 50))
        self.pushButton_69.setMinimumSize(QSize(50, 50))
        self.pushButton_69.setMaximumSize(QSize(50, 50))
        self.pushButton_69.setFont(font13)
        self.pushButton_69.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_70 = QPushButton(self.frame_49)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setGeometry(QRect(700, 110, 50, 50))
        self.pushButton_70.setMinimumSize(QSize(50, 50))
        self.pushButton_70.setMaximumSize(QSize(50, 50))
        self.pushButton_70.setFont(font13)
        self.pushButton_70.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_71 = QPushButton(self.frame_49)
        self.pushButton_71.setObjectName(u"pushButton_71")
        self.pushButton_71.setGeometry(QRect(700, 180, 50, 50))
        self.pushButton_71.setMinimumSize(QSize(50, 50))
        self.pushButton_71.setMaximumSize(QSize(50, 50))
        self.pushButton_71.setFont(font13)
        self.pushButton_71.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label_56 = QLabel(self.frame_48)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(0, 0, 880, 50))
        self.label_56.setMinimumSize(QSize(880, 50))
        self.label_56.setMaximumSize(QSize(880, 50))
        self.label_56.setFont(font10)
        self.label_56.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 120);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_56.setAlignment(Qt.AlignCenter)
        self.stackedWidget_5.addWidget(self.Notification)
        self.textImages = QWidget()
        self.textImages.setObjectName(u"textImages")
        self.frame_50 = QFrame(self.textImages)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setGeometry(QRect(0, 0, 880, 686))
        self.frame_50.setMinimumSize(QSize(880, 686))
        self.frame_50.setMaximumSize(QSize(880, 686))
        self.frame_50.setStyleSheet(u"background-color: rgba(30, 59, 81, 50);")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setGeometry(QRect(50, 100, 781, 531))
        self.frame_51.setMinimumSize(QSize(530, 260))
        self.frame_51.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.label_57 = QLabel(self.frame_51)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 40, 400, 50))
        self.label_57.setMinimumSize(QSize(400, 50))
        self.label_57.setMaximumSize(QSize(400, 50))
        self.label_57.setFont(font11)
        self.label_57.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_58 = QLabel(self.frame_51)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(10, 180, 400, 50))
        self.label_58.setMinimumSize(QSize(400, 50))
        self.label_58.setMaximumSize(QSize(400, 50))
        self.label_58.setFont(font11)
        self.label_58.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_59 = QLabel(self.frame_51)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(10, 110, 400, 50))
        self.label_59.setMinimumSize(QSize(400, 50))
        self.label_59.setMaximumSize(QSize(400, 50))
        self.label_59.setFont(font11)
        self.label_59.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_72 = QPushButton(self.frame_51)
        self.pushButton_72.setObjectName(u"pushButton_72")
        self.pushButton_72.setGeometry(QRect(700, 40, 50, 50))
        self.pushButton_72.setMinimumSize(QSize(50, 50))
        self.pushButton_72.setMaximumSize(QSize(50, 50))
        self.pushButton_72.setFont(font13)
        self.pushButton_72.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_73 = QPushButton(self.frame_51)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setGeometry(QRect(700, 110, 50, 50))
        self.pushButton_73.setMinimumSize(QSize(50, 50))
        self.pushButton_73.setMaximumSize(QSize(50, 50))
        self.pushButton_73.setFont(font13)
        self.pushButton_73.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_74 = QPushButton(self.frame_51)
        self.pushButton_74.setObjectName(u"pushButton_74")
        self.pushButton_74.setGeometry(QRect(700, 180, 50, 50))
        self.pushButton_74.setMinimumSize(QSize(50, 50))
        self.pushButton_74.setMaximumSize(QSize(50, 50))
        self.pushButton_74.setFont(font13)
        self.pushButton_74.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label_60 = QLabel(self.frame_50)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(0, 0, 880, 50))
        self.label_60.setMinimumSize(QSize(880, 50))
        self.label_60.setMaximumSize(QSize(880, 50))
        self.label_60.setFont(font10)
        self.label_60.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 120);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_60.setAlignment(Qt.AlignCenter)
        self.stackedWidget_5.addWidget(self.textImages)
        self.Performance = QWidget()
        self.Performance.setObjectName(u"Performance")
        self.frame_52 = QFrame(self.Performance)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setGeometry(QRect(0, 0, 880, 686))
        self.frame_52.setMinimumSize(QSize(880, 686))
        self.frame_52.setMaximumSize(QSize(880, 686))
        self.frame_52.setStyleSheet(u"background-color: rgba(30, 59, 81, 50);")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setGeometry(QRect(50, 100, 781, 531))
        self.frame_53.setMinimumSize(QSize(530, 260))
        self.frame_53.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.label_61 = QLabel(self.frame_53)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(10, 40, 400, 50))
        self.label_61.setMinimumSize(QSize(400, 50))
        self.label_61.setMaximumSize(QSize(400, 50))
        self.label_61.setFont(font11)
        self.label_61.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_62 = QLabel(self.frame_53)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(10, 180, 400, 50))
        self.label_62.setMinimumSize(QSize(400, 50))
        self.label_62.setMaximumSize(QSize(400, 50))
        self.label_62.setFont(font11)
        self.label_62.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_63 = QLabel(self.frame_53)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(10, 110, 400, 50))
        self.label_63.setMinimumSize(QSize(400, 50))
        self.label_63.setMaximumSize(QSize(400, 50))
        self.label_63.setFont(font11)
        self.label_63.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_75 = QPushButton(self.frame_53)
        self.pushButton_75.setObjectName(u"pushButton_75")
        self.pushButton_75.setGeometry(QRect(700, 40, 50, 50))
        self.pushButton_75.setMinimumSize(QSize(50, 50))
        self.pushButton_75.setMaximumSize(QSize(50, 50))
        self.pushButton_75.setFont(font13)
        self.pushButton_75.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_76 = QPushButton(self.frame_53)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setGeometry(QRect(700, 110, 50, 50))
        self.pushButton_76.setMinimumSize(QSize(50, 50))
        self.pushButton_76.setMaximumSize(QSize(50, 50))
        self.pushButton_76.setFont(font13)
        self.pushButton_76.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_77 = QPushButton(self.frame_53)
        self.pushButton_77.setObjectName(u"pushButton_77")
        self.pushButton_77.setGeometry(QRect(700, 180, 50, 50))
        self.pushButton_77.setMinimumSize(QSize(50, 50))
        self.pushButton_77.setMaximumSize(QSize(50, 50))
        self.pushButton_77.setFont(font13)
        self.pushButton_77.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label_64 = QLabel(self.frame_52)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(0, 0, 880, 50))
        self.label_64.setMinimumSize(QSize(880, 50))
        self.label_64.setMaximumSize(QSize(880, 50))
        self.label_64.setFont(font10)
        self.label_64.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 120);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_64.setAlignment(Qt.AlignCenter)
        self.stackedWidget_5.addWidget(self.Performance)
        self.Language = QWidget()
        self.Language.setObjectName(u"Language")
        self.frame_54 = QFrame(self.Language)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setGeometry(QRect(0, 0, 880, 686))
        self.frame_54.setMinimumSize(QSize(880, 686))
        self.frame_54.setMaximumSize(QSize(880, 686))
        self.frame_54.setStyleSheet(u"background-color: rgba(30, 59, 81, 50);")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setGeometry(QRect(50, 100, 781, 531))
        self.frame_55.setMinimumSize(QSize(530, 260))
        self.frame_55.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.label_65 = QLabel(self.frame_55)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(10, 40, 400, 50))
        self.label_65.setMinimumSize(QSize(400, 50))
        self.label_65.setMaximumSize(QSize(400, 50))
        self.label_65.setFont(font11)
        self.label_65.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_66 = QLabel(self.frame_55)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(10, 180, 400, 50))
        self.label_66.setMinimumSize(QSize(400, 50))
        self.label_66.setMaximumSize(QSize(400, 50))
        self.label_66.setFont(font11)
        self.label_66.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_67 = QLabel(self.frame_55)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(10, 110, 400, 50))
        self.label_67.setMinimumSize(QSize(400, 50))
        self.label_67.setMaximumSize(QSize(400, 50))
        self.label_67.setFont(font11)
        self.label_67.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_78 = QPushButton(self.frame_55)
        self.pushButton_78.setObjectName(u"pushButton_78")
        self.pushButton_78.setGeometry(QRect(700, 40, 50, 50))
        self.pushButton_78.setMinimumSize(QSize(50, 50))
        self.pushButton_78.setMaximumSize(QSize(50, 50))
        self.pushButton_78.setFont(font13)
        self.pushButton_78.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_79 = QPushButton(self.frame_55)
        self.pushButton_79.setObjectName(u"pushButton_79")
        self.pushButton_79.setGeometry(QRect(700, 110, 50, 50))
        self.pushButton_79.setMinimumSize(QSize(50, 50))
        self.pushButton_79.setMaximumSize(QSize(50, 50))
        self.pushButton_79.setFont(font13)
        self.pushButton_79.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_80 = QPushButton(self.frame_55)
        self.pushButton_80.setObjectName(u"pushButton_80")
        self.pushButton_80.setGeometry(QRect(700, 180, 50, 50))
        self.pushButton_80.setMinimumSize(QSize(50, 50))
        self.pushButton_80.setMaximumSize(QSize(50, 50))
        self.pushButton_80.setFont(font13)
        self.pushButton_80.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label_68 = QLabel(self.frame_54)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(0, 0, 880, 50))
        self.label_68.setMinimumSize(QSize(880, 50))
        self.label_68.setMaximumSize(QSize(880, 50))
        self.label_68.setFont(font10)
        self.label_68.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 120);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_68.setAlignment(Qt.AlignCenter)
        self.stackedWidget_5.addWidget(self.Language)
        self.versionUpdates = QWidget()
        self.versionUpdates.setObjectName(u"versionUpdates")
        self.frame_56 = QFrame(self.versionUpdates)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setGeometry(QRect(0, 0, 880, 686))
        self.frame_56.setMinimumSize(QSize(880, 686))
        self.frame_56.setMaximumSize(QSize(880, 686))
        self.frame_56.setStyleSheet(u"background-color: rgba(30, 59, 81, 50);")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setGeometry(QRect(50, 100, 781, 531))
        self.frame_57.setMinimumSize(QSize(530, 260))
        self.frame_57.setStyleSheet(u"border:none;\n"
"border:2px solid rgb(220,220,220);\n"
"border-radius:20px;\n"
"background-color: rgb(242, 242, 242);")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.label_69 = QLabel(self.frame_57)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(10, 40, 400, 50))
        self.label_69.setMinimumSize(QSize(400, 50))
        self.label_69.setMaximumSize(QSize(400, 50))
        self.label_69.setFont(font11)
        self.label_69.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_70 = QLabel(self.frame_57)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(10, 180, 400, 50))
        self.label_70.setMinimumSize(QSize(400, 50))
        self.label_70.setMaximumSize(QSize(400, 50))
        self.label_70.setFont(font11)
        self.label_70.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.label_71 = QLabel(self.frame_57)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(10, 110, 400, 50))
        self.label_71.setMinimumSize(QSize(400, 50))
        self.label_71.setMaximumSize(QSize(400, 50))
        self.label_71.setFont(font11)
        self.label_71.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
" }\n"
"")
        self.pushButton_81 = QPushButton(self.frame_57)
        self.pushButton_81.setObjectName(u"pushButton_81")
        self.pushButton_81.setGeometry(QRect(700, 40, 50, 50))
        self.pushButton_81.setMinimumSize(QSize(50, 50))
        self.pushButton_81.setMaximumSize(QSize(50, 50))
        self.pushButton_81.setFont(font13)
        self.pushButton_81.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_82 = QPushButton(self.frame_57)
        self.pushButton_82.setObjectName(u"pushButton_82")
        self.pushButton_82.setGeometry(QRect(700, 110, 50, 50))
        self.pushButton_82.setMinimumSize(QSize(50, 50))
        self.pushButton_82.setMaximumSize(QSize(50, 50))
        self.pushButton_82.setFont(font13)
        self.pushButton_82.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_83 = QPushButton(self.frame_57)
        self.pushButton_83.setObjectName(u"pushButton_83")
        self.pushButton_83.setGeometry(QRect(700, 180, 50, 50))
        self.pushButton_83.setMinimumSize(QSize(50, 50))
        self.pushButton_83.setMaximumSize(QSize(50, 50))
        self.pushButton_83.setFont(font13)
        self.pushButton_83.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.label_72 = QLabel(self.frame_56)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(0, 0, 880, 50))
        self.label_72.setMinimumSize(QSize(880, 50))
        self.label_72.setMaximumSize(QSize(880, 50))
        self.label_72.setFont(font10)
        self.label_72.setStyleSheet(u"QLabel{	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);	\n"
"	background-color: rgba(30, 59, 81, 120);\n"
" }\n"
"QLabel:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"")
        self.label_72.setAlignment(Qt.AlignCenter)
        self.stackedWidget_5.addWidget(self.versionUpdates)
        self.stackedWidget_3.addWidget(self.AppSettings)

        self.horizontalLayout_13.addWidget(self.stackedWidget_3)

        self.frame_30 = QFrame(self.Settings)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(200, 686))
        self.frame_30.setMaximumSize(QSize(200, 2058))
        self.frame_30.setStyleSheet(u"border-left: 1px solid rgb(220, 220, 220);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(1, 1, 200, 300))
        self.frame_31.setMinimumSize(QSize(200, 300))
        self.frame_31.setMaximumSize(QSize(200, 900))
        self.frame_31.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(220,220,220);")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.pushButton_38 = QPushButton(self.frame_31)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(10, 5, 180, 30))
        self.pushButton_38.setMinimumSize(QSize(180, 30))
        self.pushButton_38.setMaximumSize(QSize(180, 30))
        font15 = QFont()
        font15.setFamily(u"Calibri")
        font15.setPointSize(12)
        font15.setBold(True)
        font15.setWeight(75)
        self.pushButton_38.setFont(font15)
        self.pushButton_38.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);\n"
" }\n"
"QPushButton:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_40 = QPushButton(self.frame_31)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setGeometry(QRect(10, 50, 180, 30))
        self.pushButton_40.setMinimumSize(QSize(180, 30))
        self.pushButton_40.setMaximumSize(QSize(180, 30))
        self.pushButton_40.setFont(font13)
        self.pushButton_40.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_41 = QPushButton(self.frame_31)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setGeometry(QRect(10, 120, 180, 30))
        self.pushButton_41.setMinimumSize(QSize(180, 30))
        self.pushButton_41.setMaximumSize(QSize(180, 30))
        self.pushButton_41.setFont(font13)
        self.pushButton_41.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"border-bottom: 1px solid rgb(245,245,245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"	 border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_42 = QPushButton(self.frame_31)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setGeometry(QRect(10, 190, 180, 30))
        self.pushButton_42.setMinimumSize(QSize(180, 30))
        self.pushButton_42.setMaximumSize(QSize(180, 30))
        self.pushButton_42.setFont(font13)
        self.pushButton_42.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245,245,245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"	 border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_43 = QPushButton(self.frame_31)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setGeometry(QRect(10, 260, 180, 30))
        self.pushButton_43.setMinimumSize(QSize(180, 30))
        self.pushButton_43.setMaximumSize(QSize(180, 30))
        self.pushButton_43.setFont(font13)
        self.pushButton_43.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245,245,245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"	 border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(1, 301, 200, 300))
        self.frame_32.setMinimumSize(QSize(200, 300))
        self.frame_32.setMaximumSize(QSize(200, 900))
        self.frame_32.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(220,220,220);")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.pushButton_39 = QPushButton(self.frame_32)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setGeometry(QRect(10, 5, 180, 30))
        self.pushButton_39.setMinimumSize(QSize(180, 30))
        self.pushButton_39.setMaximumSize(QSize(180, 30))
        self.pushButton_39.setFont(font15)
        self.pushButton_39.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 220, 220);\n"
" }\n"
"QPushButton:hover{	\n"
"	color: rgba(0, 0, 0, 100);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_44 = QPushButton(self.frame_32)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setGeometry(QRect(10, 45, 180, 30))
        self.pushButton_44.setMinimumSize(QSize(180, 30))
        self.pushButton_44.setMaximumSize(QSize(180, 30))
        self.pushButton_44.setFont(font13)
        self.pushButton_44.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_45 = QPushButton(self.frame_32)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setGeometry(QRect(10, 85, 180, 30))
        self.pushButton_45.setMinimumSize(QSize(180, 30))
        self.pushButton_45.setMaximumSize(QSize(180, 30))
        self.pushButton_45.setFont(font13)
        self.pushButton_45.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_46 = QPushButton(self.frame_32)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setGeometry(QRect(10, 125, 180, 30))
        self.pushButton_46.setMinimumSize(QSize(180, 30))
        self.pushButton_46.setMaximumSize(QSize(180, 30))
        self.pushButton_46.setFont(font13)
        self.pushButton_46.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_47 = QPushButton(self.frame_32)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setGeometry(QRect(10, 165, 180, 30))
        self.pushButton_47.setMinimumSize(QSize(180, 30))
        self.pushButton_47.setMaximumSize(QSize(180, 30))
        self.pushButton_47.setFont(font13)
        self.pushButton_47.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_48 = QPushButton(self.frame_32)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setGeometry(QRect(10, 205, 180, 30))
        self.pushButton_48.setMinimumSize(QSize(180, 30))
        self.pushButton_48.setMaximumSize(QSize(180, 30))
        self.pushButton_48.setFont(font13)
        self.pushButton_48.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.pushButton_49 = QPushButton(self.frame_32)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setGeometry(QRect(10, 245, 180, 30))
        self.pushButton_49.setMinimumSize(QSize(180, 30))
        self.pushButton_49.setMaximumSize(QSize(180, 30))
        self.pushButton_49.setFont(font13)
        self.pushButton_49.setStyleSheet(u"QPushButton {\n"
"	background-color: white;	\n"
"	color: black;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(245, 245, 245);\n"
" }\n"
"QPushButton:hover{	\n"
"	background-color: rgba(230, 136, 136, 50);\n"
"    border-right: 2px solid rgb(30, 59, 81);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")
        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(1, 601, 200, 96))
        self.frame_33.setMinimumSize(QSize(200, 86))
        self.frame_33.setMaximumSize(QSize(200, 258))
        self.frame_33.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(240,240,240);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.pushButton_16 = QPushButton(self.frame_33)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(55, 10, 90, 30))
        self.pushButton_16.setMinimumSize(QSize(90, 30))
        self.pushButton_16.setMaximumSize(QSize(90, 30))
        self.pushButton_16.setFont(font15)
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
"	background-color: red;	\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(230, 136, 136);\n"
" }\n"
"QPushButton:hover{     \n"
"	background-color: rgba(255, 0, 0, 200);\n"
" }\n"
"QPushButton:pressed{     \n"
"	border-bottom: 5px solid rgb(30, 59, 81);\n"
"}")

        self.horizontalLayout_13.addWidget(self.frame_30)

        self.stackedWidget.addWidget(self.Settings)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.centralMainFrame)


        self.horizontalLayout.addLayout(self.verticalLayout)

        DashBoard.setCentralWidget(self.centralwidget)

        self.retranslateUi(DashBoard)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DashBoard)
    # setupUi

    def retranslateUi(self, DashBoard):
        DashBoard.setWindowTitle(QCoreApplication.translate("DashBoard", u"Scepter", None))
        self.dashboard.setText(QCoreApplication.translate("DashBoard", u"Dashboard", None))
        self.projects.setText(QCoreApplication.translate("DashBoard", u"Projects", None))
        self.messages.setText(QCoreApplication.translate("DashBoard", u"Messages", None))
        self.settings.setText(QCoreApplication.translate("DashBoard", u"Settings", None))
        self.user_avatar.setText("")
        self.user_handle.setText(QCoreApplication.translate("DashBoard", u"User Name", None))
        self.max.setText("")
        self.min.setText("")
        self.close.setText("")
        self.label_2.setText(QCoreApplication.translate("DashBoard", u"Projects", None))
        self.label_3.setText(QCoreApplication.translate("DashBoard", u"Progress Reports", None))
        self.label_5.setText(QCoreApplication.translate("DashBoard", u"Schedules", None))
        self.label_6.setText(QCoreApplication.translate("DashBoard", u"Members", None))
        self.pushButton_3.setText(QCoreApplication.translate("DashBoard", u"Create New Project", None))
        self.pushButton_4.setText(QCoreApplication.translate("DashBoard", u"Past Projects", None))
        self.label_20.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("DashBoard", u"User", None))
        self.label_21.setText(QCoreApplication.translate("DashBoard", u"Welcome!", None))
        self.label_22.setText(QCoreApplication.translate("DashBoard", u"User Name", None))
        self.label_25.setText(QCoreApplication.translate("DashBoard", u"Get Started", None))
        self.pushButton_20.setText(QCoreApplication.translate("DashBoard", u"New Chat", None))
        self.pushButton_21.setText(QCoreApplication.translate("DashBoard", u"New Group", None))
        self.pushButton_22.setText(QCoreApplication.translate("DashBoard", u"New Contact", None))
        self.label_23.setText(QCoreApplication.translate("DashBoard", u"You are signed in as \"UserName@email.com\"", None))
        self.label_24.setText(QCoreApplication.translate("DashBoard", u"Learn more", None))
        self.label_18.setText(QCoreApplication.translate("DashBoard", u"Last seen days ago", None))
        self.label_17.setText(QCoreApplication.translate("DashBoard", u"Member 1", None))
        self.label_19.setText(QCoreApplication.translate("DashBoard", u"Type a message here", None))
        self.pushButton_14.setText(QCoreApplication.translate("DashBoard", u"Chats", None))
        self.pushButton_18.setText(QCoreApplication.translate("DashBoard", u"Contacts", None))
        self.pushButton_17.setText(QCoreApplication.translate("DashBoard", u"Groups", None))
        self.pushButton_23.setText(QCoreApplication.translate("DashBoard", u"Member 1", None))
        self.pushButton_24.setText(QCoreApplication.translate("DashBoard", u"Member 2", None))
        self.pushButton_25.setText(QCoreApplication.translate("DashBoard", u"Member 3", None))
        self.pushButton_26.setText(QCoreApplication.translate("DashBoard", u"Member 4", None))
        self.pushButton_27.setText(QCoreApplication.translate("DashBoard", u"Member 6", None))
        self.pushButton_28.setText(QCoreApplication.translate("DashBoard", u"Member 5", None))
        self.pushButton_29.setText(QCoreApplication.translate("DashBoard", u"Member 7", None))
        self.pushButton_30.setText(QCoreApplication.translate("DashBoard", u"Member 10", None))
        self.pushButton_31.setText(QCoreApplication.translate("DashBoard", u"Member 9", None))
        self.pushButton_32.setText(QCoreApplication.translate("DashBoard", u"Member 8", None))
        self.label_11.setText(QCoreApplication.translate("DashBoard", u"My Account", None))
        self.label_12.setText(QCoreApplication.translate("DashBoard", u"Username", None))
        self.label_14.setText(QCoreApplication.translate("DashBoard", u"Phone Number", None))
        self.label_13.setText(QCoreApplication.translate("DashBoard", u"Email", None))
        self.label_16.setText(QCoreApplication.translate("DashBoard", u"*Username*", None))
        self.label_26.setText(QCoreApplication.translate("DashBoard", u"*test@email.com*", None))
        self.label_27.setText(QCoreApplication.translate("DashBoard", u"*0000000000*", None))
        self.pushButton_50.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_51.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_52.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_28.setText(QCoreApplication.translate("DashBoard", u"Enter Old Password", None))
        self.label_30.setText(QCoreApplication.translate("DashBoard", u"Enter New Password", None))
        self.pushButton_53.setText(QCoreApplication.translate("DashBoard", u"Change Password", None))
        self.label_15.setText(QCoreApplication.translate("DashBoard", u"Password and Authentication", None))
        self.label_38.setText(QCoreApplication.translate("DashBoard", u"Allow direct messages from member", None))
        self.label_39.setText(QCoreApplication.translate("DashBoard", u"Every one can add you as friend", None))
        self.label_40.setText(QCoreApplication.translate("DashBoard", u"Use data to improve scepter", None))
        self.pushButton_57.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_58.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_59.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_37.setText(QCoreApplication.translate("DashBoard", u"Privacy And Safety", None))
        self.label_41.setText(QCoreApplication.translate("DashBoard", u"Allow direct messages from member", None))
        self.label_42.setText(QCoreApplication.translate("DashBoard", u"Every one can add you as friend", None))
        self.label_43.setText(QCoreApplication.translate("DashBoard", u"Use data to improve scepter", None))
        self.pushButton_60.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_61.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_62.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_44.setText(QCoreApplication.translate("DashBoard", u"Backup and Restore", None))
        self.label_45.setText(QCoreApplication.translate("DashBoard", u"Allow direct messages from member", None))
        self.label_46.setText(QCoreApplication.translate("DashBoard", u"Every one can add you as friend", None))
        self.label_47.setText(QCoreApplication.translate("DashBoard", u"Use data to improve scepter", None))
        self.pushButton_63.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_64.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_65.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_48.setText(QCoreApplication.translate("DashBoard", u"Add Account", None))
        self.label_49.setText(QCoreApplication.translate("DashBoard", u"Allow direct messages from member", None))
        self.label_50.setText(QCoreApplication.translate("DashBoard", u"Every one can add you as friend", None))
        self.label_51.setText(QCoreApplication.translate("DashBoard", u"Use data to improve scepter", None))
        self.pushButton_66.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_67.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_68.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_52.setText(QCoreApplication.translate("DashBoard", u"Appearance", None))
        self.label_53.setText(QCoreApplication.translate("DashBoard", u"Allow direct messages from member", None))
        self.label_54.setText(QCoreApplication.translate("DashBoard", u"Every one can add you as friend", None))
        self.label_55.setText(QCoreApplication.translate("DashBoard", u"Use data to improve scepter", None))
        self.pushButton_69.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_70.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_71.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_56.setText(QCoreApplication.translate("DashBoard", u"Notification", None))
        self.label_57.setText(QCoreApplication.translate("DashBoard", u"Allow direct messages from member", None))
        self.label_58.setText(QCoreApplication.translate("DashBoard", u"Every one can add you as friend", None))
        self.label_59.setText(QCoreApplication.translate("DashBoard", u"Use data to improve scepter", None))
        self.pushButton_72.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_73.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_74.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_60.setText(QCoreApplication.translate("DashBoard", u"Text and Images", None))
        self.label_61.setText(QCoreApplication.translate("DashBoard", u"Allow direct messages from member", None))
        self.label_62.setText(QCoreApplication.translate("DashBoard", u"Every one can add you as friend", None))
        self.label_63.setText(QCoreApplication.translate("DashBoard", u"Use data to improve scepter", None))
        self.pushButton_75.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_76.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_77.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_64.setText(QCoreApplication.translate("DashBoard", u"Performance", None))
        self.label_65.setText(QCoreApplication.translate("DashBoard", u"Allow direct messages from member", None))
        self.label_66.setText(QCoreApplication.translate("DashBoard", u"Every one can add you as friend", None))
        self.label_67.setText(QCoreApplication.translate("DashBoard", u"Use data to improve scepter", None))
        self.pushButton_78.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_79.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_80.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_68.setText(QCoreApplication.translate("DashBoard", u"Language", None))
        self.label_69.setText(QCoreApplication.translate("DashBoard", u"Allow direct messages from member", None))
        self.label_70.setText(QCoreApplication.translate("DashBoard", u"Every one can add you as friend", None))
        self.label_71.setText(QCoreApplication.translate("DashBoard", u"Use data to improve scepter", None))
        self.pushButton_81.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_82.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.pushButton_83.setText(QCoreApplication.translate("DashBoard", u"Edit", None))
        self.label_72.setText(QCoreApplication.translate("DashBoard", u"Version and Updates", None))
        self.pushButton_38.setText(QCoreApplication.translate("DashBoard", u"User Settings", None))
        self.pushButton_40.setText(QCoreApplication.translate("DashBoard", u"My Account", None))
        self.pushButton_41.setText(QCoreApplication.translate("DashBoard", u"Privacy and Safety", None))
        self.pushButton_42.setText(QCoreApplication.translate("DashBoard", u"Backup and Restore", None))
        self.pushButton_43.setText(QCoreApplication.translate("DashBoard", u"Add Account", None))
        self.pushButton_39.setText(QCoreApplication.translate("DashBoard", u"App Settings", None))
        self.pushButton_44.setText(QCoreApplication.translate("DashBoard", u"Appearance", None))
        self.pushButton_45.setText(QCoreApplication.translate("DashBoard", u"Notification", None))
        self.pushButton_46.setText(QCoreApplication.translate("DashBoard", u"Text and Images", None))
        self.pushButton_47.setText(QCoreApplication.translate("DashBoard", u"Performance", None))
        self.pushButton_48.setText(QCoreApplication.translate("DashBoard", u"Language", None))
        self.pushButton_49.setText(QCoreApplication.translate("DashBoard", u"Version and Updates", None))
        self.pushButton_16.setText(QCoreApplication.translate("DashBoard", u"Log Out", None))
    # retranslateUi

