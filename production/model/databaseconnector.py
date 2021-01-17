import sqlite3
import os

with open(str(os.getpid()) + ".txt", "a+") as f:
    f.write("imported databaseconnector.py successfully\n")


def check_for_file(PATH_ONE, PATH_TWO):
    if os.path.isfile(PATH_ONE):
        return PATH_ONE
    elif os.path.isfile(PATH_TWO):
        return PATH_TWO
    else:
        raise FileNotFoundError


class DatabaseConnector:
    def __init__(self):
        PATH_ONE = r"./production/model/rbac.db"
        PATH_TWO = r"C:/Users/Asus/Desktop/team-management/production/model/rbac.db"
        try:
            file = check_for_file(PATH_ONE, PATH_TWO)
            # print(file)
            self.rbac_connection = sqlite3.connect(file)
        except Exception as e:
            print(e)
        # for setting
        # self.rbac_connection = sqlite3.connect(database)
        # for setting foreign key constraints to true
        self.rbac_connection.execute("PRAGMA foreign_keys = 1")

    def get_user_password(self, user_id):
        query = f"SELECT user_data.password_hash from user_data where user_data.user_id='{user_id}';"
        try:
            cursor = self.rbac_connection.execute(query)
            for i in cursor:
                return i[0]
        except:
            return ""

    def set_user_password(self, user_id, new_password_hash):
        query = f"UPDATE user_data SET password_hash = '{new_password_hash}' WHERE user_id = '{user_id}';"
        cursor = self.rbac_connection.execute(query)
        self.rbac_connection.commit()

    def get_user_rights(self, user_id):
        query = f"""SELECT permission.perm_desc FROM user, role_permission, permission, role WHERE
                    user.role_id = role_permission.role_id AND 
                    role_permission.permission_id = permission.permission_id AND 
                    user.role_id = role.role_id AND user.user_id='{user_id}';"""
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr

    def get_available_access_rights(self):
        query = f"SELECT perm_desc FROM permission;"
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr

    def get_access_rights_for_post(self, post_name):
        query = f"""SELECT permission.perm_desc from role, role_permission, permission WHERE
                    role.role_id = role_permission.role_id AND
                    role_permission.permission_id = permission.permission_id AND
                    role.desc like '%{post_name}%';"""
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr

    def get_access_rights_by_post_id(self, post_id):
        query = f"""SELECT role_permission.permission_id from role_permission WHERE
                    role_permission.role_id = '{post_id}';"""
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr

    def get_user_post(self, user_id):
        query = f"SELECT role.desc FROM role, user WHERE user.role_id = role.role_id AND user.user_id = '{user_id}';"
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr[0]

    def get_users_data(self):
        query = f"""SELECT user.name, user.user_id, role.role_id FROM user, role WHERE 
                    user.role_id = role.role_id ORDER BY user.user_id;"""
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i)
        return arr

    def generate_user_id(self, username):
        query = "SELECT COUNT(user.user_id) FROM user;"
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])
        return f"{username}_{arr[0] + 1}"

    def add_user(self, username, user_post, user_password_hash):
        user_id = self.generate_user_id(username)
        self.rbac_connection.execute("BEGIN")
        query_one = f"""INSERT INTO user_data(user_id, username, password_hash) 
                        VALUES ('{user_id}', '{username}', '{user_password_hash}');"""
        query_two = f"""INSERT INTO user(user_id, name, role_id) VALUES ('{user_id}', '{username}', 
                        (SELECT role.role_id FROM role WHERE role.desc = '{user_post}'));"""

        cursor = self.rbac_connection.execute(query_one)

        cursor = self.rbac_connection.execute(query_two)

        self.rbac_connection.execute("COMMIT")

    def add_post(self, post_id, post_desc, post_priority):
        query = (
            f"INSERT INTO role VALUES ('{post_id}', '{post_desc}', {post_priority});"
        )
        try:
            cursor = self.rbac_connection.execute(query)
            self.rbac_connection.commit()
        except Exception as e:
            print(e)

    def delete_post(self, post_id):
        query = f"DELETE FROM role WHERE role.role_id='{post_id}';"
        self.rbac_connection.execute(query)
        self.rbac_connection.commit()

    def assign_access_right_to_post(self, post_id, access_right_id):
        query = (
            f"INSERT INTO role_permission VALUES( '{post_id}', '{access_right_id}');"
        )
        try:
            self.rbac_connection.execute(query)
            self.rbac_connection.commit()
        except Exception as e:
            print(e)

    def delete_access_right_of_post(self, post_id, access_right_id):
        query = f"DELETE FROM role_permission WHERE role_id = '{post_id}' AND permission_id = '{access_right_id}';"
        try:
            self.rbac_connection.execute(query)
            self.rbac_connection.commit()
        except Exception as e:
            print(e)

    def get_post_id_from_post_name(self, post_name):
        query = f"SELECT role.role_id FROM role WHERE role.desc LIKE '%{post_name}%';"
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])

        return arr

    def change_user_post(self, user_id, post_id):
        query = f"UPDATE user SET role_id = '{post_id}' WHERE user_id = '{user_id}';"
        try:
            cursor = self.rbac_connection.execute(query)
            self.rbac_connection.commit()
            arr = []
            for i in cursor:
                arr.append(i[0])
            return arr
        except Exception as e:
            print(e)
            raise e

    def change_username(self, new_username, user_id):
        query_one = (
            f"UPDATE user SET name = '{new_username}' WHERE user_id = '{user_id}';"
        )
        query_two = f"UPDATE user_data SET username = '{new_username}' WHERE user_id = '{user_id}';"

        self.rbac_connection.execute("BEGIN")

        try:
            cursor = self.rbac_connection.execute(query_one)
            cursor = self.rbac_connection.execute(query_two)
            self.rbac_connection.commit()
            arr = []
            for i in cursor:
                arr.append(i[0])
            return arr
        except Exception as e:
            print(e)
            self.rbac_connection.execute("ROLLBACK")
            # due to auto commit this rollback is not required because if any
            # exception occurs the changes are not yet commited
        finally:
            # do commit here
            # self.rbac_connection.execute("COMMIT")
            pass


