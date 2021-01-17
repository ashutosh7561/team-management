import sys
import os
from os.path import abspath, dirname

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import platform
import time
from queue import Queue

## ==> Dashboard window
from view.ui_DashBoard import Ui_DashBoard

## ==> MAIN WINDOW
from view.ui_main_window import Ui_MainWindow

## ==> SPLASH SCREEN
from view.ui_Splash_screen import Ui_SplashScreen

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from controller.chats.sockets.client import ServerCon
from view.messagecentral import *


class ViewHandler:
    def __init__(self, view_queue, controller_queue, model_queue):
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue

        print("view handler up and running")

        self.CHECK_DURATION = 100

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
        elif post in ["general", "project_manager", "team_lead"]:
            self.show_dashboard_window(user_id)

    def show_admin_users_data(self, user_data_list):
        self.main_window.feed_data(user_data_list)

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
        self.CHECK_DURATION = 100

    def show_login_window(self):
        self.main_window.close()
        self.main_window = self.login_window
        self.main_window.show()

    def show_dashboard_window(self, user_id):
        self.main_window.close()
        self.main_window = self.dashboard_window
        self.main_window.show()
        self.dashboard_window.initiate(user_id)
