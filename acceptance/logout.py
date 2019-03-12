#made by matt

import unittest

class LoginTests(unittest.TestCase)
    def setUp(self):
        self.ui.command("create_user Admin AdminPassword")
        self.ui.command("create_user Supervisor SupervisorPassword")
        self.ui.command("create_user TA TAPassword")
        self.ui.command("create_user Instructor InstructorPassword")
    """
    When a user wants to logout no arguments are required 
    if logout works properly
        -"logout successful"
    if logout does not work
        -"logout failed"
    """

    def test_logout_Admin(self):
        self.ui.command("login Admin AdminPassword")
        self.assertEqual(self.ui.command("logout"), "logout successful")

    def test_logout_TA(self):
        self.ui.command("login TA TAPassword")
        self.assertEqual(self.ui.command("logout"), "logout successful")

    def test_logout_Instructor(self):
        self.ui.command("login Instructor InstructorPassword")
        self.assertEqual(self.ui.command("logout"), "logout successful")

    def test_logout_Supervisor(self):
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("logout"), "logout successful")

    def test_invalid_logout(self):
        self.assertEqual(self.ui.command("logout"), "logout failed")