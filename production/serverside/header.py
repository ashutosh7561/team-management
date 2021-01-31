import sys
import socket
import selectors
import json
import io
import struct
import pickle
from math import ceil


class Packet:
    def __init__(self, sock):
        self.sock = sock
        header = {
            "msg_len": 0,
            "content_type": None,
            "content_encoding": None,
            "data_hash": None,
            "has_more": None,
            "index": None,
            "close": None,
        }
        self.packet_threshold = 128
        self.header_threshold = 30
        self.data_threshold = self.packet_threshold - self.header_threshold
        self.encoding = "utf-8"

    def bind_socket(self, user_id, ob, ticket_db):
        self.user_id = user_id
        self.ob = ob
        self.ticket_db = ticket_db

    def send_data(self, data, data_type):
        packet_list = self.make_packets(data, data_type)
        for i in packet_list:
            self.sock.sendall(i)

    def make_packets(self, data, data_type):
        packet_list = []
        if data_type == "txt":
            data = bytes(data, self.encoding)

        if data_type == "obj":
            data = pickle.dumps(data)
            pass

        if self.is_sufficient_len(data):
            packet_list.append(
                self.add_header(data, data_type, self.encoding, False, 0)
            )
        else:
            packet_list = self.split_packets(data, data_type)
        # other data_type conditions like image or blob

        return packet_list

    def split_packets(self, data, data_type):
        packet_list = []
        no_of_packets = ceil(len(data) / self.data_threshold) - 1
        for i in range(no_of_packets):
            lower = i * self.data_threshold
            upper = (i + 1) * self.data_threshold
            packet_list.append(
                self.add_header(data[lower:upper], data_type, self.encoding, True, i)
            )

        # last packet
        i += 1
        lower = i * self.data_threshold
        packet_list.append(
            self.add_header(data[lower::], data_type, self.encoding, False, i)
        )

        return packet_list

    def is_sufficient_len(self, data):
        if len(data) >= self.packet_threshold + self.header_threshold:
            return False
        return True

    def add_header(self, data, data_type, data_encoding, has_more, index):
        header = {
            "msg_len": 0,
            "content_type": None,
            "content_encoding": None,
            "data_hash": None,
            "has_more": None,
            "index": None,
            "close": False,
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
        return packet

    def decode_header(self, sock):
        header_len_in_bytes = sock.recv(2)
        header_len = struct.unpack(">H", header_len_in_bytes)[0]
        header = sock.recv(header_len)
        header = self.decode_json_header(header)
        return header

    def decode_json_header(self, header_in_bytes):
        encoding = self.encoding
        tiow = io.TextIOWrapper(
            io.BytesIO(header_in_bytes), encoding=encoding, newline=""
        )
        json_header = json.load(tiow)
        tiow.close()
        return json_header

    def read_data(self):
        sock = self.sock
        data_packets = []
        final_data = bytes()

        has_more = True
        while has_more:
            header = self.decode_header(sock)
            msg_len, msg_type, has_more, close = self.read_header(header)
            if not close:
                data_packets.append(self.read_packet_data(sock, msg_len))

        for i in data_packets:
            final_data += i

        if msg_type == "txt":
            return final_data.decode(self.encoding)
        elif msg_type == "obj":
            return pickle.loads(final_data)

    def read_header(self, header):
        msg_len = header["msg_len"]
        msg_type = header["content_type"]
        msg_encoding = header["content_encoding"]
        msg_data_hash = header["data_hash"]
        has_more = header["has_more"]
        index = header["index"]
        close = header["close"]

        if msg_type == "txt":
            return msg_len, msg_type, has_more, close
        if msg_type == "obj":
            return msg_len, msg_type, has_more, close

    def read_packet_data(self, sock, msg_len):
        return sock.recv(msg_len)


if __name__ == "__main__":
    ms = "qwertyuiopasdfghjklmnbvcxz" * 40