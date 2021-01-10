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


class MessageTextTemplate(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"./production/view/message_text_template.ui", self)

    def self_evaluate(self):
        horizontal_spacer = self.children()[0].itemAt(0)
        msg_text = self.message_text
        msg_widget_width = msg_text.fontMetrics().boundingRect(msg_text.text()).width()
        left_bound = self.parent().width() * 0.5
        print(f"{msg_widget_width} < {left_bound}")
        print(self.message_text.width())
        print("window width:", self.parent(), self.parent().width())

        if msg_widget_width < left_bound:
            print("one liner")
            msg_text.setWordWrap(False)
            horizontal_spacer.changeSize(
                200, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
            )
        else:
            print("multiline")
            msg_text.setWordWrap(True)
            horizontal_spacer.changeSize(
                200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
            )
        horizontal_spacer.invalidate()
        msg_text.updateGeometry()


class MessageTextRecieveTemplate(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"./production/view/message_text_recieve_template.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MessageTextTemplate()
    win.show()
    sys.exit(app.exec_())