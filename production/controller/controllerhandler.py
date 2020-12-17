import time
import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import multiprocessing as mp


class ControllerHandler:
    def __init__(self, view_queue, controller_queue, model_queue):
        self.view_queue = view_queue
        self.controller_queue = controller_queue
        self.model_queue = model_queue

        print("controller handler up and running")

        self.CHECK_DURATION = 1
        self.flag = True
        self.check_for_messages()

    def check_for_messages(self):
        while self.flag:
            if not (self.controller_queue.empty()):
                message = self.controller_queue.get()
                self.identify_message(message)

            time.sleep(self.CHECK_DURATION)

    def identify_message(self, message):
        self.message_dict = {
            "admin_get_users_data": self.admin_get_users_data,
            "quit_application": self.quit_application,
        }
        self.message_dict[message[0]](*message[1:])

    def admin_get_users_data(self, *args):
        print("users data request from", *args)

    def quit_application(self):
        print("quit application request")
        self.flag = False


class ControllerHandlerTesting:
    def controller_proc(self, v_q, c_q, m_q):
        c_handler = ControllerHandler(v_q, c_q, m_q)

    def other_proc(self, v_q, c_q, m_q):
        print("putting data on queue")
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
    ControllerHandlerTesting().test()