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
        self.chat_list.setWidgetResizable(True)

    def add_group(self, user_list):
        wig = QWidget()
        box = QVBoxLayout()
        for i in user_list:
            gt = ChatWidgetTemplate()
            gt.chat_heading.setText(i)
            box.addWidget(gt)

        wig.setLayout(box)
        self.chat_list.setWidget(wig)


class ChatBoxTemplate(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"./Newfolder/view/chat_box_template.ui", self)
        self.chat_heading.setText("Alex")


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi(r"./Newfolder/view/message_template.ui", self)
        self.central_window.setCurrentWidget(self.message_initial)
        print(self.central_window.addWidget(ChatBoxTemplate()))
        # self.central_window.setCurrentIndex(1)
        t = MessageSidebar()
        user_list = [
            "adam knight",
            "alex maroni",
            "aron goodman",
            "asdf",
            "john wick",
            "ben colson",
            "bill mann",
            "caleb curry",
            "dan gran",
            "garry mann",
            "jack ma",
            "jacob darsen",
            "moray jarry",
            "morgan fitcher",
            "paul simson",
            "peter ullman",
            "phil phonies",
            "smith larson",
            "ulrich highman",
            "xenomorph",
            "zen",
        ]
        t.add_group(user_list)

        print(self.sidebar.layout().addWidget(t))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())