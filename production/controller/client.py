import threading
import socket
import selectors
import time
import pickle
from queue import Queue
import os

from header import Packet

# try:
#     from clientdbconnector import ClientDBHandler, ClientDatabaseConnector
# except:
#     try:
#         from controller.chats.sockets.clientdbconnector import (
#             ClientDBHandler,
#             ClientDatabaseConnector,
#         )
#     except Exception as e:
#         print(e)


class ServerCon:
    def __init__(self, read_queue, write_queue):
        self.read_queue = read_queue
        self.write_queue = write_queue
        self.MAPPING = {
            "identify_user": self.send_credentials,
            "authentication_status": self.authentication_status,
        }

    def authentication_status(self, msg_data):
        is_valid = msg_data["is_valid"]
        post = msg_data["post"]
        user_id = msg_data["user_id"]
        print(msg_data)
        self.write_queue.put(["user_authenticated", is_valid, post, user_id])

    def send_credentials(self, msg_data):
        print("server asked for credentials")
        self.user_id = "zed_15"
        self.password = "zed"

        dat = {"user_id": self.user_id, "password": self.password}
        self.wrapper.send_data({"msg_type": "credentials", "msg_data": dat}, "obj")

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

    def delegate_message(self, msg):
        msg_type = msg["msg_type"]
        msg_data = msg["msg_data"]
        self.MAPPING[msg_type](msg_data)

    def handle_wr(self, key, mask):
        sock = key.fileobj
        if mask & selectors.EVENT_READ:
            try:
                server_msg = self.wrapper.read_data()
                self.delegate_message(server_msg)
            except Exception as e:
                print(e)
                print("no data from server")
                print("server might have closed connection")
                sock.close()
                self.event_handler.unregister(sock)
                print("closed socket")

    def start_connection(self):
        HOST = "111.118.242.44"
        HOST = "127.0.0.1"
        PORT = 50000
        PORT = 1030

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

    def start_connection_thread(self):
        con_thread = threading.Thread(target=self.start_connection)
        con_thread.start()

    def send_some(self, msg, chat_id):
        self.read_queue.put([msg, chat_id, self.user_id])
