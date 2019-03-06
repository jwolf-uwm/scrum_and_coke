import unittest


class CreateAccountTests(unittest.TestCase):
    def setup(self):
        self.ui.command("create_user Supervisor SupervisorPassword")
        self.ui.command("create_user Administrator AdministratorPassword")
        self.ui.command("create_user Instructor InstructorPassword")
        self.ui.command("create_user TA TAPassword")
