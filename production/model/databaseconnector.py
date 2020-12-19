import sqlite3


class DatabaseConnector:
    def __init__(
        self,
        database="C:\\Users\\Ashutosh\\Desktop\\pp\\repo\\team-management\\production\\model\\rbac.db",
    ):
        self.rbac_connection = sqlite3.connect(database)

    def get_user_password(self, user_id):
        query = f"SELECT user_data.password_hash from user_data where user_data.user_id={user_id};"
        try:
            cursor = self.rbac_connection.execute(query)
            for i in cursor:
                return i[0]
        except:
            return ""

    def set_user_password(self, user_id, new_password_hash):
        query = f"UPDATE user_data SET password_hash = '{new_password_hash}' WHERE user_id = {user_id};"
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
                    role.desc = '{post_name}';"""
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr

    def get_user_post(self, user_id):
        query = f"SELECT role.desc FROM role, user WHERE user.role_id = role.role_id AND user.user_id = {user_id};"
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr[0]

    def get_users_data(self):
        query = f"""SELECT user.name, user.user_id, role.desc FROM user, role WHERE 
                    user.role_id = role.role_id ORDER BY user.user_id;"""
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i)
        return arr

    def add_user(self, username, user_post, user_password_hash):
        query_one = f"""INSERT INTO user_data(username, password_hash) VALUES ('{username}', '{user_password_hash}');"""
        query_two = f"""INSERT INTO user(name, role_id) VALUES ('{username}', 
                        (SELECT role.role_id FROM role WHERE role.desc = '{user_post}'));"""

        cursor = self.rbac_connection.execute(query_one)
        self.rbac_connection.commit()

        cursor = self.rbac_connection.execute(query_two)
        self.rbac_connection.commit()


class DatabaseConnectorTesting:
    def __init__(self):
        self.db = DatabaseConnector()
        # print(self.db.get_user_password(11))
        # print(self.db.get_user_rights(15))
        # print(self.db.get_available_access_rights())
        # print(self.db.set_user_password(16, "phil"))
        # print(self.db.set_user_password(17, "moray"))
        # print(self.db.set_user_password(18, "garry"))
        # print(self.db.set_user_password(19, "ben"))
        # print(self.db.set_user_password(31, "asdf"))
        # self.db.add_user("paul", "project_manager", "paul")
        # print(self.db.get_access_rights_for_post("team_lead"))
        # print(self.db.get_user_post(13))


if __name__ == "__main__":
    DatabaseConnectorTesting()
    pass