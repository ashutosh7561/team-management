import sys
from os.path import dirname, abspath
import os

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import time
import multiprocessing as mp

from view.main import ViewHandler
from controller.controllerhandler import ControllerHandler
from model.modelhandler import ModelHandler
from controller.client import ServerCon
from multiprocessing.managers import BaseManager


from queue import Queue

queue = Queue()


class QueueManager(BaseManager):
    pass


view_queue = mp.Queue()
controller_queue = mp.Queue()
message_queue = mp.Queue()
server_queue = mp.Queue()
con = ServerCon(server_queue, controller_queue, message_queue)


def host():
    QueueManager.register("get_viewq", callable=lambda: view_queue)
    QueueManager.register("get_conq", callable=lambda: controller_queue)
    QueueManager.register("get_messageq", callable=lambda: message_queue)
    QueueManager.register("get_serverq", callable=lambda: server_queue)
    QueueManager.register("get_con", callable=lambda: con)
    m = QueueManager(address=("127.0.0.1", 50000), authkey=b"something_random")
    m.get_server().serve_forever()


def root():
    view_process = mp.Process(
        target=view,
        name="view process",
    )
    controller_process = mp.Process(
        target=controller,
        name="controller process",
    )
    view_process.start()
    controller_process.start()

    view_process.join()
    controller_process.join()


def view():
    QueueManager.register("get_viewq")
    QueueManager.register("get_conq")
    QueueManager.register("get_messageq")
    QueueManager.register("get_serverq")
    QueueManager.register("get_con")
    m = QueueManager(address=("127.0.0.1", 50000), authkey=b"something_random")
    m.connect()
    view_queue = m.get_viewq()
    controller_queue = m.get_conq()
    message_queue = m.get_messageq()
    server_queue = m.get_serverq()
    con = m.get_con()

    view = ViewHandler(view_queue, controller_queue, message_queue, server_queue, con)
    controller_queue.put(["quit_application"])


def controller():
    QueueManager.register("get_viewq")
    QueueManager.register("get_conq")
    QueueManager.register("get_messageq")
    QueueManager.register("get_serverq")
    QueueManager.register("get_con")
    m = QueueManager(address=("127.0.0.1", 50000), authkey=b"something_random")
    m.connect()
    view_queue = m.get_viewq()
    controller_queue = m.get_conq()
    message_queue = m.get_messageq()
    server_queue = m.get_serverq()
    con = m.get_con()

    controller = ControllerHandler(
        view_queue, controller_queue, message_queue, server_queue, con
    )


if __name__ == "__main__":
    h = mp.Process(target=host)
    h.start()
    root()


# if __name__ == "__main__":
# start application with splash screen and in background load the essential components
# after loding all resources close splash screen and open Login Window
# on clicking login it sends data to controller which then requests model to authenticate it
# if credentials are wrong model returns the appropriate message to controller
# controller then informs view that credentials are invalid so view updates the gui by
# deleting entry in the fileds and changing borders of textinput to red
# if credentials are correct model informs controller the same. Controller then requests
# the model for additional data related to user. Model returns the data by fetching it from
# database. Controller then tells view that user is valid and hence tells view to close the
# login window and open the Main window. It provides view the data to be shown in the
# Main window.
# The model, view, and controller are seperate processes and these communicate via special
# queues that are used between them to put and get data. The sender process puts data on
# inteded reciever's queue. The reciever then gets the data from that queue.
# mock_preloading()
# pass


# we are using multiple process because we want the application to run in background like a
# daemon process which will be used to provide some functionality like reminders. If we do
# not use seperate process then after quiting the application it wont be able to remind user.
# here we use queues to pass messages. if we do not use multiple process then we would have
# to pass controller/view/model objects.