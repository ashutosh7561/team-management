import socket
import time
from header import Packet

HOST = "127.0.0.1"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))


def reconnect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    u = input("reconnected")


flag = True
while flag:
    user_msg = input()
    ms = "qwertyuiopasdfghjklmnbvcxz" * 40

    if user_msg == "":
        flag = False
        sock.close()
        time.sleep(5)
        reconnect()
        break
    elif user_msg == "quit":
        ms = "quit"
    elif user_msg == "request data":
        ms = "request data"
    elif user_msg == "admin":
        ms = input()

    p = Packet(sock)
    p.send_data(ms, "txt")

    if user_msg == "quit":
        sock.close()
        break
    if user_msg == "request data":
        recieved_msg = sock.recv(1024)
        print(recieved_msg.decode("utf-8"))
print("i have done my work")