import threading
import socket
import selectors
import time
import pickle
import sys
from queue import Queue
from os.path import dirname, abspath
import os

# d = dirname(dirname(abspath(__file__)))
# sys.path.append(d)

from header import Packet

try:
    from model.clientdbconnector import ClientDBHandler, ClientDatabaseConnector

    # from model.databaseconnector import *
except Exception as e:
    print(e)


class ServerCon:
    def __init__(self, read_queue, write_queue):
        self.read_queue = read_queue
        self.write_queue = write_queue
        self.SERVER_MAPPING = {
            "identify_user": self.send_credentials,
            "authentication_status": self.authentication_status,
        }
        self.CLIENT_MAPPING = {
            "chat_msg": self.send_chat_message,
            "credentials": self.pass_credentials,
        }
        self.user_id = None
        self.password = None

    def pass_credentials(self, msg_data):
        self.user_id = msg_data["user_id"]
        self.password = msg_data["password"]
        self.send_credentials()

    def authentication_status(self, msg_data):
        is_valid = msg_data["is_valid"]
        post = msg_data["post"]
        user_id = msg_data["user_id"]
        print(msg_data)
        self.write_queue.put(["user_authenticated", is_valid, post, user_id])
        if is_valid:
            self.client_db = ClientDBHandler(self.user_id, self.write_queue)

    def send_credentials(self, msg_data=None):
        print("server asked for credentials")
        if self.user_id is not None:
            dat = {"user_id": self.user_id, "password": self.password}
            self.wrapper.send_data({"msg_type": "credentials", "msg_data": dat}, "obj")

    def delegate_client_message(self, msg):
        msg_type = msg["msg_type"]
        msg_data = msg["msg_data"]
        self.CLIENT_MAPPING[msg_type](msg_data)

    def send_chat_message(self, message):
        user_msg = message[0]
        chat_id = message[1]
        sender_id = message[2]

        dat = {"chat_id": chat_id, "msg_content": user_msg, "sender_id": sender_id}
        ms = {"msg_type": "chat_msg", "msg_data": dat}

        self.wrapper.send_data(ms, "obj")
        try:
            self.client_db.write_chat_message(chat_id, {sender_id: user_msg})
        except Exception as e:
            print(e)

    def check_client_input(self):
        if not (self.read_queue.empty()):
            message = self.read_queue.get()
            self.delegate_client_message(message)

    def delegate_server_message(self, msg):
        msg_type = msg["msg_type"]
        msg_data = msg["msg_data"]
        self.SERVER_MAPPING[msg_type](msg_data)

    def handle_wr(self, key, mask):
        sock = key.fileobj
        if mask & selectors.EVENT_READ:
            try:
                server_msg = self.wrapper.read_data()
                self.delegate_server_message(server_msg)
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
                self.check_client_input()
        except Exception as e:
            print("client closing:", e)
        finally:
            self.event_handler.close()

    def start_connection_thread(self):
        con_thread = threading.Thread(target=self.start_connection)
        con_thread.start()

    def send_some(self, msg, chat_id):
        self.read_queue.put([msg, chat_id, self.user_id])