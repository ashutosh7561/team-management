import threading
import socket
import selectors
import time
from queue import Queue

try:
    from controller.chats.sockets.header import Packet
except:
    from header import Packet

import pickle

# this flag can be set to true by some other thread which accepts input from user
shared_queue = Queue()

flag = False
shared_memory = []
p = None
sel = None


def check_for_input():
    global flag
    if flag:
        user_msg = shared_memory.pop()
        chat_id = user_msg[1]
        user_msg = user_msg[0]

        if type(user_msg) is str:
            pac = {"msg": True, "chat_id": chat_id, "msg_data": user_msg}
            p.send_data(pac, "obj")
        flag = False


def identify_message(msg, head):
    if type(msg) is dict:
        if "identify_user" in msg:
            head.send_data({"credentials": [user_id, password]}, "obj")
            print("asked for verification")
    else:
        print(msg)
        ok_msg = {"msg_recieved": True}
        p.send_data(ok_msg, "obj")


def handle_wr(key, mask):
    global p
    sock = key.fileobj
    if mask & selectors.EVENT_READ:
        try:
            server_msg = p.read_data()
            identify_message(server_msg, p)
        except Exception as e:
            print("no data from server")
            print("server might have closed connection")
            sock.close()
            sel.unregister(sock)
            print("closed socket")


def start_connection():
    HOST = "127.0.0.1"
    PORT = 65432

    global sel
    sel = selectors.DefaultSelector()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex((HOST, PORT))
    sel.register(sock, selectors.EVENT_READ, data="client")

    global p
    p = Packet(sock)
    try:
        while True:
            events = sel.select(timeout=1)
            if events:
                for key, mask in events:
                    handle_wr(key, mask)
            if not sel.get_map():
                break
            check_for_input()
    except Exception as e:
        print("client closing:", e)
    finally:
        sel.close()


def chat():
    global flag, shared_memory
    do_more = True
    while do_more:
        x, y = input().split(" ")
        if x == "user_quit":
            do_more = False
        else:
            shared_memory.append([x, y])
            flag = True


class ServerCon:
    def connect_to_server(self, usr_id, pswd):
        # ui_thread = threading.Thread(target=chat)
        global user_id, password
        user_id = usr_id
        password = pswd
        con_thread = threading.Thread(target=start_connection)

        # ui_thread.start()
        con_thread.start()

        # ui_thread.join()
        # con_thread.join()

        # print("user exiting")

    def send_some(self, msg, chat_id):
        global flag, shared_memory
        shared_memory.append([msg, chat_id])
        flag = True


if __name__ == "__main__":
    user_id = str(input("user_id:"))
    password = str(input("password:"))
    ui_thread = threading.Thread(target=chat)
    con_thread = threading.Thread(target=start_connection)

    ui_thread.start()
    con_thread.start()

    ui_thread.join()
    con_thread.join()

    print("user exiting")
    # h = ServerCon()
    # h.connect_to_server("alex_11", "asdf")
    # h.send_some("asdf", "group_one")