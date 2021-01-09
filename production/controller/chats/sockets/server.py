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

sock_list = []


def client_request(sock):
    con, addr = sock.accept()
    sock_list.append(con)
    print("available connection:", sock_list)
    con.setblocking(False)
    events = selectors.EVENT_READ
    data = Packet(con)
    sel.register(con, events, data)


def handle_client(key, mask):
    sock = key.fileobj
    head = key.data

    if mask & selectors.EVENT_READ:
        try:
            msg = head.read_data()
            if msg == "request data":
                print("ok-----------\n")
                sock.sendall(bytes("here have your message", "utf-8"))
            if msg == "quit":
                print("closing connection")
                sel.unregister(sock)
                sock.close()
            if msg == "send":
                print("admin access ********")
                sock_list[0].sendall(bytes("admin notification", "utf-8"))
            else:
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
                client_request(key.fileobj)
            else:
                handle_client(key, mask)
except Exception as e:
    print("server going down:", e)
finally:
    sel.close()