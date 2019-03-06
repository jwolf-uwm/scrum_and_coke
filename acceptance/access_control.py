# made by Grant

import unittest


class AccessTests(unittest.TestCase):
    def setup(self):
        self.ui.command("request_user_data userPass")

    """
       When a user attempts to access data, it takes in user credentials
       if User is in database as a Supervisor or Administrator, access
       access is granted
    """

    def test_command_request_data_correct_user(self):
        self.assertEqual(self.ui.command("request_user_data userPass"), "Access Granted")

    def test_command_request_data_incorrect_user(self):
        self.assertEqual(self.ui.command("request_user_data userPass"), "Access Denied")

    def test_command_request_data_no_arguments(self):
        self.asserEqual(self.ui.command("request_user_data"), "Access Denied")

    def test_command_request_data_incorrect_password(self):
        self.assertEqual(self.ui.command("request_user_data badUserPass"), "Access Denied")
