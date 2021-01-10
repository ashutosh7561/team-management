import socket
import selectors
import types
from header import Packet

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


group_one = {"alex": [], "jacob": [], "peter": []}
group_one_database = {"alex": [], "jacob": [], "peter": []}

client_sockets = {}


def identify_message(msg, head):
    if type(msg) is dict:
        print("special message from client")
        if "credentials" in msg:
            credentials = msg["credentials"]
            user_id = credentials[0]
            password = credentials[1]

            head.bind_socket(user_id)

            # sel.modify(head.sock, selectors.EVENT_READ, data=head)

            if user_id in group_one.keys():
                client_sockets[user_id] = head

    elif type(msg) is str:
        user_id = head.user_id
        if user_id in group_one.keys():
            group_one_database[user_id].append(msg)
        for i in group_one:
            if i != user_id:
                group_one[i].append(msg)
        for i in group_one:
            while len(group_one[i]) > 0:
                ms = group_one[i].pop(0)
                client_sockets[i].send_data(ms, "txt")
        print("recepients:", group_one)
        print("group database:", group_one_database)

        # for i in client_sockets.keys():
        #     if i != head.user_id:
        #         client_sockets[i].send_data(msg, "txt")


def handle_client_request(key, mask):
    sock = key.fileobj
    head = key.data

    if mask & selectors.EVENT_READ:
        try:
            msg = head.read_data()
            identify_message(msg, head)
            print("[Message from client]:", msg)
        except Exception as e:
            print(e)
            print("no data from client")
            print("client might have closed connection")
            sock.close()
            sel.unregister(sock)
            print("closed socket")


try:
    while True:
        events = sel.select(timeout=None)
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