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


group_one = {"alex": [], "jacob": [], "peter": []}


def identify_message(msg):
    if type(msg) is dict:
        print("dict it is")
        print(msg)
    # if "credentials" in msg:
    #     msg = msg[16:]
    #     user_id, password = msg.split(",")
    #     user_id = user_id.strip(" '\"\[\]\{\}")
    #     password = password.strip(" '\"\[\]\{\}")


def handle_client_request(key, mask):
    sock = key.fileobj
    head = key.data

    if mask & selectors.EVENT_READ:
        try:
            msg = head.read_data()
            identify_message(msg)
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