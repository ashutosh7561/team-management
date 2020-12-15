import sqlite3


class DatabaseConnector:
    def __init__(
        self,
        database="C:\\Users\\Ashutosh\\Desktop\\pp\\repo\\team-management\\production\\model\\rbac.db",
    ):
        self.rbac_connection = sqlite3.connect(database)

    def get_user_password(self, user_id):
        query = f"SELECT user_data.password_hash from user_data where user_data.user_id={user_id}"
        try:
            cursor = self.rbac_connection.execute(query)
            for i in cursor:
                return i[0]
        except:
            return ""

    def set_user_password(self, user_id, user_password):
        pass

    def get_user_rights(self, user_id):
        query = f"SELECT permission.perm_desc FROM user, role_permission, permission, role WHERE user.role_id = role_permission.role_id AND role_permission.permission_id = permission.permission_id AND user.role_id = role.role_id AND user.user_id='{user_id}';"
        cursor = self.rbac_connection.execute(query)
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr