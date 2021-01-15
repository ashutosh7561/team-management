import sqlite3
import pickle


class ClientDatabaseConnector:
    def __init__(
        self,
        database=r"./clientdb.db",
    ):
        self.rbac_connection = sqlite3.connect(database)
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

    def get_chat_list(self):
        query = "SELECT chat_id FROM chat_cache;"
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            arr = []
            for i in rows:
                arr.append(i[0])
            return arr
        except Exception as e:
            print(e)
            return []

    def get_chat_messages(self, chat_id):
        # sqlite tries to decode binary data into string and gives exception
        # so read it in binary for this query only
        self.rbac_connection.text_factory = bytes

        query = "SELECT msg FROM chat_cache WHERE chat_id = (?);"
        arr = []
        try:
            self.cursor.execute(
                query,
                (chat_id,),
            )
            rows = self.cursor.fetchall()
            for i in rows:
                arr.append(i[0])
            self.rbac_connection.text_factory = str
            return arr[0]

        except Exception as e:
            self.rbac_connection.text_factory = str
            print(e)
            return arr

    def stash_incoming_message(self, chat_id, data):
        query = "INSERT INTO chat_cache(chat_id, msg) VALUES (?, ?);"
        query_two = "UPDATE chat_cache SET msg = (?) WHERE chat_id = (?);"

        chat_list = self.get_chat_list()
        if chat_id not in chat_list:
            try:
                cursor = self.cursor.execute(query, (chat_id, data))
                self.rbac_connection.commit()
            except Exception as e:
                print(e)
        else:
            try:
                old_binary_data = self.get_chat_messages(chat_id)
                old_data = pickle.loads(old_binary_data)
                old_data.append(data)
                new_binary_data = pickle.dumps(old_data)
                self.cursor.execute(query_two, (new_binary_data, chat_id))
                self.rbac_connection.commit()
            except Exception as e:
                print(e)

    def clear_chat_messages(self, chat_id):
        query_two = "UPDATE chat_cache SET msg = (?) WHERE chat_id = (?);"

        chat_list = self.get_chat_list()
        if chat_id not in chat_list:
            print("chat_id", chat_id, "not yet created")
        else:
            try:
                new_binary_data = pickle.dumps([])
                self.cursor.execute(query_two, (new_binary_data, chat_id))
                self.rbac_connection.commit()
            except Exception as e:
                print(e)


# must set autocommit of sqlite to false to avoid errors and full access control


class ClientDBHandler:
    def __init__(self, user_id):
        self.clientdb = ClientDatabaseConnector()
        self.user_id = user_id

    def get_chat_messages(self, chat_id):
        chat_messages = pickle.loads(self.clientdb.get_chat_messages(chat_id))

        for message in chat_messages:
            print(message)
            if self.user_id in message:
                print("render send message")
            else:
                print("render recv message")

    def write_chat_message(self, chat_id, msg):
        self.clientdb.stash_incoming_message(chat_id, msg)


if __name__ == "__main__":
    o = ClientDBHandler("adam_12")
    print(o.get_chat_messages("group_one"))
    print(o.get_chat_messages("group_two"))

    # k = ClientDatabaseConnector()

    # k.clear_chat_messages("group_one")
    # k.clear_chat_messages("group_two")

    # msg = {"alex_10": "msg from alex"}

    # k.stash_incoming_message("group_one", msg)

    # print(pickle.loads(k.get_chat_messages("group_one")))

    # chat_messages = k.get_chat_list()

    # for i in chat_messages:
    #     print(i)

    # c = UserStandard("dan_20")
    # c.send_message("group_two", "msg from dan_20")
    pass
