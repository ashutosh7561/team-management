import sqlite3
import pickle
import os

PATH_ONE = r"./chats.db"
PATH_TWO = r"./production/serverside/servermodel/chats.db"


class ChatDatabaseConnector:
    def check_for_file(self):
        if os.path.isfile(PATH_ONE):
            return PATH_ONE
        elif os.path.isfile(PATH_TWO):
            return PATH_TWO
        else:
            raise FileNotFoundError

    def __init__(self):
        try:
            database = self.check_for_file()
            self.rbac_connection = sqlite3.connect(database)
        except Exception as e:
            print(e)

        self.cursor = self.rbac_connection.cursor()
        # for setting foreign key constraints to true
        self.rbac_connection.execute("PRAGMA foreign_keys = 1")

    def add_members_to_group(self, chat_id, user_id):
        dummy = pickle.dumps([])
        query = "INSERT INTO user_chats(chat_id, user_id, sent_msg, recieve_msg) VALUES (?, ?, ?, ?);"
        try:
            self.cursor.execute(
                query,
                (
                    chat_id,
                    user_id,
                    dummy,
                    dummy,
                ),
            )
            self.rbac_connection.commit()
        except Exception as e:
            print(e)

    def create_group(self, chat_id, chat_admin_user_id):
        self.add_members_to_group(chat_id, chat_admin_user_id)

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

    def get_associated_groups(self, user_id):
        query = "SELECT chat_id FROM chat_data WHERE user_id = (?);"
        try:
            self.cursor.execute(
                query,
                (user_id,),
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

    def clear_buffer(self, user_id, chat_id):
        data = pickle.dumps([])
        query = "UPDATE chat_data SET recieve_msg = (?) WHERE user_id = (?) AND chat_id = (?);"
        try:
            cursor = self.cursor.execute(
                query,
                (
                    data,
                    user_id,
                    chat_id,
                ),
            )
            self.rbac_connection.commit()
        except Exception as e:
            print(e)


# must set autocommit of sqlite to false to avoid errors and full access control


class UserStandard:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db_connector = ChatDatabaseConnector()

    def get_recipient_list(self, chat_id):
        # extra guard try-except can be removed
        try:
            recipient_list = set(self.db_connector.get_group_members(chat_id))
            if self.user_id in recipient_list:
                recipient_list.remove(self.user_id)
                return recipient_list
            return set()
        except Exception as e:
            print(e)
            return set()

    def get_user_buffer(self, user_id, chat_id):
        try:
            bf = self.db_connector.get_user_buffer(user_id, chat_id)
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
        self.db_connector.write_to_buffer(chat_id, recipient_id, bf)

    def send_message(self, chat_id, msg):
        recipient_list = self.get_recipient_list(chat_id)
        for recipient in recipient_list:
            self.write_to_buffer(recipient, chat_id, msg)

    def get_messages(self):
        group_list = self.db_connector.get_associated_groups(self.user_id)
        msg_list = {}
        for i in group_list:
            msg_list[i] = self.get_user_buffer(self.user_id, i)
        return msg_list

    def clear_buffer(self, user_id, chat_id):
        self.db_connector.clear_buffer(user_id, chat_id)

    def create_group(self, chat_id, chat_admin_user_id):
        self.db_connector.create_group(chat_id, chat_admin_user_id)

    def add_members_to_group(self, chat_id, user_id):
        self.db_connector.add_members_to_group(chat_id, user_id)


if __name__ == "__main__":
    o = UserStandard("peter_13")
    print(o.get_messages())
    # o.clear_buffer("peter_13", "group_two")

    # c = UserStandard("dan_20")
    # c.send_message("group_two", {"sender_id": "dan_20", "message": "raw_data"})

    o = UserStandard("dan_20")
    print(o.get_messages())
    # o.clear_buffer("dan_20", "group_two")

    o = UserStandard("zed_15")
    print(o.get_messages())
    # o.clear_buffer("zed_15", "group_two")

    o = UserStandard("adam_12")
    print(o.get_messages())
    # o.clear_buffer("adam_12", "group_two")

    o = UserStandard("alex_11")
    print(o.get_messages())
    # o.clear_buffer("alex_11", "group_one")

    # o = UserStandard("adam_12")
    # o.send_message("group_one", {"sender_id": "adam_12", "message": "message from adam"})
    pass