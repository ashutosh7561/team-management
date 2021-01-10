import sys
from os.path import dirname, abspath
import os

d = dirname(dirname(abspath(__file__)))
d2 = dirname(dirname(dirname(abspath(__file__))))

sys.path.append(d)
sys.path.append(d2)


import unittest

from controller.userfactory import UserFactory
from controller.basics.basicstrategy import *
from controller.chats.chatstrategy import *


class ClassStructureTest(unittest.TestCase):
    def test_basic_user_creation(self):
        user = UserFactory().create_user("alex", "basic", True)

        self.assertIsInstance(user, BasicOperationHandler)
        self.assertEqual(user.login("alex", "alex"), None)
        self.assertEqual(user.logout(), None)
        self.assertEqual(user.feed_userdata("alex"), None)

        with self.assertRaises(NotImplementedError):
            user.send_message()

    def test_groupadmin_user_creation(self):
        user = UserFactory().create_user("alex", "group_creation", True)

        self.assertIsInstance(user, BasicOperationHandler)
        self.assertIsInstance(user.delegatee, GroupAdminStratrgy)

        self.assertEqual(user.login("alex", "alex"), None)
        self.assertEqual(user.logout(), None)
        self.assertEqual(user.feed_userdata("alex"), None)

        self.assertEqual(user.send_message("test_groupone", "test_message"), None)
        self.assertEqual(user.get_message_info("test_groupone", "test_message_1"), None)

        self.assertEqual(user.add_member("test_groupone", "test_member_1"), None)
        self.assertEqual(user.delete_member("test_groupone", "test_member_1"), None)
        self.assertEqual(user.list_members("test_groupone"), None)

        self.assertEqual(
            user.update_chatinfo(
                "test_groupone", "test_group", "testing group description"
            ),
            None,
        )
        self.assertEqual(user.delete_chat("test_groupone"), None)
        self.assertEqual(user.archieve_chat("test_groupone"), None)

    def test_groupadmintwo_user_creation(self):
        user = UserFactory().create_user("alex", "group_creation", False)

        self.assertIsInstance(user, BasicOperationHandler)
        self.assertIsInstance(user.delegatee, GroupAdminStratrgy)

        self.assertEqual(user.login("alex", "alex"), None)
        self.assertEqual(user.logout(), None)
        self.assertEqual(user.feed_userdata("alex"), None)

        self.assertEqual(user.send_message("test_groupone", "test_message"), None)
        self.assertEqual(user.get_message_info("test_groupone", "test_message_1"), None)

        self.assertEqual(
            user.update_chatinfo(
                "test_groupone", "test_group", "testing group description"
            ),
            None,
        )
        self.assertEqual(user.delete_chat("test_groupone"), None)
        self.assertEqual(user.archieve_chat("test_groupone"), None)

        with self.assertRaises(NotImplementedError):
            user.add_member("test_groupone", "test_member_1"), None
            user.delete_member("test_groupone", "test_member_1"), None
            user.list_members("test_groupone"), None

    def test_groupmember_user_creation(self):
        user = UserFactory().create_user("alex", "group_member", True)

        self.assertIsInstance(user, BasicOperationHandler)
        self.assertIsInstance(user.delegatee, GroupMemberStrategy)

        self.assertEqual(user.login("alex", "alex"), None)
        self.assertEqual(user.logout(), None)
        self.assertEqual(user.feed_userdata("alex"), None)

        user.send_message("test_groupone", "test_message")
        user.get_message_info("test_groupone", "test_message_1")

        user.update_chatinfo("test_groupone", "test_group", "testing group description")
        user.delete_chat("test_groupone")
        user.archieve_chat("test_groupone")

        with self.assertRaises(NotImplementedError):
            user.add_member("test_groupone", "test_member_1")
            user.delete_member("test_groupone", "test_member_1")
            user.list_members("test_groupone")

    def test_groupmembertwo_user_creation(self):
        user = UserFactory().create_user("alex", "group_member", False)

        self.assertIsInstance(user, BasicOperationHandler)
        self.assertIsInstance(user.delegatee, GroupMemberStrategy)

        self.assertEqual(user.login("alex", "alex"), None)
        self.assertEqual(user.logout(), None)
        self.assertEqual(user.feed_userdata("alex"), None)

        with self.assertRaises(NotImplementedError):
            user.send_message("test_groupone", "test_message")
            user.get_message_info("test_groupone", "test_message_1")

            user.add_member("test_groupone", "test_member_1")
            user.delete_member("test_groupone", "test_member_1")
            user.list_members("test_groupone")

            user.update_chatinfo(
                "test_groupone", "test_group", "testing group description"
            )
            user.delete_chat("test_groupone")
            user.archieve_chat("test_groupone")


if __name__ == "__main__":
    unittest.main()