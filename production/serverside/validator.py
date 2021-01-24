import sys
from os.path import dirname, abspath
import os

# d = dirname(dirname(abspath(__file__)))
# sys.path.append(d)

from hashalgo import hash_password, verify_password
from databaseconnector import DatabaseConnector


class Validator:
    def __init__(self):
        self.db = DatabaseConnector()

    def validate_user(self, user_id, password):
        orignal_hash = self.db.get_user_password(user_id)
        if orignal_hash is None:
            return False
        if verify_password(orignal_hash, password):
            return True
        else:
            return False

    def change_user_password(self, user_id, new_password):
        self.db.set_user_password(user_id, hash_password(new_password))

    def add_user(self, new_data):
        username = new_data["username"]
        user_post = new_data["user_post"]
        password_hash = hash_password(new_data["user_password"])
        if username in [None, "", "None"]:
            return
        if user_post not in ["general", "project_manager", "team_manager", "admin"]:
            return
        self.db.add_user(username, user_post, password_hash)

    def get_users_data(self):
        user_data_list = []
        data = self.db.get_users_data()
        for i in data:
            t = {
                "username": i[0],
                "user_id": i[1],
                "user_post": i[2],
                "user_other_data": "None",
                "user_special_rights": "None",
            }
            user_data_list.append(t)
        return user_data_list

    def create_post(self, post_id, post_desc, post_priority, access_rights=[]):
        self.db.add_post(post_id, post_desc, post_priority)

        for right in access_rights:
            self.db.assign_access_right_to_post(post_id, right)

    def change_post_rights(self, post_id, new_access_rights=[]):
        old_access_rights = self.db.get_access_rights_by_post_id(post_id)
        for right in old_access_rights:
            self.db.delete_access_right_of_post(post_id, right)

        for right in new_access_rights:
            self.db.assign_access_right_to_post(post_id, right)


if __name__ == "__main__":
    # Validator().change_post_rights("sm", ["CUDFlags", "CUDGroups"])
    # Validator().create_post( "CEO", "CEO", 0, ["CUDGroups", "CUDFlags", "CUDTeams"]
    # )
    # Validator().create_post("CEO", "CEO", 0 )
    pass