# made by Dillan

import unittest


class CreateCourseTests(unittest.TestCase):
    def setup(self):
        self.ui.command("create_user Administrator")
        self.ui.command("create_user Supervisor")

    """
    When the create course cmd is entered, it takes < 3 > arguments:
    - Title
    - Instructor
    - Open TA slots
    If Title and Instructor fields are filled in, create course is a success:
    - "Create course successful."
    If Title field is omitted, failure:
    - "Error creating course."
    If Instructor field is omitted, failure:
    - "Error creating course."
    If Title already exists, failure:
    - "Error creating  course."
    """
    def test_command_create_course_correct(self):
        self.assertEqual(self.ui.command("create_course Administrator"), "Create course successful.")
        self.assertEqual(self.ui.command("create_course Supervisor"), "Create course successful.")

    def test_command_create_course_no_title(self):
        self.assertEqual(self.ui.command("create_course Administrator"), "Error creating course.")
        self.assertEqual(self.ui.command("create_course Supervisor"), "Error creating course.")

    def test_command_create_course_no_instructor(self):
        self.assertEqual(self.ui.command("create_course Administrator"), "Error creating course.")
        self.assertEqual(self.ui.command("create_course Supervisor"), "Error creating course.")

    def test_command_create_course_already_exists(self):
        self.ui.command("create_course Administrator")
        self.assertEqual(self.ui.command("create_course Administrator"), "Error creating course")
        self.ui.command("create_course Supervisor")
        self.assertEqual(self.ui.command("create_course Supervisor"), "Error creating course")
