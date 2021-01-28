import sys
import time
from os.path import abspath, dirname
import os

# d = dirname(dirname(abspath(__file__)))
# sys.path.append(d)

import multiprocessing as mp

# from model.databaseconnector import DatabaseConnector
# from model.validator import Validator

# Hanlders including Model, View, and Controller will only contain
# functionality to check for messages, identify them and call
# appropriate method. These methods wont contain any other logic.
# At present it contains these logic but will be removed in further
# versions.
# Instead of creating seperate methods inside handler which then
# further calls other methods of some objects we might directly
# bind those methods to the messages to avoid code duplication.
class ModelHandler:
    def __init__(self, view_queue, controller_queue, model_queue):
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue

        # print("model handler up and running")

        self.flag = True
        # self.validator = Validator()
        # self.db = DatabaseConnector()
        self.check_for_messages()

    def check_for_messages(self):
        while self.flag:
            message = self.model_queue.get()
            self.identify_message(message)

    def identify_message(self, message):
        self.message_dict = {
            "admin_get_users_data": self.admin_get_users_data,
            "quit_application": self.quit_application,
            "validate_credentials": self.validate_credentials,
            "get_access_rights": self.db.get_user_rights,
            "create_post": self.validator.create_post,
            "change_post_rights": self.change_post_rights,
            "change_user_password": self.validator.change_user_password,
            "get_available_access_rights": self.db.get_available_access_rights,
            "get_access_rights_for_post": self.db.get_access_rights_for_post,
            "get_user_post": self.db.get_user_post,
            "admin_add_new_user": self.validator.add_user,
            "change_user_post": self.db.change_user_post,
            "change_username": self.db.change_username,
        }
        self.message_dict[message[0]](*message[1:])

    def change_post_rights(self, post_name, associated_rights):
        pass

    def create_post(self, post_name, *args):
        pass

    def get_access_rights(self, user_id):
        self.controller_queue.put(
            ["user_access_rights", user_id, self.validator.get_access_rights(user_id)]
        )

    def validate_credentials(self, user_id, password):
        if self.validator.validate_user(user_id, password):
            self.controller_queue.put(
                ["user_authenticated", True, self.db.get_user_post(user_id), user_id]
            )
        else:
            self.controller_queue.put(["user_authenticated", False, None, user_id])

    def admin_get_users_data(self, *args):
        self.controller_queue.put(["admin_users_data", self.validator.get_users_data()])

    def quit_application(self):
        # print("quit application request")
        self.flag = False


class ModelHandlerTesting:
    def model_proc(self, v_q, c_q, m_q):
        m_handler = ModelHandler(v_q, c_q, m_q)

    def controller_proc(self, v_q, c_q, m_q):
        # print("putting data on queue")
        m_q.put(["admin_get_users_data", "alex", "admin"])
        m_q.put(["validate_credentials", "11", "alex"])
        m_q.put(["validate_credentials", "12", "adam"])
        m_q.put(["validate_credentials", "13", "jack"])
        m_q.put(["validate_credentials", "14", "john"])
        m_q.put(["validate_credentials", "15", "zed"])
        while True:
            if not (c_q.empty()):
                masg = c_q.get()
                if masg[0] == "user_authenticated" and masg[1] == True:
                    m_q.put(["get_access_rights", masg[2]])
                elif masg[0] == "user_access_rights":
                    print(masg)
        # print("other processs quiting")
        m_q.put(["quit_application"])

    def test(self):
        v_q = mp.Queue()
        c_q = mp.Queue()
        m_q = mp.Queue()

        c_proc = mp.Process(
            target=self.model_proc,
            args=(v_q, c_q, m_q),
        )

        v_proc = mp.Process(
            target=self.controller_proc,
            args=(v_q, c_q, m_q),
        )

        v_proc.start()
        c_proc.start()


if __name__ == "__main__":
    ModelHandlerTesting().test()
