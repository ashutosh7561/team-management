import sys
from os.path import abspath, dirname

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import platform
import time

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
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PyQt5.QtGui import QFont


class ChatWidgetTemplate(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"./Newfolder/view/chat_widget.ui", self)


class MessageCentral(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"./Newfolder/view/message_template_initial.ui", self)


class MessageSidebar(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"./Newfolder/view/message_template_sidebar.ui", self)

    def add_group(self, name):
        gt = ChatWidgetTemplate()
        gt.chat_heading.setText(name)

        self.members_list.layout().addWidget(gt)


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi(r"./Newfolder/view/message_template.ui", self)
        self.central_window.setCurrentWidget(self.message_initial)
        t = MessageSidebar()
        user_list = [
            "adam knight",
            "asdf",
            "john wick",
            "ben colson",
            "caleb curry",
            "jack ma",
            "paul simson",
            "xenomorph",
        ]
        for i in user_list:
            t.add_group(i)

        print(self.sidebar.layout().addWidget(t))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())