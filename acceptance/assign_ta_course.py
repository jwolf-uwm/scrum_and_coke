import unittest


class AssignTACourse(unittest.TestCase):
        def setUp(self):
                self.TA1 = ("TA1@uwm.edu", "TA1")
                self.Course1 = ("Intro to Computer Stuff", "CS101", 801)
                self.assertEqual(self.ui.command("assign_ta_course TA1@uwm.edu CS101"),
                                 "TA1@uwm.edu was assigned to CS101")

        def assign_ta_Course(self):
                # best case
                self.assertEqual(self.ui.command("assign_ta_course TA1@uwm.edu CS101"),
                                 "TA1@uwm.edu was assigned to CS101")

        def assign_ta_course_args_dne(self):
                # entered arguments that don't exist
                self.assertEqual(self.ui.command("assign_ta_course TA1, CS101"), "Error: invalid email address")
                self.assertEqual(self.ui.command("assign_ta_course TA2@uwm.edu, CS101"),
                                 "TA2@uwm.edu could not be assigned since it does not exist")
                self.assertEqual(self.ui.command("assign_ta_course TA1@uwm.edu, CS102"),
                                 "CS102 could not be assigned since it does not exist")

        def assign_ta_course_num_args(self):
                # test number of arguments
                self.assertEqual(self.ui.command("assign_ta_course TA@uwm.edu"), "Error: too few arguments")
                self.assertEqual(self.ui.command("assign_ta_course"), "Error: too few arguments")

        def assign_ta_course_non_ta(self):
                # test against non-TAs
                self.SUP = ("SUP@uwm.edu", "SUP")
                self.ADMIN = ("ADMN@uwm.edu", "ADMIN")
                self.INS = ("INS@uwm.edu", "INS")
                self.assertEqual(self.ui.command("assign_ta_course INS@uwm.edu CS101"),
                                 "Error: INS@uwm.edu is not a TA")
                self.assertEqual(self.ui.command("assign_ta_course SUP@uwm.edu CS101"),
                                 "Error: SUP@uwm.edu is not a TA")
                self.assertEqual(self.ui.command("assign_ta_course ADMIN@uwm.edu CS101"),
                                 "Error: ADMIN@uwm.edu is not a TA")