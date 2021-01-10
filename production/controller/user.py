from abc import ABC, abstractmethod


class Delegator:
    def __init__(self, delegatee=None, *args, **kwargs):
        self.delegatee = delegatee

    def __getattr__(self, called_method):
        if hasattr(self.delegatee, called_method):
            return getattr(self.delegatee, called_method)
        else:
            return self.dummy

    def dummy(self, *args, **kwargs):
        raise NotImplementedError


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


class BasicOperationHandler(Delegator):
    def __init__(self, username=None):
        self.username = username

    def login(self, user_id, password):
        print("authenticating user credentials")

    def logout(self):
        print("logging out the user")

    def feed_userdata(self, username):
        print("feeding user data")
        self.username = username


class GroupOperationHandler(ABC, Delegator):
    pass


class GroupMemberStrategy(GroupOperationHandler):
    def __getattr__(self, attr_name):
        for i in self.features:
            if hasattr(i, attr_name):
                return getattr(i, attr_name)
        else:
            return self.dummy

    def dummy(self, *args, **kwrags):
        raise NotImplementedError

    def __init__(self, can_message):
        self.features = []
        if can_message:
            self.features.append(ChatOperation())
            self.features.append(MessagingOperation())
        else:
            pass


class GroupAdminStratrgy(GroupOperationHandler):
    def __getattr__(self, attr_name):
        for i in self.features:
            if hasattr(i, attr_name):
                return getattr(i, attr_name)
        else:
            return self.dummy

    def dummy(self, *args, **kwargs):
        raise NotImplementedError

    def __init__(self, is_admin):
        self.features = []
        self.features.append(ChatOperation())
        self.features.append(MessagingOperation())
        if is_admin:
            self.features.append(MemberOperation())
            # provide funcionality for admin
            pass
        else:
            # overwride admin fucntionality to empty implementation
            pass


class ChatOperation:
    def update_chatinfo(self, chat_id, chat_name, chat_desc=None):
        print("updating chat info for:", chat_id)

    def delete_chat(self, chat_id):
        print("deleting chat:", chat_id)

    def archieve_chat(self, chat_id):
        print("archiving chat:", chat_id)


class MessagingOperation:
    def send_message(self, chat_id, message=None):
        print(f"sending message {message} in chat {chat_id}")

    def get_message_info(self, chat_id, message_id):
        print(
            f"message info for {message_id} : some data like sending time, recipient, read status"
        )


class MemberOperation:
    def add_member(self, chat_id, memeber_id):
        print(f"adding {memeber_id} to chat: {chat_id}")

    def delete_member(self, chat_id, member_id):
        print(f"deleting {member_id} from chat: {chat_id}")

    def list_members(self, chat_id):
        print(f"list of members in chat: {chat_id}")
        for i in range(3):
            print(i)
