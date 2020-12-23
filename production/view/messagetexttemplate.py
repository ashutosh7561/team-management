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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MessageTextTemplate()
    win.show()
    sys.exit(app.exec_())