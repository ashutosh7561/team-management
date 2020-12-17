import sys
from os.path import abspath, dirname

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import platform
import time

from controller.authenticator import authenticate

# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import (
#     QCoreApplication,
#     QDate,
#     QDateTime,
#     QEvent,
#     QMetaObject,
#     QObject,
#     QPoint,
#     QPropertyAnimation,
#     QRect,
#     QSize,
#     Qt,
#     QTime,
#     QUrl,
# )
# from PySide2.QtGui import (
#     QBrush,
#     QColor,
#     QConicalGradient,
#     QCursor,
#     QFont,
#     QFontDatabase,
#     QIcon,
#     QKeySequence,
#     QLinearGradient,
#     QPainter,
#     QPalette,
#     QPixmap,
#     QRadialGradient,
# )
# from PySide2.QtWidgets import *

## ==> Dashboard window
from view.ui_DashBoard import Ui_DashBoard

## ==> MAIN WINDOW
from view.ui_main_window import Ui_MainWindow

## ==> SPLASH SCREEN
from view.ui_Splash_screen import Ui_SplashScreen

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMainWindow,
)
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect

## ==> GLOBALS
WINDOW_SIZE = 0


class AdminPannel(QWidget):
    def __init__(self, view_queue, controller_queue, model_queue, **kwargs):
        super(AdminPannel, self).__init__(**kwargs)
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue
        uic.loadUi(
            "C:\\Users\\Ashutosh\\Desktop\\pp\\repo\\team-management\\production\\view\\admin_pannel.ui",
            self,
        )
        self.switch_to_credentials()
        self.credentials.clicked.connect(self.switch_to_credentials)
        self.access_rights.clicked.connect(self.switch_to_access_rights)
        self.posts.clicked.connect(self.switch_to_posts)
        self.add_entry.clicked.connect(self.populate_data)

        self.user_list.setWidgetResizable(True)
        self.posts_list.setWidgetResizable(True)
        self.glob = 1

    def populate_data(self):
        self.controller_queue.put(["admin_get_users_data"])

    def feed_data(self, l):
        wig = QWidget()
        box = QVBoxLayout()
        for _ in range(l + self.glob):
            t = CustWidget()
            box.addWidget(t)
        wig.setLayout(box)
        self.user_list.setWidget(wig)
        self.glob += 2

    def switch_to_credentials(self):
        self.central_stack_frame.setCurrentWidget(self.credentials_page)

    def switch_to_access_rights(self):
        self.central_stack_frame.setCurrentWidget(self.access_rights_page)

    def switch_to_posts(self):
        # dummy posts data
        post_data = [
            PostTemplate(self.view_queue, self.controller_queue, self.model_queue)
            for i in range(10)
        ]
        lis = QWidget()
        bb = QVBoxLayout()
        for i in post_data:
            bb.addWidget(i)
        lis.setLayout(bb)
        self.posts_list.setWidget(lis)
        self.central_stack_frame.setCurrentWidget(self.posts_page)


