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

from view.messagetexttemplate import (
    MessageTextTemplate,
    MessageTextRecieveTemplate,
)


class ChatWidgetTemplate(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"./production/view/chat_widget.ui", self)


class MessageCentral(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r"./production/view/message_template_initial.ui", self)


class MessageSidebar(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"./production/view/message_template_sidebar.ui", self)
        self.contact_list.setWidgetResizable(True)
        self.group_list.setWidgetResizable(True)
        self.personal_chat_list.setWidgetResizable(True)

        self.show_chats.clicked.connect(self.switch_to_personalchats)
        self.show_contacts.clicked.connect(self.switch_to_contacts)
        self.show_groups.clicked.connect(self.switch_to_groups)

    def switch_to_groups(self):
        # self.chat_list.setCurrentWidget(self.group_list_page)
        pass

    def switch_to_contacts(self):
        # self.chat_list.setCurrentWidget(self.contact_list_page)
        pass

    def switch_to_personalchats(self):
        self.chat_list.setCurrentWidget(self.personal_chat_list_page)

    def add_group(self, user_list):
        wig = QWidget()
        box = QVBoxLayout()
        for i in user_list:
            gt = ChatWidgetTemplate()
            gt.chat_heading.setText(i)
            box.addWidget(gt)

        wig.setLayout(box)
        self.personal_chat_list.setWidget(wig)


class ChatBoxTemplate(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"./production/view/chat_box_template.ui", self)
        self.chat_heading.setText("Alex")
        self.send.clicked.connect(self.send_message)
        self.bt.clicked.connect(self.recieve_message)
        self.fbor = QWidget()
        self.vbox = QVBoxLayout()
        self.fbor.setLayout(self.vbox)
        self.vbox.addStretch()
        self.chat_message_list.setWidget(self.fbor)

    def resizeEvent(self, event):
        km = iter(self.fbor.children())
        next(km)
        for i in km:
            if isinstance(i, MessageTextTemplate):
                wid = self.set_message_size(i)
                # i.self_evaluate()
            elif isinstance(i, MessageTextRecieveTemplate):
                wid = self.set_message_receive_size(i)
        super().resizeEvent(event)

    def set_message_size(self, msg_widget):
        horizontal_spacer = msg_widget.children()[0].itemAt(0)
        msg_text = msg_widget.message_text
        msg_widget_width = msg_text.fontMetrics().boundingRect(msg_text.text()).width()
        left_bound = self.width() * 0.5

        if msg_widget_width < left_bound:
            msg_text.setWordWrap(False)
            horizontal_spacer.changeSize(
                200, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
            )
        else:
            msg_text.setWordWrap(True)
            horizontal_spacer.changeSize(
                200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
            )
            if msg_widget.message_text.width() >= msg_widget_width:
                msg_text.setWordWrap(False)
                horizontal_spacer.changeSize(
                    200, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
                )

        if msg_widget.width() > self.width():
            msg_text.setWordWrap(True)
            horizontal_spacer.changeSize(
                200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
            )
        horizontal_spacer.invalidate()
        msg_text.updateGeometry()

    def set_message_receive_size(self, msg_widget):
        horizontal_spacer = msg_widget.children()[0].itemAt(1)
        msg_text = msg_widget.message_text
        msg_widget_width = msg_text.fontMetrics().boundingRect(msg_text.text()).width()
        left_bound = self.width() * 0.5

        if msg_widget_width < left_bound:
            msg_text.setWordWrap(False)
            horizontal_spacer.changeSize(
                200, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
            )
        else:
            msg_text.setWordWrap(True)
            horizontal_spacer.changeSize(
                200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
            )
            if msg_widget.message_text.width() >= msg_widget_width:
                msg_text.setWordWrap(False)
                horizontal_spacer.changeSize(
                    200, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
                )

        if msg_widget.width() > self.width():
            msg_text.setWordWrap(True)
            horizontal_spacer.changeSize(
                200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
            )
        horizontal_spacer.invalidate()
        msg_text.updateGeometry()

    def send_message(self):
        msg_text = self.input_field.text()
        m = MessageTextTemplate()
        m.message_text.setText(msg_text)

        self.set_message_size(m)

        self.vbox.addWidget(m)
        self.scroll_to_last()

    def scroll_to_last(self):

        scroll_bar = self.chat_message_list.verticalScrollBar()

        scroll_bar.setMaximum(self.fbor.height())
        scroll_bar.setValue(self.fbor.height())

    def recieve_message(self):
        msg_text = self.input_field.text()
        m = MessageTextRecieveTemplate()
        m.message_text.setText(msg_text)

        self.set_message_receive_size(m)
        self.vbox.addWidget(m)
        self.scroll_to_last()


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi(r"./production/view/message_template.ui", self)
        self.central_window.setCurrentWidget(self.message_initial)
        print(self.central_window.addWidget(ChatBoxTemplate()))
        # self.central_window.setCurrentIndex(1)
        self.message_sidebar = MessageSidebar()
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
        self.message_sidebar.add_group(user_list)

        self.sidebar.layout().addWidget(self.message_sidebar)

        self.message_sidebar.show_contacts.clicked.connect(self.start_screen)
        self.message_sidebar.show_groups.clicked.connect(self.chat_box_screen)

    def start_screen(self):
        self.central_window.setCurrentWidget(self.message_initial)

    def chat_box_screen(self):
        self.central_window.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())