import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import multiprocessing as mp
import time


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
    time.sleep(3)
    print("view process")
    while not (view_queue.empty()):
        print("view queue :", view_queue.get())
        time.sleep(1)


def controller(view_queue, controller_queue, model_queue, root_queue):
    time.sleep(1)
    print("controller process")
    for i in range(12, 21):
        if controller_queue.empty():
            print("waiting for model to put data")
        j = controller_queue.get()
        print(f"putting {i * j} in view_queue")
        view_queue.put(i * j)
        time.sleep(1)


def model(view_queue, controller_queue, model_queue, root_queue):
    time.sleep(2)
    print("model process")
    for i in range(10):
        controller_queue.put(i)
        print(f"putting {i} in controller_queue")
        time.sleep(1)


if __name__ == "__main__":
    root_process = mp.Process(target=root)
    root_process.start()
    root_process.join()