class PostTemplate(QWidget):
    def __init__(self, view_queue, controller_queue, model_queue, **kwargs):
        super(PostTemplate, self).__init__(**kwargs)
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue
        uic.loadUi(
            "C:\\Users\\Ashutosh\\Desktop\\pp\\repo\\team-management\\production\\view\\post_template.ui",
            self,
        )
        self.toggle = True
        self.access_rights_status = [True] * 6

        self.post_name.clicked.connect(self.toggle_access_rights_list)
        self.access_right_1.clicked.connect(self.toggle_access_right_1)
        self.access_right_2.clicked.connect(self.toggle_access_right_2)
        self.access_right_3.clicked.connect(self.toggle_access_right_3)
        self.access_right_4.clicked.connect(self.toggle_access_right_4)
        self.access_right_5.clicked.connect(self.toggle_access_right_5)
        self.access_right_6.clicked.connect(self.toggle_access_right_6)

        self.toggle_access_rights_list()

    def toggle_access_right_1(self):
        if self.access_rights_status[0]:
            self.access_right_1.setStyleSheet("background-color: rgb(0, 255, 0)")
            self.access_rights_status[0] = False
        else:
            self.access_right_1.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.access_rights_status[0] = True

    def toggle_access_right_2(self):
        if self.access_rights_status[1]:
            self.access_right_2.setStyleSheet("background-color: rgb(0, 255, 0)")
            self.access_rights_status[1] = False
        else:
            self.access_right_2.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.access_rights_status[1] = True

    def toggle_access_right_3(self):
        if self.access_rights_status[2]:
            self.access_right_3.setStyleSheet("background-color: rgb(0, 255, 0)")
            self.access_rights_status[2] = False
        else:
            self.access_right_3.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.access_rights_status[2] = True

    def toggle_access_right_4(self):
        if self.access_rights_status[3]:
            self.access_right_4.setStyleSheet("background-color: rgb(0, 255, 0)")
            self.access_rights_status[3] = False
        else:
            self.access_right_4.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.access_rights_status[3] = True

    def toggle_access_right_5(self):
        if self.access_rights_status[4]:
            self.access_right_5.setStyleSheet("background-color: rgb(0, 255, 0)")
            self.access_rights_status[4] = False
        else:
            self.access_right_5.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.access_rights_status[4] = True

    def toggle_access_right_6(self):
        if self.access_rights_status[5]:
            self.access_right_6.setStyleSheet("background-color: rgb(0, 255, 0)")
            self.access_rights_status[5] = False
        else:
            self.access_right_6.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.access_rights_status[5] = True

    def toggle_access_rights_list(self):
        if self.toggle:
            self.temp = self.post_rights
            self.post_rights.setParent(None)
            self.toggle = False
        else:
            self.layout().addWidget(self.temp)
            self.toggle = True


class CustWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            "C:\\Users\\Ashutosh\\Desktop\\pp\\repo\\team-management\\production\\view\\users_table_entry_template.ui",
            self,
        )


class LoginScreen(QMainWindow):
    def __init__(self, view_queue, controller_queue, model_queue, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue
        uic.loadUi(
            "C:\\Users\\Ashutosh\\Desktop\\pp\\repo\\team-management\\production\\view\\main_window.ui",
            self,
        )
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(20)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0, 0, 0, 255))
        # self.ui.label.setGraphicsEffect(self.shadow)

        # shadow1(self.ui.label_5, 40)
        # shadow1(self.ui.label_6, 40)
        # shadow1(self.ui.frame_2, 20)

        self.login_btn.clicked.connect(self.LoginFunc)
        # self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)

    def LoginFunc(self):
        self.start_time = time.time()
        username = self.username_field.text()
        password = self.password_field.text()
        self.controller_queue.put(["validate_credentials", username, password])

    def invalid_user(self):
        print(time.time() - self.start_time)
        print("Incorrect Credentials")
        self.username_field.setText("")
        self.username_field.setStyleSheet("""QLineEdit {border: 1px solid red }""")
        self.password_field.setText("")
        self.password_field.setStyleSheet("""QLineEdit {border: 1px solid red }""")


