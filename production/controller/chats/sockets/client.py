import threading
import socket
import selectors
import time
from queue import Queue

try:
    from controller.chats.sockets.header import Packet
except:
    from header import Packet

try:
    from clientdbconnector import ClientDBHandler, ClientDatabaseConnector
except:
    from controller.chats.sockets.clientdbconnector import (
        ClientDBHandler,
        ClientDatabaseConnector,
    )

import pickle


class ServerCon:
    def __init__(self, read_queue, write_queue):
        self.read_queue = read_queue
        self.write_queue = write_queue

    def check_for_updates(self):
        if not (self.read_queue.empty()):
            message = self.read_queue.get()
            user_msg = {"message": message[0], "sender_id": message[2]}
            chat_id = message[1]

            pac = {
                "msg": True,
                "chat_id": chat_id,
                "msg_data": user_msg,
            }
            self.wrapper.send_data(pac, "obj")
            self.client_db.write_chat_message(chat_id, {message[2]: message[0]})

    def identify_message(self, msg):
        if "identify_user" in msg:
            self.wrapper.send_data(
                {"credentials": [self.user_id, self.password]}, "obj"
            )

        if "buffer_msg" in msg:
            msg = msg["buffer_msg"]

            chat_id = msg["chat_id"]
            msg = msg["message"]
            sender_id = msg["sender_id"]
            main_msg = msg["message"]
            final_msg = {sender_id: main_msg}

            self.client_db.write_chat_message(chat_id, final_msg)
            # self.write_queue.put(final_msg)
            ok_msg = {"msg_recieved": True}
            self.wrapper.send_data(ok_msg, "obj")

    def handle_wr(self, key, mask):
        sock = key.fileobj
        if mask & selectors.EVENT_READ:
            try:
                server_msg = self.wrapper.read_data()
                self.identify_message(server_msg)
            except Exception as e:
                print("no data from server")
                print("server might have closed connection")
                sock.close()
                self.event_handler.unregister(sock)
                print("closed socket")

    def start_connection(self):
        HOST = "127.0.0.1"
        PORT = 65432

        self.client_db = ClientDBHandler(self.user_id, self.write_queue)
        self.event_handler = selectors.DefaultSelector()

        main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        main_socket.setblocking(False)
        main_socket.connect_ex((HOST, PORT))
        self.event_handler.register(main_socket, selectors.EVENT_READ, data="client")

        self.wrapper = Packet(main_socket)

        try:
            while True:
                events = self.event_handler.select(timeout=1)
                if events:
                    for key, mask in events:
                        self.handle_wr(key, mask)
                if not self.event_handler.get_map():
                    break
                self.check_for_updates()
        except Exception as e:
            print("client closing:", e)
        finally:
            self.event_handler.close()

    def start_connection_thread(self, user_id, password):

        self.user_id = user_id
        self.password = password

        self.client_tmdb = ClientDBHandler(self.user_id, self.write_queue)
        self.client_tmdb.get_all_chat_messages()

        con_thread = threading.Thread(target=self.start_connection)

        con_thread.start()

    def send_some(self, msg, chat_id):
        self.read_queue.put([msg, chat_id, self.user_id])


if __name__ == "__main__":
    q = Queue()
    q2 = Queue()
    h = ServerCon(q, q2)
    # h.start_connection_thread("alex_11", "qwer")
    # h.send_some("new message from alex_11", "group_one")
    # h.send_some("message1 from adam_12 for group_two", "group_two")
    # h.send_some("message2 from adam_12 for group_two", "group_two")
    # h.send_some("message3 from adam_12 for group_two", "group_two")

    # h.start_connection_thread("peter_13", "qwer")