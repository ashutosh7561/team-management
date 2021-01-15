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


class ServerCon:
    def __init__(self, read_queue, write_queue):
        self.read_queue = read_queue
        self.write_queue = write_queue

    def check_for_input(self):
        if not (self.read_queue.empty()):
            message = self.read_queue.get()
            sender_id = message[0]
            user_msg = message[1]
            chat_id = message[2]

            if type(user_msg) is str:
                pac = {
                    "msg": True,
                    "sender_id": sender_id,
                    "chat_id": chat_id,
                    "msg_data": user_msg,
                }
                pac = {
                    "msg": True,
                    "chat_id": chat_id,
                    "msg_data": {"sender_id": sender_id, "msg": user_msg},
                }
                self.p.send_data(pac, "obj")

    def identify_message(self, msg, head):
        if type(msg) is dict:

            if "identify_user" in msg:
                head.send_data({"credentials": [self.user_id, self.password]}, "obj")

            if "buffer_msg" in msg:
                self.write_queue.put(msg)
                ok_msg = {"msg_recieved": True}
                self.p.send_data(ok_msg, "obj")

    def handle_wr(self, key, mask):
        sock = key.fileobj
        if mask & selectors.EVENT_READ:
            try:
                server_msg = self.p.read_data()
                self.identify_message(server_msg, self.p)
            except Exception as e:
                print("no data from server")
                print("server might have closed connection")
                sock.close()
                self.sel.unregister(sock)
                print("closed socket")

    def start_connection(self, queue):
        HOST = "127.0.0.1"
        PORT = 65432

        self.sel = selectors.DefaultSelector()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex((HOST, PORT))
        self.sel.register(sock, selectors.EVENT_READ, data="client")

        self.p = Packet(sock)
        try:
            while True:
                events = self.sel.select(timeout=1)
                if events:
                    for key, mask in events:
                        self.handle_wr(key, mask)
                if not self.sel.get_map():
                    break
                self.check_for_input()
        except Exception as e:
            print("client closing:", e)
        finally:
            self.sel.close()

    def start_connection_thread(self, user_id, password):

        self.user_id = user_id
        self.password = password

        con_thread = threading.Thread(
            target=self.start_connection, args=(self.read_queue,)
        )

        con_thread.start()

    def send_some(self, msg, chat_id):
        self.read_queue.put([msg, chat_id])


if __name__ == "__main__":
    q = Queue()
    q2 = Queue()
    h = ServerCon(q, q2)
    h.start_connection_thread("alex_11", "qwer")
    # h.send_some("some msg", "group_one")