# must set autocommit of sqlite to false to avoid errors and full access control


class DatabaseConnectorTesting:
    def __init__(self):
        self.db = DatabaseConnector()
        # print(self.db.get_post_id_from_post_name("master"))
        # print(self.db.change_user_post("zed_15", "new_post_rand"))
        # print(self.db.change_username("zen", "zed_15"))

        # self.db.add_user("maron", "admin", "none")
        # self.db.add_post("org", "organizor", 7)
        # self.db.assign_access_right_to_post("org", "CUDFlags")
        # self.db.add_user("peter falcone", "organizor", "copy")
        # print(self.db.get_access_rights_by_post_id("sm"))
        # print(self.db.delete_access_right_of_post("sm", "CUDFlags"))
        # print(self.db.assign_access_right_to_post("sm", "CUDFlags"))

        # print(self.db.get_user_password("adam_12"))
        # print(self.db.get_user_rights(15))
        # print(self.db.get_available_access_rights())
        # print(self.db.set_user_password(16, "phil"))
        # print(self.db.set_user_password(17, "moray"))
        # print(self.db.set_user_password(18, "garry"))
        # print(self.db.set_user_password(19, "ben"))
        # print(self.db.set_user_password(31, "asdf"))
        # self.db.add_user("paul", "project_manager", "paul")
        # print(self.db.get_access_rights_for_post("team"))
        # print(self.db.get_user_post(13))
        # print(self.db.generate_user_id("asdf"))
        # print(self.db.add_user("asdf", "admin", "no_password"))
        # print(self.db.add_post("sm", "scrum_master", 10))
        # print(self.db.assign_access_right_to_post("sm", "CUDFlags"))
        # print(self.db.assign_access_right_to_post("sm", "CUDGroups"))
        # print(self.db.delete_post("root"))


if __name__ == "__main__":
    DatabaseConnectorTesting()
    pass