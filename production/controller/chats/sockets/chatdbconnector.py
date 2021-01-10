import sqlite3


class ChatDatabaseConnector:
    def __init__(
        self,
        database=r"./chats.db",
    ):
        self.rbac_connection = sqlite3.connect(database)
        self.cursor = self.rbac_connection.cursor()
        # for setting foreign key constraints to true
        self.rbac_connection.execute("PRAGMA foreign_keys = 1")

    def create_group(self, group_id):
        pass

    def add_members_to_group(self, user_id, group_id):
        pass

    def get_group_members(self, chat_id):
        query = "SELECT user_chats.user_id FROM user_chats WHERE chat_id=(?);"
        try:
            self.cursor.execute(query, (chat_id,))
            rows = self.cursor.fetchall()
            arr = []
            for i in rows:
                arr.append(i[0])
            return arr
        except Exception as e:
            print(e)
            return []

    def get_user_buffer(self, user_id, chat_id):
        # sqlite tries to decode binary data into string and gives exception
        # so read it in binary for this query only
        self.rbac_connection.text_factory = bytes
        query = (
            "SELECT recieve_msg FROM chat_data WHERE user_id = (?) AND chat_id = (?);"
        )
        try:
            self.cursor.execute(
                query,
                (
                    user_id,
                    chat_id,
                ),
            )
            rows = self.cursor.fetchall()
            arr = []
            for i in rows:
                arr.append(i[0])
            return arr
        except Exception as e:
            print(e)
            return []
        finally:
            self.rbac_connection.text_factory = str

    def write_to_buffer(self, chat_id, recipient_id, data):
        query = "UPDATE chat_data SET recieve_msg = (?) WHERE user_id = (?) AND chat_id = (?);"
        try:
            cursor = self.cursor.execute(
                query,
                (
                    data,
                    recipient_id,
                    chat_id,
                ),
            )
            self.rbac_connection.commit()
        except Exception as e:
            print(e)


# must set autocommit of sqlite to false to avoid errors and full access control

import pickle


class UserStandard:
    def __init__(self, user_id):
        self.user_id = user_id
        self.ch = ChatDatabaseConnector()

    def get_recipient_list(self, chat_id):
        # extra guard try-except can be removed
        try:
            recipient_list = set(self.ch.get_group_members(chat_id))
            if self.user_id in recipient_list:
                recipient_list.remove(self.user_id)
                return recipient_list
            return set()
        except Exception as e:
            print(e)
            return set()

    def get_user_buffer(self, user_id, chat_id):
        try:
            bf = self.ch.get_user_buffer(user_id, chat_id)
            bf = bf[0]
            bf = pickle.loads(bf)
            return bf
        except Exception as e:
            # no recieve_msg buffer associated with user_id, chat_id
            print(e)

    def write_to_buffer(self, recipient_id, chat_id, msg):
        bf = self.get_user_buffer(recipient_id, chat_id)
        bf.append(msg)
        bf = pickle.dumps(bf)
        self.ch.write_to_buffer(chat_id, recipient_id, bf)

    def send_message(self, chat_id, msg):
        recipient_list = self.get_recipient_list(chat_id)
        for recipient in recipient_list:
            self.write_to_buffer(recipient, chat_id, msg)


if __name__ == "__main__":
    pass