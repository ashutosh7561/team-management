import sqlite3
import pickle
import os

PATH_ONE = r"./production/model/clientdb.db"
PATH_TWO = r"C:/Users/Asus/Desktop/team-management/production/model/clientdb.db"


class ClientDatabaseConnector:
    def check_for_file(self):
        if os.path.isfile(PATH_ONE):
            return PATH_ONE
        elif os.path.isfile(PATH_TWO):
            return PATH_TWO
        else:
            raise FileNotFoundError

    def __init__(self, user_id):
        self.user_chat_table = user_id + "_chats"
        self.user_chat_details_table = user_id + "_chatdetails"

        try:
            database = self.check_for_file()
            self.rbac_connection = sqlite3.connect(database)
        except Exception as e:
            print(e)

        self.cursor = self.rbac_connection.cursor()
        # for setting foreign key constraints to true
        self.rbac_connection.execute("PRAGMA foreign_keys = 1")

        self.verify_table()

    def verify_table(self):
        user_table = self.table_exists()
        if user_table == []:
            self.add_user_table()

    def table_exists(self):
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name= (?);"
        try:
            self.cursor.execute(query, (self.user_chat_table,))
            rows = self.cursor.fetchall()
            arr = []
            for i in rows:
                arr.append(i[0])
            return arr
        except Exception as e:
            print(e)
            return []

    def add_user_table(self):
        query = f'CREATE TABLE IF NOT EXISTS "{self.user_chat_table}" (chat_id TEXT PRIMARY KEY, msg BOLB);'
        try:
            self.cursor.execute(query)
            self.rbac_connection.commit()
        except Exception as e:
            print(e)

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
        query = f'SELECT chat_id FROM "{self.user_chat_table}";'
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

        query = f'SELECT msg FROM "{self.user_chat_table}" WHERE chat_id = (?);'
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

    def details_table_exists(self):
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name= (?);"
        try:
            self.cursor.execute(query, (self.user_chat_details_table,))
            rows = self.cursor.fetchall()
            arr = []
            for i in rows:
                arr.append(i[0])
            return arr
        except Exception as e:
            print(e)
            return []

    def get_chat_details(self, chat_id):
        # query_two = f'CREATE TABLE IF NOT EXISTS "{self.user_chat_details_table}" ("chat_id" TEXT, "chat_desc" TEXT, "chat_icon" BLOB, PRIMARY KEY("chat_id"));'
        # query_three = f'INSERT INTO "{self.user_chat_details_table}" (chat_id, chat_desc, chat_icon) VALUES (?, ?, ?);'
        # if self.details_table_exists() == []:
        #     try:
        #         self.cursor.execute(
        #             query_three,
        #             (
        #                 "empty",
        #                 "empty",
        #                 "empty",
        #             ),
        #         )
        #         self.cursor.execute(query_two)
        #         self.rbac_connection.commit()
        #     except Exception as e:
        #         print(e)

        # self.rbac_connection.text_factory = bytes
        # query_one = f'SELECT chat_icon, chat_desc FROM "{self.user_chat_details_table}" WHERE chat_id = (?);'

        # arr = []
        # try:
        #     self.cursor.execute(
        #         query_one,
        #         (chat_id,),
        #     )
        #     rows = self.cursor.fetchall()
        #     for i in rows:
        #         arr.append(i)
        #     self.rbac_connection.text_factory = str
        #     return arr[0]

        # except Exception as e:
        #     self.rbac_connection.text_factory = str
        #     print(e)
        #     return arr
        return ["id", "desc", b"icon"]

    def update_chat_icon(self, chat_id, chat_icon):
        query = f'UPDATE "{self.user_chat_details_table}" SET chat_icon = (?) WHERE chat_id = (?);'

        chat_list = self.get_chat_list()
        if chat_id not in chat_list:
            raise Exception("chat_id not found")
        try:
            cursor = self.cursor.execute(query, (chat_id, chat_icon))
            self.rbac_connection.commit()
        except Exception as e:
            print(e)

    def update_chat_desc(self, chat_id, chat_desc):
        query = f'UPDATE "{self.user_chat_details_table}" SET chat_desc = (?) WHERE chat_id = (?);'

        chat_list = self.get_chat_list()
        if chat_id not in chat_list:
            raise Exception("chat_id not found")
        try:
            cursor = self.cursor.execute(query, (chat_id, chat_desc))
            self.rbac_connection.commit()
        except Exception as e:
            print(e)

    def stash_incoming_message(self, chat_id, data):
        query = f'INSERT INTO "{self.user_chat_table}"(chat_id, msg) VALUES (?, ?);'
        query_two = (
            f'UPDATE "{self.user_chat_table}" SET msg = (?) WHERE chat_id = (?);'
        )

        chat_list = self.get_chat_list()
        if chat_id not in chat_list:
            try:
                data = [data]
                data = pickle.dumps(data)
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
                # self.cursor.execute(query_two, (chat_id, new_binary_data))
                self.rbac_connection.commit()
            except Exception as e:
                print(e)

    def clear_chat_messages(self, chat_id):
        query_two = (
            f'UPDATE "{self.user_chat_table}" SET msg = (?) WHERE chat_id = (?);'
        )

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
    def __init__(self, user_id, queue):
        self.clientdb = ClientDatabaseConnector(user_id)
        self.user_id = user_id
        self.queue = queue

    def get_chat_messages(self, chat_id):
        dat = self.clientdb.get_chat_messages(chat_id)
        chat_messages = pickle.loads(dat)

        for message in chat_messages:
            for i in message.keys():
                message_sender = i
                msg = message[i]
            if self.user_id in message:
                # print("render send message")
                # message = message[self.user_id]
                self.queue.put({"send_msg": True, "chat_id": chat_id, "message": msg})
                # self.queue.put({"send_msg": message})
            else:
                # print("render recv message")
                self.queue.put({"recv_msg": True, "chat_id": chat_id, "message": msg})
                # self.queue.put({"recv_msg": message})

    def write_chat_message(self, chat_id, msg):
        self.clientdb.stash_incoming_message(chat_id, msg)
        # if self.user_id in msg:
        #     # print("render send message")
        #     self.queue.put({"send_msg": msg})
        # else:
        #     # print("render recv message")
        #     self.queue.put({"recv_msg": msg})

    def get_all_chat_messages(self):
        for i in self.clientdb.get_chat_list():
            self.get_chat_messages(i)

    def get_chat_details(self, chat_id):
        details = self.clientdb.get_chat_details(chat_id)
        chat_icon = details[1]
        # chat_desc = details[1].decode("utf-8")
        chat_desc = details[0]

        return {"chat_id": chat_id, "chat_icon": chat_icon, "chat_desc": chat_desc}

    def get_all_chats_list(self):
        chats_list = self.clientdb.get_chat_list()
        dat = {}
        dat["chats_list"] = True
        dat["list"] = chats_list
        self.queue.put(dat)

    def get_all_chats_details(self):
        chats_list = self.clientdb.get_chat_list()
        chats_list_detail = []
        for chat in chats_list:
            chats_list_detail.append(self.get_chat_details(chat))
        dat = {}
        dat["chats_list_detail"] = True
        dat["list_two"] = chats_list_detail
        dat["list"] = chats_list
        self.queue.put(dat)


from queue import Queue

if __name__ == "__main__":
    qu = Queue()
    o = ClientDBHandler("adam_12", qu)
    o.get_chat_messages("group_one")
    # o.get_chat_messages("group_two")
    # print(o.get_chat_details("group_one"))
    # o.write_chat_message("group_one", {"alex_11": "actual message"})

    # print(qu.get())
    # print(qu.get())

    # k = ClientDatabaseConnector("alex_11")
    # k.clear_chat_messages("group_one")

    # print(k.get_chat_details("group_one"))
    # k.clear_chat_messages("group_two")
    # mm = pickle.dumps({"adam_12": "message from adam_12"})

    # k.stash_incoming_message("group_one", mm)

    # msg = {"alex_10": "msg from alex"}

    # k.stash_incoming_message("group_one", msg)

    # print(pickle.loads(k.get_chat_messages("group_one")))

    # chat_messages = k.get_chat_list()

    # for i in chat_messages:
    #     print(i)

    # c = UserStandard("dan_20")
    # c.send_message("group_two", "msg from dan_20")
    pass