class SplashScreen(QMainWindow):
    def __init__(self, view_queue, controller_queue, model_queue, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue
        uic.loadUi(
            "C:\\Users\\Ashutosh\\Desktop\\pp\\repo\\team-management\\production\\view\\Splash_screen.ui",
            self,
        )
        # self.ui = Ui_SplashScreen()
        # self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(20)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0, 0, 0, 255))
        # self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # shadow1(self.ui.label, 20)

        self.label_3.setText("<strong>LOADING</strong>")
        self.progressBar.setValue(0)

    def set_progress_value(self, value, message):
        self.progressBar.setValue(value)
        self.label_3.setText(f"<strong>{message}</strong>")


class Dashboard(QWidget):
    def __init__(self, view_queue, controller_queue, model_queue, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue
        uic.loadUi(
            "C:\\Users\\Ashutosh\\Desktop\\pp\\repo\\team-management\\production\\view\\root_window.ui",
            self,
        )

        self.dashboard.clicked.connect(
            lambda: self.stacked_action_pannel.setCurrentWidget(self.dashboard_frame)
        )
        self.projects.clicked.connect(
            lambda: self.stacked_action_pannel.setCurrentWidget(self.projects_frame)
        )
        self.tickets.clicked.connect(
            lambda: self.stacked_action_pannel.setCurrentWidget(self.tickets_frame)
        )
        self.boards.clicked.connect(
            lambda: self.stacked_action_pannel.setCurrentWidget(self.boards_frame)
        )
        self.calendar.clicked.connect(
            lambda: self.stacked_action_pannel.setCurrentWidget(self.calendar_frame)
        )
        self.analysis.clicked.connect(
            lambda: self.stacked_action_pannel.setCurrentWidget(self.analysis_frame)
        )
        self.messages.clicked.connect(
            lambda: self.stacked_action_pannel.setCurrentWidget(self.messages_frame)
        )
        self.worklog.clicked.connect(
            lambda: self.stacked_action_pannel.setCurrentWidget(self.worklog_frame)
        )
        self.settings.clicked.connect(
            lambda: self.stacked_action_pannel.setCurrentWidget(self.settings_frame)
        )


class ViewHandler:
    def __init__(self, view_queue, controller_queue, model_queue):
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue

        print("view handler up and running")

        self.CHECK_DURATION = 1000

        self.app = QApplication(sys.argv)
        self.main_window = None
        self.splash_screen = SplashScreen(
            self.view_queue, self.controller_queue, self.model_queue
        )
        self.login_window = LoginScreen(
            self.view_queue, self.controller_queue, self.model_queue
        )
        self.dashboard_window = Dashboard(
            self.view_queue, self.controller_queue, self.model_queue
        )
        self.admin_pannel = AdminPannel(
            self.view_queue, self.controller_queue, self.model_queue
        )

        self.start_app()

    def start_app(self):
        self.show_splash_screen()
        self.controller_queue.put(["load_resources"])
        QtCore.QTimer.singleShot(self.CHECK_DURATION, self.check_for_messages)
        self.app.exec_()

    def stop_app(self):
        self.main_window.close()

    def check_for_messages(self):
        # print("this will acts like a schedular which checks for messages")
        if not (self.view_queue.empty()):
            message = self.view_queue.get()
            self.identify_message(message)

        QtCore.QTimer.singleShot(self.CHECK_DURATION, self.check_for_messages)

    def load_status(self, progress_value, special_message):
        print("setting progress bar value to", progress_value)
        self.set_status(progress_value, special_message)

    def load_complete(self):
        self.close_splash_screen()
        self.show_login_window()

    def identify_message(self, message):
        self.message_dict = {
            "load_status": self.load_status,
            "load_complete": self.load_complete,
            "stop_app": self.stop_app,
            "switch_to_dashboard": self.show_dashboard_window,
            "switch_to_admin": self.show_admin_pannel,
            "admin_users_data": self.show_admin_users_data,
            "valid_user": self.valid_user,
            "invalid_user": self.invalid_user,
        }

        self.message_dict[message[0]](*message[1:])

    def invalid_user(self):
        self.main_window.invalid_user()

    def valid_user(self, post, user_id):
        if post == "admin":
            self.show_admin_pannel(user_id)
        elif post == "general":
            self.show_dashboard_window()

    def show_admin_users_data(self, l):
        self.main_window.feed_data(l)

    def show_admin_pannel(self, username):
        self.main_window.close()
        self.main_window = self.admin_pannel
        self.main_window.user_handle.setText(username)
        self.main_window.populate_data()
        self.main_window.show()

    def set_status(self, value, message):
        self.splash_screen.set_progress_value(value, message)

    def show_splash_screen(self):
        self.main_window = self.splash_screen
        self.CHECK_DURATION = 100
        self.main_window.show()

    def close_splash_screen(self):
        self.CHECK_DURATION = 1000

    def show_login_window(self):
        self.main_window.close()
        self.main_window = self.login_window
        self.main_window.show()

    def show_dashboard_window(self):
        self.main_window.close()
        self.main_window = self.dashboard_window
        self.main_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AdminPannel()
    win.show()
    sys.exit(app.exec_())