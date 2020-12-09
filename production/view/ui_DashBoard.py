# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashBoardPabikp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QUrl,
    Qt,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
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
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
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
        self.frame_2.setStyleSheet(
            u"QFrame{\n" "background-color: rgb(30, 59, 81);\n" "}\n" ""
        )
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
        self.pushButton.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 290, 150, 40))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 390, 150, 40))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 340, 150, 40))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 590, 150, 40))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 490, 150, 40))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 440, 150, 40))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 540, 150, 40))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 670, 150, 40))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 125, 125))
        self.label.setPixmap(QPixmap(u":/usericon/res/usericon.png"))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 160, 160, 40))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"\n" "color: rgb(230, 136, 136);")

        self.horizontalLayout.addWidget(self.frame_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(1080, 34))
        self.frame_3.setMaximumSize(QSize(2160, 34))
        self.frame_3.setStyleSheet(
            u"background-color: rgb(230, 136, 136);\n" "border-radius:1px;"
        )
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
        self.max.setStyleSheet(
            u"QPushButton:hover{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            " }\n"
            "QPushButton:pressed{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(u":/button/res/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.max.setIcon(icon1)
        self.max.setIconSize(QSize(30, 30))
        self.min = QPushButton(self.frame_11)
        self.min.setObjectName(u"min")
        self.min.setGeometry(QRect(45, 1, 30, 30))
        sizePolicy1.setHeightForWidth(self.min.sizePolicy().hasHeightForWidth())
        self.min.setSizePolicy(sizePolicy1)
        self.min.setStyleSheet(
            u"QPushButton:hover{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            " }\n"
            "QPushButton:pressed{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            "}"
        )
        icon2 = QIcon()
        icon2.addFile(u":/button/res/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min.setIcon(icon2)
        self.min.setIconSize(QSize(30, 30))
        self.close = QPushButton(self.frame_11)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(85, 1, 30, 30))
        sizePolicy1.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy1)
        self.close.setStyleSheet(
            u"QPushButton:hover{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            " }\n"
            "QPushButton:pressed{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            "}"
        )
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
        sizePolicy1.setHeightForWidth(
            self.centralMainFrame.sizePolicy().hasHeightForWidth()
        )
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
        self.stackedWidget.setStyleSheet(u"background-color: rgb(240, 240, 240);\n" "")
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
        self.frame_4.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 101, 31))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(16)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(
            u"border:none;\n" "border-radius:0px;\n" "color: rgb(30, 59, 81);"
        )

        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.Dashboard)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(360, 300))
        self.frame_5.setMaximumSize(QSize(720, 600))
        self.frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_5.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 171, 31))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(
            u"border:none;\n" "border-radius:0px;\n" "color: rgb(30, 59, 81);"
        )

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
        self.frame_7.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 171, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(
            u"border:none;\n" "border-radius:0px;\n" "color: rgb(30, 59, 81);"
        )

        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.Dashboard)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(350, 320))
        self.frame_8.setMaximumSize(QSize(700, 600))
        self.frame_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_8.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 171, 31))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(
            u"border:none;\n" "border-radius:0px;\n" "color: rgb(30, 59, 81);"
        )

        self.verticalLayout_4.addWidget(self.frame_8)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.Dashboard)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(320, 150))
        self.frame_6.setMaximumSize(QSize(700, 300))
        self.frame_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_6.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 171, 31))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(
            u"border:none;\n" "border-radius:0px;\n" "color: rgb(30, 59, 81);"
        )

        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.Dashboard)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(320, 320))
        self.frame_9.setMaximumSize(QSize(700, 640))
        self.frame_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_9.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 171, 31))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(
            u"border:none;\n" "border-radius:0px;\n" "color: rgb(30, 59, 81);"
        )

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
        sizePolicy2 = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(200, 200))
        self.frame.setMaximumSize(QSize(900, 900))
        self.frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
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
        self.label_9.setStyleSheet(
            u"border:none;\n" "border-radius:0px;\n" "color: rgb(30, 59, 81);"
        )

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.Projects)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setMinimumSize(QSize(200, 200))
        self.frame_10.setMaximumSize(QSize(900, 900))
        self.frame_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_10.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 200, 30))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(
            u"border:none;\n" "border-radius:0px;\n" "color: rgb(30, 59, 81);"
        )

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
        self.frame_12.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.pushButton_10 = QPushButton(self.frame_12)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(310, 160, 150, 50))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(14)
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.stackedWidget.addWidget(self.Tickets)
        self.Boards = QWidget()
        self.Boards.setObjectName(u"Boards")
        self.Boards.setMinimumSize(QSize(1080, 700))
        self.Boards.setMaximumSize(QSize(2160, 1400))
        self.Boards.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_13 = QFrame(self.Boards)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(170, 100, 801, 461))
        self.frame_13.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.pushButton_11 = QPushButton(self.frame_13)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_11.setFont(font3)
        self.pushButton_11.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.stackedWidget.addWidget(self.Boards)
        self.Calendar = QWidget()
        self.Calendar.setObjectName(u"Calendar")
        self.Calendar.setMinimumSize(QSize(1080, 700))
        self.Calendar.setMaximumSize(QSize(2160, 1400))
        self.Calendar.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_14 = QFrame(self.Calendar)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(160, 100, 801, 461))
        self.frame_14.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.pushButton_12 = QPushButton(self.frame_14)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_12.setFont(font3)
        self.pushButton_12.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.stackedWidget.addWidget(self.Calendar)
        self.Analysis = QWidget()
        self.Analysis.setObjectName(u"Analysis")
        self.Analysis.setMinimumSize(QSize(1080, 700))
        self.Analysis.setMaximumSize(QSize(2160, 1400))
        self.Analysis.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_15 = QFrame(self.Analysis)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(170, 70, 801, 461))
        self.frame_15.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.pushButton_13 = QPushButton(self.frame_15)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_13.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.stackedWidget.addWidget(self.Analysis)
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
        self.label_20.setStyleSheet(
            u"border-radius:8px;\n"
            "background-color: rgb(0, 255, 0);\n"
            "border: 2px solid rgb(255,255,255);"
        )
        self.pushButton_19 = QPushButton(self.frame_25)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(315, 0, 150, 150))
        self.pushButton_19.setMinimumSize(QSize(150, 150))
        self.pushButton_19.setMaximumSize(QSize(450, 450))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton_19.setFont(font4)
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet(
            u"QPushButton{\n"
            "border-radius:75px;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(152, 199, 255);\n"
            "}\n"
            "QPushButton:hover{     \n"
            "	background-color: rgb(230, 136, 136);\n"
            " }\n"
            "QPushButton:pressed{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            "}"
        )
        self.pushButton_19.raise_()
        self.label_20.raise_()

        self.verticalLayout_7.addWidget(
            self.frame_25, 0, Qt.AlignHCenter | Qt.AlignVCenter
        )

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
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(28)
        self.label_21.setFont(font5)
        self.label_21.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_26)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(780, 51))
        self.label_22.setMaximumSize(QSize(2340, 153))
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(28)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_22.setFont(font6)
        self.label_22.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.label_22)

        self.verticalLayout_7.addWidget(self.frame_26)

        self.label_25 = QLabel(self.frame_24)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(780, 100))
        self.label_25.setMaximumSize(QSize(2340, 300))
        font7 = QFont()
        font7.setFamily(u"Calibri")
        font7.setPointSize(10)
        self.label_25.setFont(font7)
        self.label_25.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

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
        sizePolicy1.setHeightForWidth(
            self.pushButton_20.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_20.setSizePolicy(sizePolicy1)
        self.pushButton_20.setMinimumSize(QSize(150, 51))
        self.pushButton_20.setMaximumSize(QSize(450, 153))
        self.pushButton_20.setFont(font4)
        self.pushButton_20.setStyleSheet(
            u"QPushButton{\n"
            "border-radius:25px;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(30, 59, 81);\n"
            "}\n"
            "QPushButton:hover{     \n"
            "	background-color: rgb(230, 136, 136);\n"
            " }\n"
            "QPushButton:pressed{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            "}"
        )

        self.horizontalLayout_7.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.frame_27)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy1.setHeightForWidth(
            self.pushButton_21.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_21.setSizePolicy(sizePolicy1)
        self.pushButton_21.setMinimumSize(QSize(150, 51))
        self.pushButton_21.setMaximumSize(QSize(450, 153))
        self.pushButton_21.setFont(font4)
        self.pushButton_21.setStyleSheet(
            u"QPushButton{\n"
            "border-radius:25px;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(30, 59, 81);\n"
            "}\n"
            "QPushButton:hover{     \n"
            "	background-color: rgb(230, 136, 136);\n"
            " }\n"
            "QPushButton:pressed{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            "}"
        )

        self.horizontalLayout_7.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_27)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy1.setHeightForWidth(
            self.pushButton_22.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_22.setSizePolicy(sizePolicy1)
        self.pushButton_22.setMinimumSize(QSize(150, 51))
        self.pushButton_22.setMaximumSize(QSize(450, 153))
        self.pushButton_22.setFont(font4)
        self.pushButton_22.setStyleSheet(
            u"QPushButton{\n"
            "border-radius:25px;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(30, 59, 81);\n"
            "}\n"
            "QPushButton:hover{     \n"
            "	background-color: rgb(230, 136, 136);\n"
            " }\n"
            "QPushButton:pressed{     \n"
            "	border-bottom: 5px solid rgb(30, 59, 81);\n"
            "}"
        )

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
        self.label_23.setFont(font7)
        self.label_23.setStyleSheet(u"\n" "color: rgb(230, 136, 136);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_28)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(780, 20))
        self.label_24.setMaximumSize(QSize(2340, 60))
        font8 = QFont()
        font8.setFamily(u"Calibri")
        font8.setPointSize(10)
        font8.setUnderline(True)
        self.label_24.setFont(font8)
        self.label_24.setStyleSheet(u"\n" "color: rgb(230, 136, 136);")
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
        self.frame_22.setStyleSheet(
            u"border:none;\n" "border-bottom: 2px solid rgb(238, 238, 238);"
        )
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
        self.frame_29.setStyleSheet(
            u"border:none;\n"
            "border-bottom: 2px solid rgb(225, 225, 225);\n"
            "border-radius: 5px;"
        )
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_29)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(780, 86))
        self.frame_23.setMaximumSize(QSize(2280, 86))
        self.frame_23.setStyleSheet(
            u"border:none;\n"
            "border-bottom: 2px solid rgb(225, 225, 225);\n"
            "border-radius: 5px;"
        )
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
        self.frame_16.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid rgb(236,236,236);\n"
            "}\n"
            ""
        )
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
        sizePolicy1.setHeightForWidth(
            self.pushButton_14.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_14.setSizePolicy(sizePolicy1)
        self.pushButton_14.setMinimumSize(QSize(50, 20))
        font9 = QFont()
        font9.setFamily(u"Calibri")
        font9.setPointSize(8)
        self.pushButton_14.setFont(font9)
        self.pushButton_14.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_14)

        self.pushButton_18 = QPushButton(self.frame_19)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy1.setHeightForWidth(
            self.pushButton_18.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_18.setSizePolicy(sizePolicy1)
        self.pushButton_18.setMinimumSize(QSize(50, 20))
        self.pushButton_18.setFont(font9)
        self.pushButton_18.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_18)

        self.pushButton_17 = QPushButton(self.frame_19)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy1.setHeightForWidth(
            self.pushButton_17.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_17.setSizePolicy(sizePolicy1)
        self.pushButton_17.setMinimumSize(QSize(50, 20))
        self.pushButton_17.setFont(font9)
        self.pushButton_17.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_17)

        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(10, 70, 281, 591))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.pushButton_23 = QPushButton(self.frame_20)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(40, 30, 200, 40))
        sizePolicy1.setHeightForWidth(
            self.pushButton_23.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_23.setSizePolicy(sizePolicy1)
        self.pushButton_23.setMinimumSize(QSize(50, 20))
        font10 = QFont()
        font10.setFamily(u"Calibri")
        font10.setPointSize(18)
        font10.setBold(True)
        font10.setWeight(75)
        self.pushButton_23.setFont(font10)
        self.pushButton_23.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )

        self.horizontalLayout_6.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.Messages)
        self.Worklog = QWidget()
        self.Worklog.setObjectName(u"Worklog")
        self.Worklog.setMinimumSize(QSize(1080, 700))
        self.Worklog.setMaximumSize(QSize(2160, 1400))
        self.frame_17 = QFrame(self.Worklog)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(110, 90, 801, 461))
        self.frame_17.setStyleSheet(
            u"QFrame{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius:10px;\n"
            "border:1px solid;\n"
            "}\n"
            "QFrame:hover{     \n"
            "	border:2px solid rgb(230, 136, 136);\n"
            " }"
        )
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.pushButton_15 = QPushButton(self.frame_17)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(310, 160, 150, 50))
        self.pushButton_15.setFont(font3)
        self.pushButton_15.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )
        self.stackedWidget.addWidget(self.Worklog)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.Settings.setMinimumSize(QSize(1080, 700))
        self.Settings.setMaximumSize(QSize(2160, 1400))
        self.Settings.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout_9 = QHBoxLayout(self.Settings)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.Settings)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(1080, 686))
        self.frame_18.setMaximumSize(QSize(2160, 2058))
        self.frame_18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n" "")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_30 = QFrame(self.frame_18)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(880, 0, 200, 698))
        self.frame_30.setMinimumSize(QSize(200, 686))
        self.frame_30.setMaximumSize(QSize(200, 2058))
        self.frame_30.setStyleSheet(u"border-left: 1px solid rgb(220, 220, 220);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_30)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(200, 300))
        self.frame_31.setMaximumSize(QSize(200, 900))
        self.frame_31.setStyleSheet(
            u"border:none;\n" "border-bottom:2px solid rgb(220,220,220);"
        )
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_31)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 5, 110, 20))
        self.label_11.setMinimumSize(QSize(110, 20))
        self.label_11.setMaximumSize(QSize(110, 20))
        self.label_11.setFont(font4)

        self.verticalLayout_11.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(200, 300))
        self.frame_32.setMaximumSize(QSize(200, 900))
        self.frame_32.setStyleSheet(
            u"border:none;\n" "border-bottom:2px solid rgb(220,220,220);"
        )
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_32)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 110, 20))
        self.label_12.setMinimumSize(QSize(110, 20))
        self.label_12.setMaximumSize(QSize(110, 20))
        self.label_12.setFont(font4)

        self.verticalLayout_11.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(200, 86))
        self.frame_33.setMaximumSize(QSize(200, 258))
        self.frame_33.setStyleSheet(
            u"border:none;\n" "border-bottom:2px solid rgb(240,240,240);"
        )
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.pushButton_16 = QPushButton(self.frame_33)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(10, 10, 90, 30))
        self.pushButton_16.setMinimumSize(QSize(90, 30))
        self.pushButton_16.setMaximumSize(QSize(90, 30))
        font11 = QFont()
        font11.setFamily(u"Calibri")
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setWeight(75)
        self.pushButton_16.setFont(font11)
        self.pushButton_16.setStyleSheet(
            u"QPushButton {\n"
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
            "}"
        )

        self.verticalLayout_11.addWidget(self.frame_33)

        self.stackedWidget_3 = QStackedWidget(self.frame_18)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(0, 0, 880, 698))
        self.stackedWidget_3.setMinimumSize(QSize(880, 686))
        self.stackedWidget_3.setMaximumSize(QSize(2640, 2058))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_3.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_3.addWidget(self.page_2)

        self.horizontalLayout_9.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.Settings)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.centralMainFrame)

        self.horizontalLayout.addLayout(self.verticalLayout)

        DashBoard.setCentralWidget(self.centralwidget)

        self.retranslateUi(DashBoard)

        QMetaObject.connectSlotsByName(DashBoard)

    # setupUi

    def retranslateUi(self, DashBoard):
        DashBoard.setWindowTitle(
            QCoreApplication.translate("DashBoard", u"Scepter", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("DashBoard", u"Dashboard", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("DashBoard", u"Projects", None)
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("DashBoard", u"Boards", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("DashBoard", u"Tickets", None)
        )
        self.pushButton_8.setText(
            QCoreApplication.translate("DashBoard", u"Worklog", None)
        )
        self.pushButton_6.setText(
            QCoreApplication.translate("DashBoard", u"Analysis", None)
        )
        self.pushButton_5.setText(
            QCoreApplication.translate("DashBoard", u"Calendar", None)
        )
        self.pushButton_7.setText(
            QCoreApplication.translate("DashBoard", u"Messages", None)
        )
        self.pushButton_9.setText(
            QCoreApplication.translate("DashBoard", u"Settings", None)
        )
        self.label.setText("")
        self.label_8.setText(
            QCoreApplication.translate("DashBoard", u"User Name", None)
        )
        self.max.setText("")
        self.min.setText("")
        self.close.setText("")
        self.label_2.setText(QCoreApplication.translate("DashBoard", u"Projects", None))
        self.label_3.setText(
            QCoreApplication.translate("DashBoard", u"Progress Reports", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("DashBoard", u"Schedules", None)
        )
        self.label_6.setText(QCoreApplication.translate("DashBoard", u"Files", None))
        self.label_4.setText(
            QCoreApplication.translate("DashBoard", u"Recent Charts", None)
        )
        self.label_7.setText(QCoreApplication.translate("DashBoard", u"Flags", None))
        self.label_9.setText(
            QCoreApplication.translate("DashBoard", u"Ongoing Projects", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("DashBoard", u"Past Projects", None)
        )
        self.pushButton_10.setText(
            QCoreApplication.translate("DashBoard", u"Tickets Page", None)
        )
        self.pushButton_11.setText(
            QCoreApplication.translate("DashBoard", u"Boards Page", None)
        )
        self.pushButton_12.setText(
            QCoreApplication.translate("DashBoard", u"Calendar Page", None)
        )
        self.pushButton_13.setText(
            QCoreApplication.translate("DashBoard", u"Analysis Page", None)
        )
        self.label_20.setText("")
        self.pushButton_19.setText(
            QCoreApplication.translate("DashBoard", u"User", None)
        )
        self.label_21.setText(
            QCoreApplication.translate("DashBoard", u"Welcome!", None)
        )
        self.label_22.setText(
            QCoreApplication.translate("DashBoard", u"User Name", None)
        )
        self.label_25.setText(
            QCoreApplication.translate("DashBoard", u"Get Started", None)
        )
        self.pushButton_20.setText(
            QCoreApplication.translate("DashBoard", u"New Chat", None)
        )
        self.pushButton_21.setText(
            QCoreApplication.translate("DashBoard", u"New Group", None)
        )
        self.pushButton_22.setText(
            QCoreApplication.translate("DashBoard", u"New Contact", None)
        )
        self.label_23.setText(
            QCoreApplication.translate(
                "DashBoard", u'You are signed in as "UserName@email.com"', None
            )
        )
        self.label_24.setText(
            QCoreApplication.translate("DashBoard", u"Learn more", None)
        )
        self.label_18.setText(
            QCoreApplication.translate("DashBoard", u"Last seen days ago", None)
        )
        self.label_17.setText(
            QCoreApplication.translate("DashBoard", u"Member 1", None)
        )
        self.label_19.setText(
            QCoreApplication.translate("DashBoard", u"Type a message here", None)
        )
        self.pushButton_14.setText(
            QCoreApplication.translate("DashBoard", u"Chats", None)
        )
        self.pushButton_18.setText(
            QCoreApplication.translate("DashBoard", u"Contacts", None)
        )
        self.pushButton_17.setText(
            QCoreApplication.translate("DashBoard", u"Groups", None)
        )
        self.pushButton_23.setText(
            QCoreApplication.translate("DashBoard", u"Member 1", None)
        )
        self.pushButton_15.setText(
            QCoreApplication.translate("DashBoard", u"Worklog Page", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("DashBoard", u"User Settings", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("DashBoard", u"App Settings", None)
        )
        self.pushButton_16.setText(
            QCoreApplication.translate("DashBoard", u"Log Out", None)
        )

    # retranslateUi
