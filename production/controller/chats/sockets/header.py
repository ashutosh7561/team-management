import sys
import selectors
import json
import struct


class Message:
    def __init__(self, message):
        self.message = None
        self.message_data = message

    def add_header(self):
        self.header = {
            "message_len": 0,
            "content_type": None,
            "content-encoding": None,
            "has_more": None,
        }
        self.json_header_bytes = json.dumps(self.header).encode("utf-8")
        self.header_len_bytes = struct.pack(">H", len(self.json_header_bytes))

        self.message = self.header_len_bytes + self.json_header_bytes

        print(self.message)

    def process_header(self):
        pass


msg = Message("a text")
msg.add_header()