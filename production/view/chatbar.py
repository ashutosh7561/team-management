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

    def initialize(self, chat_id, chat_desc, chat_icon):
        self.chat_id = chat_id
        if type(chat_desc) == bytes:
            chat_desc = chat_desc.decode("utf-8")
        self.chat_heading.setText(self.chat_id)
        # self.chat_heading2.set_message_receive_size
        self.chat_desc.setText(chat_desc)

    def close_tab(self):
        self.root.hide_chat_details(self.chat_id)


class ChatBar(QWidget):
    def __init__(self, parent=None, root=None):
        super().__init__(parent)
        self.root = root

    def mousePressEvent(self, event):
        chat_id = self.parent().chat_heading.text()
        self.root.show_chat_details(chat_id)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBar()
    window.show()
    sys.exit(app.exec_())
