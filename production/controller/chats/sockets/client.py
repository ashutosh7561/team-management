import threading
import socket
import selectors
import time
from header import Packet
import pickle

HOST = "127.0.0.1"
PORT = 65432

sel = selectors.DefaultSelector()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(False)
sock.connect_ex((HOST, PORT))
sel.register(sock, selectors.EVENT_READ, data="client")

p = Packet(sock)


def handle_wr(key, mask):
    global p
    sock = key.fileobj
    if mask & selectors.EVENT_READ:
        try:
            server_msg = p.read_data()
            print("[Server Response]:", server_msg)
        except Exception as e:
            print("no data from server")
            print("server might have closed connection")
            sock.close()
            sel.unregister(sock)
            print("closed socket")


# this flag can be set to true by some other thread which accepts input from user
flag = False
shared_memory = []


def check_for_input():
    global flag
    if flag:
        user_msg = shared_memory.pop()
        if type(user_msg) is dict:
            p.send_data(user_msg, "obj")
        elif type(user_msg) is str:
            p.send_data(user_msg, "txt")
        flag = False


def con():
    try:
        while True:
            events = sel.select(timeout=1)
            check_for_input()
            if events:
                for key, mask in events:
                    handle_wr(key, mask)
            if not sel.get_map():
                break
    except Exception as e:
        print("client closing:", e)
    finally:
        sel.close()


def chat():
    global flag, shared_memory
    user_id = str(input("user_id:"))
    password = str(input("password:"))
    shared_memory.append({"credetials": [user_id, password]})
    flag = True
    do_more = True
    while do_more:
        x = input()
        if x == "user_quit":
            do_more = False
        else:
            shared_memory.append(x)
            flag = True


if __name__ == "__main__":
    ui_thread = threading.Thread(target=chat)
    con_thread = threading.Thread(target=con)

    ui_thread.start()
    con_thread.start()

    ui_thread.join()
    con_thread.join()

    print("user exiting")