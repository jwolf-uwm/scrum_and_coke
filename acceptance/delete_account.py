# made by Evan

import unittest


class DeleteTests(unittest.TestCase):
    def setup(self):
        self.ui.command("create_user Admin AdminPassword")
        self.ui.command("create_user Supervisor SupervisorPassword")
        self.ui.commant("create_user TA TAPassword")
        self.ui.command("create_user Instructor InstructorPassword")

    """
        When the delete command is entered, it takes one argument:
        - Username
        If the user has permission to delete and
        the username matches the database entry
        the user delete is successful:
        - "User deleted successfully"
        If the user does not have permission, failure:
        - "You do not have permission to delete users"
        If the username does not match or is omitted, failure:
        - "Error deleting account"
    """

    def test_delete_fromAdmin(self):
        self.ui.command("login Admin AdminPassword")
        self.assertEqual(self.ui.command("delete TA"), "User deleted successfully")

    def test_delete_fromSupervisor(self):
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("delete TA"), "User deleted successfully")

    def test_delete_fromInstructor(self):
        self.ui.command("login Instructor InstructorPassword")
        self.assertEqual(self.ui.command("delete TA"), "You do not have permission to delete users")

    def test_delete_fromTA(self):
        self.ui.command("login TA TAPassword")
        self.assertEqual(self.ui.command("delete TA"), "You do not have permission to delete users")

    def test_delete_no_args(self):
        self.assertEqual(self.ui.command("delete"), "Error deleting account")

    def test_delete_wrongUsername(self):
        self.assertEqual(self.ui.command("delete TA1"), "Error deleting account")
