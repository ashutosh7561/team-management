import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from PyQt5 import QtCore, QtGui, uic


class ChatDetails(QWidget):
    def __init__(self, parent=None, root=None):
        super().__init__(parent)

        self.parent = parent
        self.root = root
        PATH_ONE = r"./production/view/chat_details.ui"
        try:
            uic.loadUi(PATH_ONE, self)
        except Exception as e:
            print(e)

        self.close_btn.clicked.connect(self.close_tab)

    def initialize(self, chat_id):
        self.chat_id = chat_id
        self.chat_heading.setText(self.chat_id)

    def close_tab(self):
        self.root.hide_chat_details(self.chat_id)


class ChatBar(QWidget):
    def __init__(self, parent=None, root=None):
        super().__init__(parent)
        self.root = root

    def mousePressEvent(self, event):
        # print(self.parent())
        chat_id = self.parent().chat_heading.text()
        # chat_id = "group_one"
        self.root.show_chat_details(chat_id)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBar()
    window.show()
    sys.exit(app.exec_())