class MessagingOperation:
    def send_message(self, chat_id, message=None):
        print(f"sending message {message} in chat {chat_id}")

    def get_message_info(self, chat_id, message_id):
        print(
            f"message info for {message_id} : some data like sending time, recipient, read status"
        )