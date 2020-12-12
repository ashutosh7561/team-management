import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    QCoreApplication,
    QPropertyAnimation,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
    QEvent,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *

from controller.authenticator import authenticate

## ==> SPLASH SCREEN
from view.ui_Splash_screen import Ui_SplashScreen

## ==> MAIN WINDOW
from view.ui_main_window import Ui_MainWindow

## ==> Dashboard window
from view.ui_DashBoard import Ui_DashBoard

## ==> GLOBALS
WINDOW_SIZE = 0

# YOUR APPLICATION
class LoginScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 255))
        self.ui.label.setGraphicsEffect(self.shadow)

        shadow1(self.ui.label_5, 40)
        shadow1(self.ui.label_6, 40)
        shadow1(self.ui.frame_2, 20)
        # shadow1(self.ui.label_2,5)
        # shadow1(self.ui.label_3,5)
        # shadow1(self.ui.label_4,5)

        # MAIN WINDOW LABEL
        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label_2.setText("THANK YOU"))
        # QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))
        self.ui.pushButton.clicked.connect(self.LoginFunc)
        self.ui.password_field.setEchoMode(QtWidgets.QLineEdit.Password)

    def LoginFunc(self):
        username = self.ui.username_field.text()
        password = self.ui.password_field.text()
        valid = authenticate(username, password)
        if valid:
            self.main = Dashboard()
            self.main.show()
            print(valid)
            self.main.ui.label_8.setText(username)
            self.close()
        else:
            print("Incorrect Credentials")
            self.ui.username_field.setText("")
            self.ui.username_field.setStyleSheet(
                """QLineEdit {border: 1px solid red }"""
            )
            self.ui.password_field.setText("")
            self.ui.password_field.setStyleSheet(
                """QLineEdit {border: 1px solid red }"""
            )


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 255))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        shadow1(self.ui.label, 20)

        ## QTIMER ==> START
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        # self.timer.start(5)

        self.ui.label_3.setText("<strong>LOADING</strong>")

        QtCore.QTimer.singleShot(
            1500, lambda: self.ui.label_3.setText("<strong>LOADING DATABASE</strong>")
        )
        QtCore.QTimer.singleShot(
            3000,
            lambda: self.ui.label_3.setText("<strong>LOADING USER INTERFACE</strong>"),
        )

    def set_progress_value(self, value):
        self.ui.progressBar.setValue(value)
        # if value > 100:
        # self.timer.stop()
        # self.main = MainWindow()
        # self.main.show()
        # self.close()


class Dashboard(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_DashBoard()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ##shadow effect
        shadow1(self.ui.label, 10)
        shadow1(self.ui.pushButton, 5)
        shadow1(self.ui.pushButton_2, 5)
        shadow1(self.ui.pushButton_3, 5)
        shadow1(self.ui.pushButton_4, 5)
        shadow1(self.ui.pushButton_5, 5)
        shadow1(self.ui.pushButton_6, 5)
        shadow1(self.ui.pushButton_7, 5)
        shadow1(self.ui.pushButton_8, 5)
        shadow1(self.ui.pushButton_9, 5)
        shadow1(self.ui.frame, 5)
        shadow1(self.ui.frame_2, 5)
        shadow1(self.ui.frame_3, 5)
        shadow1(self.ui.frame_4, 5)
        shadow1(self.ui.frame_5, 5)
        shadow1(self.ui.frame_6, 5)
        shadow1(self.ui.frame_7, 5)
        shadow1(self.ui.frame_8, 5)
        shadow1(self.ui.frame_9, 5)
        shadow1(self.ui.frame_10, 5)
        shadow1(self.ui.frame_12, 5)
        shadow1(self.ui.frame_13, 5)
        shadow1(self.ui.frame_14, 5)
        shadow1(self.ui.frame_15, 5)
        shadow1(self.ui.frame_16, 5)
        shadow1(self.ui.frame_17, 5)
        shadow1(self.ui.frame_18, 5)

        ##navigation to pages
        self.ui.pushButton.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Dashboard)
        )
        self.ui.pushButton_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Projects)
        )
        self.ui.pushButton_3.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Tickets)
        )
        self.ui.pushButton_4.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Boards)
        )
        self.ui.pushButton_5.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Calendar)
        )
        self.ui.pushButton_6.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Analysis)
        )
        self.ui.pushButton_7.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Messages)
        )
        self.ui.pushButton_8.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Worklog)
        )
        self.ui.pushButton_9.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Settings)
        )

        ##window size buttons
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.max.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.min.clicked.connect(lambda: self.showMinimized())

        ##message page navigation
        self.ui.pushButton_7.clicked.connect(self.setMessage)
        self.ui.pushButton_23.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.member1)
        )

    def setMessage(self):
        if self.ui.stackedWidget_2.currentWidget() == self.ui.member1:
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.welcome)

        else:
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.welcome)

    def restore_or_maximize_window(self):
        global WINDOW_SIZE
        win_status = WINDOW_SIZE
        if win_status == 0:
            WINDOW_SIZE = 1
            self.showMaximized()
        else:
            WINDOW_SIZE = 0
            self.showNormal()

    ## move window

    def moveWindow(self):

        if self.isMaximized() == False:
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
        self.ui.frame_3.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.clickPosition)
        # print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.clickPosition = event.globalPos()


def shadow1(self, radius):
    # for child in self.findChildren(QMainWindow,"label_2"):
    #     print("a")
    #     # shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3,Color=(QColor(0, 0, 0, 255)))
    #     # child.setGraphicsEffect(shadow)

    shadow = QGraphicsDropShadowEffect(self)
    shadow.setBlurRadius(radius)
    shadow.setXOffset(0)
    shadow.setYOffset(0)
    shadow.setColor(QColor(0, 0, 0, 255))
    self.setGraphicsEffect(shadow)


class ViewHandler:
    def __init__(self):
        self.app = QApplication(sys.argv)
        # self.splash_screen = SplashScreen()
        self.window = QWidget()
        self.window.setGeometry(0, 0, 500, 300)
        self.window.setWindowTitle("PyQT Tuts!")
        # self.login_window = LoginScreen()
        # self.dashboard_window = Dashboard()
        # self.main_window = self.splash_screen

    def start_app(self):
        self.window.show()
        self.app.exec_()

    def stop_app(self):
        self.window.close()

    def load_status(self, value):
        self.window.set_progress_value(value)

    def start_splash_screen(self):
        self.main_window.close()
        self.main_window = self.splash_screen
        self.main_window.show()

    def show_login_window(self):
        self.main_window.close()
        self.main_window = self.login_window
        self.main_window.show()

    def show_dashboard_window(self):
        self.main_window.close()
        self.main_window = self.dashboard_window
        self.main_window.show()