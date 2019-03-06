import unittest


class AssignInstructorTests(unittest.TestCase):
    def setup(self):

        # Think we should instantiate things once we have unit tests, and not use commands for this. - Jeff

        self.ui.command("create_user Supervisor SupervisorPassword")
        self.ui.command("create_user Administrator AdministratorPassword")
        self.ui.command("create_user Instructor InstructorId InstructorPassword")
        self.ui.command("create_user Instructor2 InstructorId2 InstructorPassword2")
        self.ui.command("create_user TA TAId TAPassword")
        self.ui.command("create_cs_class SomeCSClass CS101")
        self.ui.command("create_cs_class SomeCSClass2 CS102")
        self.ui.command("create_cs_class SomeCSClass3 CS103")
        self.ui.command("create_cs_class SomeCSClass4 CS104")
        self.ui.command("create_cs_class SomeCSClass5 CS105")
        self.ui.command("create_cs_class SomeCSClass6 CS106")

    """
        Assigning an instructor requires user logged in as Supervisor or Administrator.
        When the create account command is entered, it takes two arguments:
            - Instructor ID
            - Course ID
        If the course does not currently have an instructor, assigns instructor to that course and
        is successful:
        - "Instructor *Instructor Name* assigned to class *Class Name*."
        If the course is already assigned to an instructor then failure:
        - "*Class Name* already has an instructor."
        If the Instructor ID or Course ID is omitted, failure:
        - "Invalid arguments in command."
        If attempting to assign a role that is not instructor, failure:
        - "Only instructors can be assigned to classes."
        If the user is not logged in as a Supervisor or Administrator, failure:
        - "You are not authorized to assign instructors."
    """

    """ 
        NOTE: Should we add the functionality to remove/edit a course from an instructor, or create
        a new user story for this? - Jeff
    """

    def test_command_assign_instructor_supervisor(self):
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor.id SomeCSClass"),
                         "Instructor " + Instructor.name + " assigned to " + SomeCSClass.name + ".")

    def test_command_assign_instructor_administrator(self):
        self.ui.command("login Administrator AdministratorPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor.id SomeCSClass2"),
                         "Instructor " + Instructor.name + " assigned to " + SomeCSClass2.name + ".")

    def test_command_assign_instructor_instructor(self):
        self.ui.command("login Instructor InstructorPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor.id SomeCSClass3"),
                         "You are not authorized to assign instructors.")

    def test_command_assign_instructor_TA(self):
        self.ui.command("login TA TAPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor.id SomeCSClass3"),
                         "You are not authorized to assign instructors.")

    def test_command_assign_instructor_class_taken(self):
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor2.id SomeCSClass"),
                         SomeCSClass.name + " already has an instructor.")

    def test_command_assign_instructor_invalid_arguments(self):
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_instructor Instructor.id"),
                         "Invalid arguments in command.")

    def test_command_assign_instructor_assign_TA(self):
        self.ui.command("login Supervisor SupervisorPassword")
        self.assertEqual(self.ui.command("assign_instructor TA.id SomeCSClass3"),
                         "Only instructors can be assigned to classes.")
