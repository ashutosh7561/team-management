import threading
import socket
import selectors
import time
import pickle
import sys
from queue import Queue
from os.path import dirname, abspath
import os

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from header import Packet

try:
    from model.clientdbconnector import ClientDBHandler, ClientDatabaseConnector

    # from model.databaseconnector import *
except Exception as e:
    print(e)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ServerCon(metaclass=Singleton):
    def __init__(self, read_queue, write_queue, message_queue=None):
        self.read_queue = read_queue
        self.write_queue = write_queue
        self.message_queue = message_queue
        self.flag = True

        self.SERVER_MAPPING = {
            "identify_user": self.send_credentials,
            "authentication_status": self.authentication_status,
            "chat_msg": self.recv_chat_message,
            "ticket_list": self.pass_ticket_list,
            "ticket_response": self.pass_ticket_response,
        }
        self.CLIENT_MAPPING = {
            "chat_msg": self.send_chat_message,
            "credentials": self.pass_credentials,
            "action": self.perform_action,
            "chats_list": self.fetch_all_chats_list,
            "chats_details": self.fetch_all_chats_details,
            "ticket_list": self.fetch_ticket_list,
            "create_ticket": self.create_ticket,
            "pick_ticket": self.pick_ticket,
            "load_local_message": self.load_message,
        }
        self.user_id = None
        self.password = None

    def load_message(self, msg_data):
        self.client_db.get_all_chat_messages()

    def pass_ticket_response(self, msg_data):
        pass
        # self.write_queue.put(["ticket_id", msg_data["ticket_id"]])

    def pass_ticket_list(self, msg_data):
        self.write_queue.put(["ticket_list", msg_data])

    def create_ticket(self, msg_data):
        self.wrapper.send_data(
            {"msg_type": "create_ticket", "msg_data": msg_data}, "obj"
        )

    def pick_ticket(self, msg_data):
        self.wrapper.send_data({"msg_type": "pick_ticket", "msg_data": msg_data}, "obj")

    def fetch_ticket_list(self, msg_data):
        self.wrapper.send_data({"msg_type": "ticket_list", "msg_data": msg_data}, "obj")

    def fetch_all_chats_list(self, msg_data):
        self.client_db.get_all_chats_list()

    def fetch_all_chats_details(self, msg_data):
        self.client_db.get_all_chats_details()
        pass

    def perform_action(self, msg_data):
        self.flag = msg_data["quit"]

    def recv_chat_message(self, msg_data):
        chat_id = msg_data["chat_id"]
        message = msg_data["message"]
        msg_data["recv_msg"] = True
        self.message_queue.put(msg_data)
        self.client_db.write_chat_message(chat_id, {" ": message})
        self.wrapper.send_data({"msg_type": "msg_ack", "msg_data": None}, "obj")

    def pass_credentials(self, msg_data):
        self.user_id = msg_data["user_id"]
        self.password = msg_data["password"]
        self.send_credentials()

    def authentication_status(self, msg_data):
        is_valid = msg_data["is_valid"]
        post = msg_data["post"]
        user_id = msg_data["user_id"]
        self.write_queue.put(["user_authenticated", is_valid, post, user_id])
        if is_valid:
            self.client_db = ClientDBHandler(self.user_id, self.message_queue)
            # self.client_db.get_all_chat_messages()

    def send_credentials(self, msg_data=None):
        if self.user_id is not None:
            dat = {"user_id": self.user_id, "password": self.password}
            self.wrapper.send_data({"msg_type": "credentials", "msg_data": dat}, "obj")

    def delegate_client_message(self, msg):
        msg_type = msg["msg_type"]
        msg_data = msg["msg_data"]
        self.CLIENT_MAPPING[msg_type](msg_data)

    def send_chat_message(self, msg_data):
        user_msg = msg_data[0]
        chat_id = msg_data[1]
        sender_id = msg_data[2]

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
            while self.flag:
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
        self.read_queue.put(
            {"msg_type": "chat_msg", "msg_data": [msg, chat_id, self.user_id]}
        )
        # self.read_queue.put([msg, chat_id, self.user_id])
        # sender_id = self.user_id
        # dat = {"chat_id": chat_id, "msg_content": msg, "sender_id": sender_id}
        # ms = {"msg_type": "chat_msg", "msg_data": dat}
        # self.wrapper.send_data(ms, "obj")
        # try:
        #     self.client_db.write_chat_message(chat_id, {sender_id: msg})
        # except Exception as e:
        #     print(e)

    def get_all_chats_list(self):
        self.read_queue.put({"msg_type": "chats_list", "msg_data": None})

    def get_all_chats_details(self):
        self.read_queue.put({"msg_type": "chats_details", "msg_data": None})

    def load_local_message(self):
        self.read_queue.put({"msg_type": "load_local_message", "msg_data": None})


if __name__ == "__main__":
    c = ServerCon(None, None, None)
    print(c)
    c2 = ServerCon(None, None, None)
    print(c2)