from controller.chats.chatoperation import ChatOperation
from controller.chats.memberoperation import MemberOperation
from controller.chats.messagingoperation import MessagingOperation


class GroupMemberStrategy:
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


class GroupAdminStratrgy:
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