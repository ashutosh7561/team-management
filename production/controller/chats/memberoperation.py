class MemberOperation:
    def add_member(self, chat_id, memeber_id):
        print(f"adding {memeber_id} to chat: {chat_id}")

    def delete_member(self, chat_id, member_id):
        print(f"deleting {member_id} from chat: {chat_id}")

    def list_members(self, chat_id):
        print(f"list of members in chat: {chat_id}")
        for i in range(3):
            print(i)