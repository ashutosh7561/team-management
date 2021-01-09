import socket
import time
from header import Message, SendMessage

HOST = "127.0.0.1"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

flag = True
while flag:
    user_msg = input()
    if user_msg == "":
        flag = False
        break
    elif user_msg == "quit":
        ms = "quit"
    elif user_msg == "request data":
        ms = "request data"
    else:
        ms = "qwertyuiopasdfghjklmnbvcxz" * 40

    msg = Message(ms, "txt")
    sm = SendMessage(sock, msg.packet_list)
    # sock.sendall(msg.msg)
    if user_msg == "quit":
        sock.close()
        break
    if user_msg == "request data":
        recieved_msg = sock.recv(1024)
        print(recieved_msg.decode("utf-8"))
print("i have done my work")