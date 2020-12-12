import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import time
import multiprocessing as mp

from view.main import ViewHandler


def ug():
    print("starting gui process")
    time.sleep(3)
    view = ViewHandler()
    view.start_app()


def mock_preloading():
    # it will function as loading resources
    # start loading
    # start splash screen
    view = ViewHandler()
    gui_proc = mp.Process(target=ug)
    gui_proc.start()
    # it passes the percentage completion to view
    # view.start_splash_screen()
    for i in range(101):
        print(i)
        time.sleep(0.1)  # mock loading
        # view.load_status(i)
    view.stop_app()
    # view.close_splash_screen()
    # view.show_login_window()
    # finished loading
    # close splash_screen
    # open login window
    pass


if __name__ == "__main__":
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
    mock_preloading()
    pass
