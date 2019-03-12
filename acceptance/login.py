#made by matt
import unittest

class LoginTests(unittest.TestCase)
    def setUp(self):
        self.ui.command("create_user Admin1 AdminPassword")
        self.ui.command("create_user Supervisor1 SupervisorPassword")
        self.ui.command("create_user TA1 TAPassword")
        self.ui.command("create_user Instructor1 InstructorPassword")
    """
    When a user wants to login two arguments are required
        -Username
        -password
    the password must match the password for the given username
    if login is successful
        -"login successful" displayed"
    if password is incorrect
        -"password invalid" displayed
    if username does not exist
        -"no such user" displayed
    """
    def test_valid_login_Admin(self):
        self.assertEqual(self.ui.command("Login Admin1 AdminPassword "), "login successful")

    def test_invalid_login_Admin(self):
        self.assertEqual(self.ui.command("Login Admin1 AdminPaword "), "Password invalid")
        self.assertEqual(self.ui.command("Login Admin2 AdminPassword"), "No such user")

    def test_valid_login_TA(self):
        self.assertEqual(self.ui.command("Login TA1 TAPassword "), "login successful")

    def test_invalid_login_TA(self):
        self.assertEqual(self.ui.command("Login TA1 AdminPaword "), "Password invalid")
        self.assertEqual(self.ui.command("Login TA2 TAPassword"), "No such user")

    def test_valid_login_Instructor(self):
        self.assertEqual(self.ui.command("Login Instructor1 InstructorPassword "), "login successful")

    def test_invalid_login_Instructor(self):
        self.assertEqual(self.ui.command("Login Instructor1 AdminPaword "), "Password invalid")
        self.assertEqual(self.ui.command("Login Instructor2 InstructorPassowrd"), "No such user")

    def test_valid_login_Supervisor(self):
        self.assertEqual(self.ui.command("Login Supervisor1 SupervisorPassword "), "login successful")

    def test_invalid_login_Admin(self):
        self.assertEqual(self.ui.command("Login Supervisor1 AdminPaword "), "Password invalid")
        self.assertEqual(self.ui.command("Login Supervisor2 SupervisorPassowrd"), "No such user")
