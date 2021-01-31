import time
import sys
from os.path import dirname, abspath
import os

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import multiprocessing as mp
from queue import Queue

from client import ServerCon


class ControllerHandler:
    def __init__(self, view_queue, controller_queue, message_queue, server_queue, con):
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.message_queue = message_queue
        self.server_queue = server_queue
        self.con = con

        self.flag = True
        self.check_for_messages()

    def connect_to_server(self):
        self.con.start_connection_thread()
        # self.view_queue.put(["connection_obj", self.con])
        self.view_queue.put(["connection_obj", None])

    def check_for_messages(self):
        while self.flag:
            message = self.controller_queue.get()
            self.identify_message(message)

    def identify_message(self, message):
        self.message_dict = {
            "load_resources": self.load_resources,
            "admin_get_users_data": self.admin_get_users_data,
            "quit_application": self.quit_application,
            "validate_credentials": self.validate_credentials,
            "user_authenticated": self.authentication_status,
            "admin_users_data": self.admin_users_data,
            "admin_add_new_user": self.admin_add_new_user,
            "chat_msg": self.send_chat_msg,
            "message_queue": self.store_message_queue,
            "ticket_list": self.pass_ticket_list,
        }
        self.message_dict[message[0]](*message[1:])

    def pass_ticket_list(self, msg_data):
        print(msg_data)
        dat = {
            "recepient_list": ["adam_12"],
            "ticket_creator": "alex_11",
            "ticket_heading": "message",
            "ticket_content": "hi",
        }
        # self.server_queue.put({"msg_type": "create_ticket", "msg_data": dat})
        self.server_queue.put({"msg_type": "pick_ticket", "msg_data": {"ticket_id": 9}})
        pass
        # self.view_queue.put(["ticket_list", msg_data])

    def store_message_queue(self, queue):
        # self.message_queue = self.message_queue
        # self.con.message_queue = self.message_queue
        # print(self.con)
        pass

    def send_chat_msg(self, chat_msg, chat_id, sender_id):
        self.server_queue.put(
            {
                "msg_type": "chat_msg",
                "msg_data": [chat_msg, chat_id, sender_id],
            }
        )

    def admin_add_new_user(self, *args):
        self.model_queue.put(["admin_add_new_user", *args])
        self.model_queue.put(["admin_get_users_data"])

    def admin_users_data(self, data):
        self.view_queue.put(["admin_users_data", data])

    def authentication_status(self, is_valid, post, user_id):
        if is_valid:
            self.view_queue.put(["valid_user", post, user_id])
            self.server_queue.put(
                {"msg_type": "ticket_list", "msg_data": {"active": True}}
            )
        else:
            self.view_queue.put(["invalid_user"])

    def validate_credentials(self, user_id, password):
        # self.model_queue.put(["validate_credentials", user_id, password])
        self.server_queue.put(
            {
                "msg_type": "credentials",
                "msg_data": {"user_id": user_id, "password": password},
            }
        )

    def load_resources(self):
        self.connect_to_server()
        # msg = [
        #     "Database",
        #     "Files",
        #     "Settings",
        #     "Settings",
        #     "Dependencies",
        #     "Dependencies",
        #     "Images",
        #     "Projects",
        #     "Calendar",
        #     "Messages",
        #     "Messages",
        # ]
        # for i in range(11):
        #     time.sleep(0.3)
        #     print("loading...", i * 10)
        #     self.view_queue.put(["load_status", i * 10, f"Loading {msg[i]}"])
        print("load complete")
        self.view_queue.put(["load_complete"])
        # self.validate_credentials("adam_12", "adam")

    def admin_get_users_data(self, *args):
        self.model_queue.put(["admin_get_users_data", *args])

    def quit_application(self):
        self.server_queue.put({"msg_type": "action", "msg_data": {"quit": True}})
        self.flag = False


class ControllerHandlerTesting:
    def controller_proc(self, v_q, c_q, m_q):
        c_handler = ControllerHandler(v_q, c_q, m_q)

    def other_proc(self, v_q, c_q, m_q):
        c_q.put(["load_resources"])
        time.sleep(2)
        c_q.put(["validate_credentials", "adam_12", "adam"])
        print("sending chat messages:\n")
        c_q.put(["chat_msg", "hi", "group_one", "adam"])

    def test(self):
        v_q = mp.Queue()
        c_q = mp.Queue()
        m_q = mp.Queue()

        c_proc = mp.Process(
            target=self.controller_proc,
            args=(v_q, c_q, m_q),
        )

        v_proc = mp.Process(
            target=self.other_proc,
            args=(v_q, c_q, m_q),
        )

        v_proc.start()
        c_proc.start()


if __name__ == "__main__":
    ControllerHandlerTesting().test()