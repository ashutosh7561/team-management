import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from model.validator import validate_user, get_access_rights


def authenticate(user_id, password):
    is_valid = validate_user(user_id, password)
    if is_valid:
        access_rights = get_access_rights(user_id)
        return access_rights
    else:
        return False