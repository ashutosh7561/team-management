import sys
from os.path import abspath, dirname

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)


import platform
import time
import os
from queue import Queue

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
from view.chatbar import ChatDetails
from controller.client import ServerCon


def check_for_file(PATH_ONE, PATH_TWO):
    # print("\n\n\nfile path:")
    # print(os.getcwd())
    if os.path.isfile(PATH_ONE):
        return PATH_ONE
    elif os.path.isfile(PATH_TWO):
        return PATH_TWO
    else:
        raise FileNotFoundError


class ChatWidgetTemplate(QWidget):
    def __init__(self, parent=None, root=None):
        super().__init__(parent)
        self.root = root
        PATH_ONE = r"./production/view/chat_widget.ui"
        PATH_TWO = r""
        try:
            file = check_for_file(PATH_ONE, PATH_TWO)
            uic.loadUi(file, self)
        except Exception as e:
            print(e)

    def mousePressEvent(self, event):
        chat_id = self.chat_heading.text()
        self.root.change_chat(chat_id)


class MessageCentral(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        PATH_ONE = r"./production/view/message_template_initial.ui"
        PATH_TWO = r""
        try:
            file = check_for_file(PATH_ONE, PATH_TWO)
            uic.loadUi(file, self)
        except Exception as e:
            print(e)
        # self.chat_heading.clicked.connect(self.callback)


class MessageSidebar(QWidget):
    def __init__(self, parent=None, root=None):
        super().__init__(parent)
        self.root = root
        PATH_ONE = r"./production/view/message_template_sidebar.ui"
        PATH_TWO = r""
        try:
            file = check_for_file(PATH_ONE, PATH_TWO)
            uic.loadUi(file, self)
        except Exception as e:
            print(e)
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
            gt = ChatWidgetTemplate(parent=self, root=self.root)
            gt.chat_heading.setText(i)
            box.addWidget(gt)

        wig.setLayout(box)
        self.personal_chat_list.setWidget(wig)


class ChatBoxTemplate(QWidget):
    def __init__(self, servcon, chat_heading, parent=None, root=None):
        super().__init__(parent)
        self.root = root
        PATH_ONE = r"./production/view/chat_box_template.ui"
        PATH_TWO = r""
        try:
            file = check_for_file(PATH_ONE, PATH_TWO)
            uic.loadUi(file, self)
        except Exception as e:
            print(e)

        self.servcon = servcon

        self.chat_heading.setText(chat_heading)
        self.send.clicked.connect(self.send_message)
        # self.bt.clicked.connect(self.recieve_message)
        self.fbor = QWidget()
        self.vbox = QVBoxLayout()
        self.fbor.setLayout(self.vbox)
        self.vbox.addStretch()
        self.chat_message_list.setWidget(self.fbor)
        self.chat_group_info.root = self.root

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
        self.load_send_message(msg_text)
        self.servcon.send_some(msg_text, self.chat_heading.text())

    def load_send_message(self, msg_text):
        m = MessageTextTemplate()
        m.message_text.setText(msg_text)

        self.set_message_size(m)

        self.vbox.addWidget(m)
        self.scroll_to_last()

    def scroll_to_last(self):

        scroll_bar = self.chat_message_list.verticalScrollBar()

        scroll_bar.setMaximum(self.fbor.height())
        scroll_bar.setValue(self.fbor.height())

    def load_recieve_message(self, msg_text):
        m = MessageTextRecieveTemplate()
        m.message_text.setText(msg_text)

        self.set_message_receive_size(m)
        self.vbox.addWidget(m)
        self.scroll_to_last()


class Main(QWidget):
    def __init__(self, read_queue, servcon, parent=None):
        super(Main, self).__init__(parent)
        PATH_ONE = r"./production/view/message_template.ui"
        PATH_TWO = r""
        try:
            file = check_for_file(PATH_ONE, PATH_TWO)
            uic.loadUi(file, self)
        except Exception as e:
            print(e)

        self.CHECK_DURATION = 50
        self.read_queue = read_queue
        self.servcon = servcon

        # self.tw = ChatDetails(parent=self.central_window, root=self)
        # self.central_window.addWidget(self.tw)

        self.message_sidebar = MessageSidebar(parent=self.sidebar, root=self)
        user_list = [
            "group_one",
            "group_two",
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

        self.chat_list_widgets = {}

        # self.populate_chat_widgets(user_list)

        # self.message_sidebar.add_group(user_list)

        self.sidebar.layout().addWidget(self.message_sidebar)

        self.message_sidebar.show_contacts.clicked.connect(self.start_screen)
        self.message_sidebar.show_groups.clicked.connect(self.chat_box_screen)

        self.message_sidebar.show_groups.clicked.connect(
            lambda: self.central_window.setCurrentWidget(self.tw)
        )
        try:
            self.servcon.get_all_chats_list()
            self.servcon.get_all_chats_details()
        except Exception as e:
            print(e)

        QtCore.QTimer.singleShot(self.CHECK_DURATION, self.check_for_messages)

    def identify_message(self, message):
        if isinstance(message, dict):
            try:
                if "send_msg" in message:
                    chat_id = message["chat_id"]
                    msg_text = message["message"]
                    # print(msg_text)
                    if msg_text == "":
                        return
                    try:
                        wg = self.chat_list_widgets[chat_id][0]
                        wg.load_send_message(msg_text)
                        # wg.recieve_message(msg_text)
                    except Exception as e:
                        print(e)
                elif "recv_msg" in message:
                    chat_id = message["chat_id"]
                    msg_text = message["message"]
                    # print("recv", msg_text)
                    if msg_text == "":
                        return
                    try:
                        wg = self.chat_list_widgets[chat_id][0]
                        wg.load_recieve_message(msg_text)
                        # wg.recieve_message(msg_text)
                    except Exception as e:
                        print(e)
                elif "chats_list" in message:
                    chats_list = message["list"]
                    self.message_sidebar.add_group(chats_list)

                elif "chats_list_detail" in message:
                    chats_list = message["list"]
                    chats_list_details = message["list_two"]
                    self.populate_chat_widgets(chats_list)
                    # self.update_chat_details(chats_list_details)
            except Exception as e:
                print(e)

    def check_for_messages(self):
        if not (self.read_queue.empty()):
            message = self.read_queue.get()
            self.identify_message(message)

        QtCore.QTimer.singleShot(self.CHECK_DURATION, self.check_for_messages)

    def start_screen(self):
        self.central_window.setCurrentWidget(self.message_initial)

    def chat_box_screen(self):
        self.central_window.setCurrentIndex(1)

    def populate_chat_widgets(self, user_list):
        for i in user_list:
            wg = ChatBoxTemplate(
                servcon=self.servcon,
                chat_heading=i,
                parent=self.central_window,
                root=self,
            )
            self.chat_list_widgets[i] = [None, None]
            self.chat_list_widgets[i][0] = wg
            self.central_window.addWidget(wg)
        self.servcon.load_local_message()

    def update_chat_details(self, chats_list):
        for i in chats_list:
            tg = ChatDetails(parent=self.central_window, root=self)
            chat_id = i["chat_id"]
            chat_desc = i["chat_desc"]
            chat_icon = i["chat_icon"]
            tg.initialize(
                chat_id=chat_id, chat_desc=chat_desc, chat_icon=chat_icon
            )  # pass other details like group_desc, group_icon also.Delete this comment if done
            self.chat_list_widgets[chat_id][1] = tg
            self.central_window.addWidget(tg)

    def change_chat(self, chat_id):
        wg = self.chat_list_widgets[chat_id][0]
        self.central_window.setCurrentWidget(wg)

    def show_chat_details(self, chat_id):
        chat_detail = self.chat_list_widgets[chat_id][1]
        self.central_window.setCurrentWidget(chat_detail)

    def hide_chat_details(self, chat_id):
        chat_widget = self.chat_list_widgets[chat_id][0]
        self.central_window.setCurrentWidget(chat_widget)


if __name__ == "__main__":
    queue_one = Queue()  # used for sending messages
    queue_two = Queue()  # used for receiving messages

    user_id = "alex_11"
    password = "alex"

    con = ServerCon(queue_one, queue_two)
    con.start_connection_thread(user_id, password)

    app = QApplication(sys.argv)
    win = Main(queue_two, con)
    win.show()
    sys.exit(app.exec_())