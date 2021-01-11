import socket
import selectors
import types
from header import Packet
from chatdbconnector import *

HOST = "127.0.0.1"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
sock.setblocking(False)

sel = selectors.DefaultSelector()
sel.register(sock, selectors.EVENT_READ, data=None)


def register_client(sock):
    con, addr = sock.accept()
    con.setblocking(False)
    events = selectors.EVENT_READ
    data = Packet(con)
    sel.register(con, events, data)
    first = {"identify_user": ["user_id", "password"]}
    data.send_data(first, "obj")


client_sockets = {}


def try_sending_buffer_msg(head):
    user_id = head.user_id
    ob = head.ob
    rcv_msg_list = ob.get_messages()

    for group in rcv_msg_list:
        for message in rcv_msg_list[group]:
            dat = {"chat_id": group, "message": message}
            dat = {"buffer_msg": dat}
            head.send_data(dat, "obj")


def clear_msg_buffer(head):
    user_id = head.user_id
    ob = head.ob

    rcv_msg_list = ob.get_messages()

    for group in rcv_msg_list:
        ob.clear_buffer(user_id, group)


def identify_message(msg, head):
    if type(msg) is dict:
        if "credentials" in msg:
            credentials = msg["credentials"]
            user_id = credentials[0]
            password = credentials[1]

            ob = UserStandard(user_id)
            head.bind_socket(user_id, ob)

            in_progress = False
            client_sockets[user_id] = [head, in_progress]

        elif "msg" in msg:
            chat_id = msg["chat_id"]
            msg_data = msg["msg_data"]

            ob = head.ob
            ob.send_message(chat_id, msg_data)
            recipient_list = ob.get_recipient_list(chat_id)
            for i in recipient_list:
                try:
                    is_online = client_sockets[i]
                    if is_online:
                        client_sockets[i][1] = False
                except:
                    pass

        elif "msg_recieved" in msg:
            clear_msg_buffer(head)
            user_id = head.user_id
            client_sockets[user_id][1] = False


def handle_client_request(key, mask):
    sock = key.fileobj
    head = key.data

    if mask & selectors.EVENT_READ:
        try:
            msg = head.read_data()
            identify_message(msg, head)
        except Exception as e:
            print(e)
            print("no data from client")
            print("client might have closed connection")
            del client_sockets[head.user_id]
            sock.close()
            sel.unregister(sock)
            print("closed socket")


def checkout():
    for i in client_sockets:
        head = client_sockets[i][0]
        in_progress = client_sockets[i][1]
        if not in_progress:
            try_sending_buffer_msg(head)
            client_sockets[i][1] = True


try:
    while True:
        events = sel.select(timeout=1)
        checkout()
        for key, mask in events:
            if key.data == None:
                # new client request
                print("new client connection")
                register_client(key.fileobj)
            else:
                handle_client_request(key, mask)
except Exception as e:
    print("server going down:", e)
finally:
    sel.close()