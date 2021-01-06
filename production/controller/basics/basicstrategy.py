from controller.delegator import Delegator


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