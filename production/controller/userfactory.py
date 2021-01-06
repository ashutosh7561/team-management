import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from controller.basics.basicstrategy import BasicOperationHandler
from controller.chats.chatstrategy import GroupAdminStratrgy, GroupMemberStrategy


class UserFactory:
    def create_user(self, username, user_post, other_rights):
        user = BasicOperationHandler(username)  # default features
        user.delegatee = None

        if user_post == "group_creation":
            group_strategy = GroupAdminStratrgy(other_rights)
            user.delegatee = group_strategy
        elif user_post == "group_member":
            group_strategy = GroupMemberStrategy(other_rights)
            user.delegatee = group_strategy

        return user