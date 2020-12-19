import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from model.hashalgo import hash_password, verify_password
from model.databaseconnector import DatabaseConnector


class Validator:
    def __init__(self):
        self.db = DatabaseConnector()

    def validate_user(self, user_id, password):
        orignal_hash = self.db.get_user_password(user_id)
        if verify_password(orignal_hash, password):
            print("correct credentials")
            return True
        else:
            return False

    def change_user_password(self, user_id, new_password):
        self.db.set_user_password(user_id, hash_password(new_password))

    def add_user(self, new_data):
        username = new_data["username"]
        user_post = new_data["user_post"]
        hash_password = new_data["user_password"]
        if username in [None, "", "None"]:
            return
        if user_post not in ["general", "project_manager", "team_lead", "admin"]:
            return
        self.db.add_user(
            new_data["username"],
            new_data["user_post"],
            hash_password(new_data["user_password"]),
        )

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


if __name__ == "__main__":
    # Validator().change_user_password(16, "phil")
    # Validator().change_user_password(17, "moray")
    # Validator().change_user_password(18, "garry")
    # Validator().change_user_password(19, "ben")
    # Validator().change_user_password(20, "dan")
    # Validator().change_user_password(21, "paul")
    # Validator().change_user_password(31, "asdf")
    pass