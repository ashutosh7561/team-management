import sys
import socket
import selectors
import json
import io
import struct
from math import ceil


class RecieveMessage:
    def __init__(self, sock):
        self.sock = sock
        self.msg_enc = bytes()
        self.data_packets = []
        self.process_header()

    def process_header(self):
        header_len_in_bytes = self.sock.recv(2)
        header_len = struct.unpack(">H", header_len_in_bytes)[0]
        header = self.sock.recv(header_len)
        header = self.decode_json_header(header)
        self.read_data(header)

    def read_data(self, header):
        msg_len = header["msg_len"]
        msg_type = header["content_type"]
        msg_encoding = header["content_encoding"]
        msg_data_hash = header["data_hash"]
        has_more = header["has_more"]
        index = header["index"]

        if msg_type == "txt":
            data = self.sock.recv(msg_len)
            self.data_packets.append(data)
            # used recurssion here which can affect performance
            if has_more:
                self.process_header()
            else:
                for i in self.data_packets:
                    self.msg_enc += i
        # self.msg_enc = self.sock.recv(msg_len)

    def decode_json_header(self, header_in_bytes):
        encoding = "utf-8"
        tiow = io.TextIOWrapper(
            io.BytesIO(header_in_bytes), encoding=encoding, newline=""
        )
        json_header = json.load(tiow)
        tiow.close()
        return json_header

    def get_message(self):
        return self.msg_enc.decode("utf-8")


class SendMessage:
    def __init__(self, sock, packet_list):
        self.sock = sock
        self.packet_list = packet_list
        for i in self.packet_list:
            self.send_packet(i)

    def send_packet(self, packet):
        self.sock.sendall(packet)


class Message:
    def __init__(self, msg_data, msg_type):
        self.header = {
            "msg_len": 0,
            "content_type": None,
            "content_encoding": None,
            "data_hash": None,
            "has_more": None,
            "index": None,
        }
        self.packet_threshold = 128
        self.header_threshold = 30
        self.data_threshold = self.packet_threshold - self.header_threshold
        self.packet_list = []
        if msg_type == "txt":
            self.msg_data = bytes(msg_data, "utf-8")

        self.create_packets()

        # self.encode_msg_data()
        # self.add_header()

    def encode_data(self, data):
        return data.encode("utf-8")

    def split(self):
        no_of_packets = ceil(len(self.msg_data) / self.data_threshold)
        print(no_of_packets)
        for i in range(no_of_packets - 1):
            lower = i * self.data_threshold
            upper = (i + 1) * self.data_threshold
            self.add_header(self.msg_data[lower:upper], "txt", "utf-8", True, i)
        # last packet
        i += 1
        lower = i * self.data_threshold
        upper = (i + 1) * self.data_threshold
        self.add_header(self.msg_data[lower:upper], "txt", "utf-8", False, i)

    def create_packets(self):
        if len(self.msg_data) >= self.packet_threshold + self.header_threshold:
            self.split()
        else:
            self.add_header(self.msg_data, "txt", "utf-8", False, 0)

    def add_header(self, data, data_type, data_encoding, has_more, index):
        header = {
            "msg_len": 0,
            "content_type": None,
            "content_encoding": None,
            "data_hash": None,
            "has_more": None,
            "index": None,
        }
        header["msg_len"] = len(data)
        header["content_type"] = data_type
        header["content_encoding"] = data_encoding
        header["has_more"] = has_more
        header["index"] = index

        json_header_in_bytes = json.dumps(header).encode("utf-8")
        # 2 byte(int) header indicating length of header
        header_len_in_bytes = struct.pack(">H", len(json_header_in_bytes))

        packet = header_len_in_bytes + json_header_in_bytes + data
        self.packet_list.append(packet)


if __name__ == "__main__":
    ms = "qwertyuiopasdfghjklmnbvcxz" * 40
    msg = Message(ms, "txt")
    # for i in msg.packet_list:
    # print(i)

    sm = SendMessage(None, msg.packet_list)