import sqlite3
import pickle
import os
import random

PATH_ONE = r"./production/serverside/servermodel/tickets.db"
PATH_TWO = r"C:/Users/Asus/Desktop/team-management/production/serverside/tickets.db"


class TicketDatabaseConnector:
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

    def get_ticket_id(self, user_id):
        query = f"SELECT COUNT(ticket_id) FROM ticket_list;"
        try:
            self.cursor.execute(
                query,
            )
            rows = self.cursor.fetchall()
            arr = []
            for i in rows:
                arr.append(i[0])
            count = arr[0] + 1
            ticket_id = str(user_id) + str(random.randint(10000, 1000000)) + str(count)
            return ticket_id
        except Exception as e:
            print(e)
            raise Exception("cannot create id")

    def add_ticket(
        self,
        user_id,
        ticket_id,
        ticket_creator_id,
        ticket_heading,
        ticket_content,
        is_active=1,
    ):
        query = f"INSERT INTO ticket_list(user_id, ticket_id, ticket_creator, ticket_heading, ticket_content, is_active) VALUES (?, ?, ?, ?, ?, ?);"
        try:
            cursor = self.cursor.execute(
                query,
                (
                    user_id,
                    ticket_id,
                    ticket_creator_id,
                    ticket_heading,
                    ticket_content,
                    is_active,
                ),
            )
            self.rbac_connection.commit()
            return ticket_id
        except Exception as e:
            print(e)

    def list_all_tickets(self, user_id):
        query = f"SELECT * FROM ticket_list WHERE user_id = (?);"
        try:
            self.cursor.execute(
                query,
                (user_id,),
            )
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
            return []

    def list_active_tickets(self, user_id):
        query = f"SELECT * FROM ticket_list WHERE user_id = (?) AND is_active = 1;"
        try:
            self.cursor.execute(
                query,
                (user_id,),
            )
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
            return []

    def pick_ticket(self, ticket_id):
        query = f"UPDATE ticket_list SET is_active = 0 WHERE ticket_id = (?);"
        try:
            cursor = self.cursor.execute(
                query,
                (ticket_id,),
            )
            self.rbac_connection.commit()
        except Exception as e:
            print(e)


# must set autocommit of sqlite to false to avoid errors and full access control


class TicketDBHandler:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db_connector = TicketDatabaseConnector()

    def create_ticket(self, recepient_list, ticket_heading, ticket_content):
        ticket_id = self.db_connector.get_ticket_id(self.user_id)
        for i in recepient_list:
            self.db_connector.add_ticket(
                i, ticket_id, self.user_id, ticket_heading, ticket_content, is_active=1
            )
        return ticket_id

    def get_tickets(self, active=False):
        if active:
            return self.db_connector.list_active_tickets(self.user_id)
        return self.db_connector.list_all_tickets(self.user_id)

    def pick_ticket(self, ticket_id):
        self.db_connector.pick_ticket(ticket_id)


if __name__ == "__main__":
    tc = TicketDBHandler("alex_11")
    print(tc.get_tickets(True))

    # tc.create_ticket(["adam_12", "dan_20"], "none", "none")

    # print(tc.get_tickets(False))
    # o = TicketDatabaseConnector()
    # print(o.get_ticket_id("adam_12"))
    # print(o.add_ticket("alex_11", "adam_12", "nothing", "empty", 1))

    # print(o.list_active_tickets("alex_11"))

    # tc.pick_ticket(6)
    # tc.create_ticket(
    #     ["alex_11", "dan_20", "zed_15"],
    #     "ticket for a group",
    #     "content which will include something",
    # )
    # tc.get_tickets()