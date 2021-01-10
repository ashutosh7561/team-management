import unittest

from chatdbconnector import *


class ClassStructureTest(unittest.TestCase):
    def test_getting_group_members(self):
        c = ChatDatabaseConnector()
        self.assertIsInstance(c.get_group_members("group_one"), list)
        self.assertIsInstance(c.get_group_members("group_three"), list)

    def test_getting_user_buffer(self):
        c = ChatDatabaseConnector()
        self.assertIsInstance(c.get_user_buffer("alex_11", "group_one"), list)
        self.assertIsInstance(c.get_user_buffer("alex_11", "not_existing"), list)


if __name__ == "__main__":
    unittest.main()