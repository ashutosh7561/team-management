import socket
import selectors
import types

try:
    from header import Packet
except:
    try:
        from controller.chats.sockets.header import Packet
    except Exception as e:
        print(e)

try:
    from chatdbconnector import *
except:
    try:
        from controller.chats.sockets.chatdbconnector import *
    except Exception as e:
        print(e)


HOST = "127.0.0.1"
PORT = 65432

event_handler = selectors.DefaultSelector()

main_listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_listening_socket.bind((HOST, PORT))
main_listening_socket.setblocking(False)
main_listening_socket.listen(5)
event_handler.register(main_listening_socket, selectors.EVENT_READ, data=None)

active_client_sockets = {}


def create_secure_connection(client_socket):
    print("do tls handshake")


def register_new_client(client_handle):
    client_socket, address = client_handle.accept()
    client_socket.setblocking(False)
    respond_to = selectors.EVENT_READ
    data = Packet(client_socket)

    event_handler.register(client_socket, events=respond_to, data=data)

    create_secure_connection(client_socket)

    first = {"identify_user": ["user_id", "password"]}
    data.send_data(first, "obj")


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
            active_client_sockets[user_id] = [head, in_progress]

        elif "msg" in msg:
            chat_id = msg["chat_id"]
            msg_data = msg["msg_data"]

            ob = head.ob
            ob.send_message(chat_id, msg_data)
            recipient_list = ob.get_recipient_list(chat_id)
            for i in recipient_list:
                try:
                    is_online = active_client_sockets[i]
                    if is_online:
                        active_client_sockets[i][1] = False
                except:
                    pass

        elif "msg_recieved" in msg:
            clear_msg_buffer(head)
            user_id = head.user_id
            active_client_sockets[user_id][1] = False


def handle_client_request(key, mask):
    client_socket = key.fileobj
    head = key.data

    if mask & selectors.EVENT_READ:
        try:
            msg = head.read_data()
            identify_message(msg, head)
        except Exception as e:
            print(e)
            print("no data from client")
            print("client might have closed connection")
            del active_client_sockets[head.user_id]
            client_socket.close()
            event_handler.unregister(client_socket)
            print("closed socket")


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