import socket
import selectors
import types
from header import Message, RecieveMessage

HOST = "127.0.0.1"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
sock.setblocking(False)

sel = selectors.DefaultSelector()
sel.register(sock, selectors.EVENT_READ, data=None)


def client_request(sock):
    con, addr = sock.accept()
    con.setblocking(False)
    events = selectors.EVENT_READ
    data = types.SimpleNamespace(addr=addr, inb=b"", outb="")
    sel.register(con, events, data)


def handle_client(key, mask):
    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        pt = RecieveMessage(sock)
        # msg = sock.recv(1024).decode("utf-8")
        msg = pt.get_message()
        if msg == "request data":
            print("ok-----------\n")
            sock.sendall(bytes("here have your message", "utf-8"))
        if msg == "quit":
            print("closing connection")
            sel.unregister(sock)
            sock.close()
        else:
            print("[Message from client]:", msg)


try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data == None:
                # new client request
                client_request(key.fileobj)
            else:
                handle_client(key, mask)
except Exception as e:
    print("server going down:", e)
finally:
    sel.close()