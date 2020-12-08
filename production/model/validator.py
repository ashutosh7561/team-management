import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from model.hashalgo import hash_password, verify_password


def get_password_hash_from_database(username):
    # connection to database will come here
    # it will pass username and will recieve password_hash
    return hash_password(username)


def get_password_hash(password):
    # implement hashing algo here
    return password + "hash"


def validate_user(username, password):
    # password_hash = get_password_hash(password)
    orignal_hash = get_password_hash_from_database(username)
    # print(password_hash, orignal_hash)
    if verify_password(orignal_hash, password):
        print("correct credentials")
        return True
    else:
        return False


def get_access_rights(username):
    return ["CUDProjects", "CUDTeams", "CUDGroups"]