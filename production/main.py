import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import multiprocessing as mp
import time


def root():
    print("root process")
    root_conn_view, view_conn = mp.Pipe(duplex=True)
    root_conn_controller, controller_conn = mp.Pipe(duplex=True)
    root_conn_model, model_conn = mp.Pipe(duplex=True)

    view_process = mp.Process(target=view, args=(view_conn,))
    controller_process = mp.Process(target=controller, args=(controller_conn,))
    model_process = mp.Process(target=model, args=(model_conn,))

    controller_process.start()
    view_process.start()
    model_process.start()

    # while root_conn_controller.recv() != 100:
    #     pass
    # root_conn_view.send(100)

    t = root_conn_controller.recv()
    while t < 100:
        t = root_conn_controller.recv()
        root_conn_view.send(t)

    controller_process.join()
    view_process.join()
    model_process.join()

    print("doing cleanpup")
    time.sleep(5)


def view(handle):
    valv = handle.recv()
    while valv != 100:
        print("simulating event loop", "percentage completion", "-" * valv)
        # time.sleep(1)
        valv = handle.recv()
    for i in range(10):
        print("hey wait for me")
        time.sleep(1)


def controller(handle):
    print("controller process")
    print("doing preloading")
    for i in range(11):
        handle.send(i * 10)
        # print(i * 10)
        time.sleep(1)
    # handle.send("i have loaded")
    print("controller ready")


def model(handle):
    print("model process")


if __name__ == "__main__":
    root_process = mp.Process(target=root)
    root_process.start()
    root_process.join()