import unittest
from locker import User, Credential

class TestUser(unittest.TestCase):
    """
        Test class that defines test cases for the user class behaviours.
    """

    def setUp(self):
        self.created_user = User("Kiptoo", "1997")


    def tearDown(self):
        User.user_list = []


    def test_init(self):
        self.assertEqual(self.created_user.name, "Kiptoo")
        self.assertEqual(self.created_user.user_password, "1997")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
        the user list
        """

        self.created_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        self.created_user.save_user()
        test_user = User("Kevin", "1050")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from our users list
        """
        self.created_user.save_user()
        test_user = User("Kevin", "1050")
        test_user.save_user()

        self.created_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
    unittest.main()