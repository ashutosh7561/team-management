import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from model.authenticator import validate_user, get_access_rights


def authenticate(username, password):
    is_valid = validate_user(username, password)
    if is_valid:
        access_rights = get_access_rights(username)
        return access_rights
    else:
        return False