import time
import sys
from os.path import dirname, abspath
import os

# d = dirname(dirname(abspath(__file__)))
# sys.path.append(d)

import multiprocessing as mp

with open(str(os.getpid()) + ".txt", "a+") as f:
    f.write("imported controllerhandler.py successfully\n")


class ControllerHandler:
    def __init__(self, view_queue, controller_queue, model_queue):
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue

        # print("controller handler up and running")

        self.flag = True
        self.check_for_messages()

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
        }
        self.message_dict[message[0]](*message[1:])

    def admin_add_new_user(self, *args):
        self.model_queue.put(["admin_add_new_user", *args])
        self.model_queue.put(["admin_get_users_data"])

    def admin_users_data(self, data):
        self.view_queue.put(["admin_users_data", data])

    def authentication_status(self, is_valid, post, user_id):
        if is_valid:
            # print(post)
            self.view_queue.put(["valid_user", post, user_id])
        else:
            self.view_queue.put(["invalid_user"])

    def validate_credentials(self, user_id, password):
        self.model_queue.put(["validate_credentials", user_id, password])

    def load_resources(self):
        msg = [
            "Database",
            "Files",
            "Settings",
            "Settings",
            "Dependencies",
            "Dependencies",
            "Images",
            "Projects",
            "Calendar",
            "Messages",
            "Messages",
        ]
        for i in range(11):
            time.sleep(0.3)
            # print("loading...", i * 10)
            self.view_queue.put(["load_status", i * 10, f"Loading {msg[i]}"])
        # print("load complete")
        self.view_queue.put(["load_complete"])

    def admin_get_users_data(self, *args):
        self.model_queue.put(["admin_get_users_data", *args])

    def quit_application(self):
        # print("quit application request")
        self.flag = False


class ControllerHandlerTesting:
    def controller_proc(self, v_q, c_q, m_q):
        c_handler = ControllerHandler(v_q, c_q, m_q)

    def other_proc(self, v_q, c_q, m_q):
        # print("putting data on queue")
        c_q.put(["admin_get_users_data", "alex", "admin", "root"])
        c_q.put(["quit_application"])

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
    # ControllerHandlerTesting().test()
    pass