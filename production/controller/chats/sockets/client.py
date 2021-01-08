import socket
import time

HOST = "127.0.0.1"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

flag = True
while flag:
    msg = input()
    if msg == "":
        flag = False
        break
    sock.send(bytes(msg, "utf-8"))
    if msg == "request data":
        recieved_msg = sock.recv(1024)
        print(recieved_msg.decode("utf-8"))
    if msg == "quit":
        sock.close()
        break
print("i have done my work")