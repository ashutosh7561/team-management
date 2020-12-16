import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import time
import multiprocessing as mp

from view.main import ViewHandler


def root():
    print("root process")
    view_queue = mp.Queue()
    controller_queue = mp.Queue()
    model_queue = mp.Queue()
    root_queue = mp.Queue()

    view_process = mp.Process(
        target=view,
        args=(
            view_queue,
            controller_queue,
            model_queue,
            root_queue,
        ),
    )
    controller_process = mp.Process(
        target=controller,
        args=(
            view_queue,
            controller_queue,
            model_queue,
            root_queue,
        ),
    )
    model_process = mp.Process(
        target=model,
        args=(
            view_queue,
            controller_queue,
            model_queue,
            root_queue,
        ),
    )

    view_process.start()
    controller_process.start()
    model_process.start()

    view_process.join()
    controller_process.join()
    model_process.join()

    print("doing cleanpup")


def view(view_queue, controller_queue, model_queue, root_queue):
    print("starting view process")
    view = ViewHandler(view_queue, controller_queue, model_queue)
    print("exit from app.exec_() event loop")
    controller_queue.put(["quit_application"])
    model_queue.put(["quit_application"])


def controller(view_queue, controller_queue, model_queue, root_queue):
    print("starting controller process")
    # create ControllerHandler class similar to ViewHandler which
    # will handle messages and other stuff
    print("mock loading")
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
        print("loading...", i * 10)
        view_queue.put(["load_status", i * 10, f"Loading {msg[i]}"])
    print("load complete")
    view_queue.put(["load_complete", 1])
    flag = True

    # event loop for controller to check for messages
    while flag:
        time.sleep(1)
        if not (controller_queue.empty()):
            msg = controller_queue.get()
            if msg[0] == "credential_data_request":
                print("credential data request from view handled by controller")
                print("passing request to model")
                model_queue.put(msg)
            if msg[0] == "credential_data":
                print("got data from model")
                print("passing data to view")
                view_queue.put(msg)
            elif msg[0] == "quit_application":
                flag = False
    print("controller is quiting")


def model(view_queue, controller_queue, model_queue, root_queue):
    print("starting model process")
    flag = True

    # event loop for model to check for messages
    while flag:
        time.sleep(1)
        if not (model_queue.empty()):
            msg = model_queue.get()
            if msg[0] == "credential_data_request":
                print("credential data request from controller")
                print("fetching data from database")
                time.sleep(5)
                print("sending data to controller")
                controller_queue.put(["credential_data", 10])
            elif msg[0] == "quit_application":
                flag = False
    print("model quiting")


if __name__ == "__main__":
    root_process = mp.Process(target=root)
    root_process.start()
    root_process.join()


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