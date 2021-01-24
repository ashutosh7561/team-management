import socket
import selectors
import types

try:
    from header import Packet
except:
    try:
        from serverside.header import Packet
    except Exception as e:
        print(e)

from validator import Validator
from databaseconnector import DatabaseConnector
from chatdbconnector import ChatDatabaseConnector, UserStandard

HOST = "192.168.1.6"
HOST = "127.0.0.1"
PORT = 1030

event_handler = selectors.DefaultSelector()

main_listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_listening_socket.bind((HOST, PORT))
main_listening_socket.setblocking(False)
main_listening_socket.listen(5)
event_handler.register(main_listening_socket, selectors.EVENT_READ, data=None)

active_client_sockets = {}


def verify_user(wrapper):
    first = {"msg_type": "identify_user", "msg_data": None}
    wrapper.send_data(first, "obj")


def fanout_message(msg_data, wrapper):
    chat_id = msg_data["chat_id"]
    msg_content = msg_data["msg_content"]

    ob = wrapper.ob
    ob.send_message(chat_id, msg_content)
    recipient_list = ob.get_recipient_list(chat_id)
    for i in recipient_list:
        try:
            is_online = active_client_sockets[i]
            if is_online:
                active_client_sockets[i][1] = False
        except:
            pass


def msg_ack(msg_data, wrapper):
    clear_msg_buffer(wrapper)
    user_id = wrapper.user_id
    active_client_sockets[user_id][1] = False


def verify_credentials(msg_data, wrapper):
    user_id = msg_data["user_id"]
    password = msg_data["password"]

    is_valid_user = False

    if Validator().validate_user(user_id, password):
        user_post = DatabaseConnector().get_user_post(user_id)
        is_valid_user = True
        dat = {"is_valid": True, "post": user_post, "user_id": user_id}
        wrapper.send_data({"msg_type": "authentication_status", "msg_data": dat}, "obj")
    else:
        dat = {"is_valid": False, "post": None, "user_id": user_id}
        wrapper.send_data({"msg_type": "authentication_status", "msg_data": dat}, "obj")

    if not (is_valid_user):
        return
    ob = UserStandard(user_id)
    wrapper.bind_socket(user_id, ob)

    in_progress = False
    active_client_sockets[user_id] = [wrapper, in_progress]


def register_new_client(client_handle):
    client_socket, address = client_handle.accept()
    client_socket.setblocking(False)
    respond_to = selectors.EVENT_READ
    wrapper = Packet(client_socket)

    event_handler.register(client_socket, events=respond_to, data=wrapper)

    verify_user(wrapper)

    print("active clients:\n", active_client_sockets)


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


def delegate_message(msg, wrapper):
    print(msg)
    MAPPING = {
        "credentials": verify_credentials,
        "msg": fanout_message,
        "msg_ack": msg_ack,
    }
    if type(msg) is dict:

        msg_type = msg["msg_type"]
        msg_data = msg["msg_data"]
        MAPPING[msg_type](msg_data, wrapper)


def handle_client_request(key, mask):
    client_socket = key.fileobj
    head = key.data

    if mask & selectors.EVENT_READ:
        try:
            msg = head.read_data()
            delegate_message(msg, head)
        except Exception as e:
            print(e)
            print("no data from client")
            print("client might have closed connection")
            del active_client_sockets[head.user_id]
            client_socket.close()
            event_handler.unregister(client_socket)
            print("closed socket")
            print(client_socket)


def check_for_updates():
    for i in active_client_sockets:
        head = active_client_sockets[i][0]
        in_progress = active_client_sockets[i][1]
        if not in_progress:
            try_sending_buffer_msg(head)
            active_client_sockets[i][1] = True


def start_server():
    try:
        while True:
            events = event_handler.select(timeout=1)
            check_for_updates()
            for key, mask in events:
                if key.data == None:
                    register_new_client(key.fileobj)
                else:
                    handle_client_request(key, mask)
    except Exception as e:
        print("server going down:", e)
    finally:
        event_handler.close()


if __name__ == "__main__":
    start_server()
    # verify_credentials({"user_id": "adam_12", "password": "adam"}, None)
    # verify_credentials({"user_id": "peter_13", "password": "peter"}, None)