import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from model.hashalgo import hash_password, verify_password
from model.databaseconnector import DatabaseConnector


def validate_user(user_id, password):
    orignal_hash = DatabaseConnector().get_user_password(user_id)
    if verify_password(orignal_hash, password):
        print("correct credentials")
        return True
    else:
        return False


def get_access_rights(user_id):
    return DatabaseConnector().get_user_rights(user_id)