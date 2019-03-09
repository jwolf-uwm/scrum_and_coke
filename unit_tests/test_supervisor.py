# created by Evan

from unittest import TestCase
from classes.Supervisor import Supervisor
from classes.Instructor import Instructor
from classes.Course import Course
from classes.TA import TA
from classes.Administrator import Administrator


class TestSupervisor(TestCase):

    def test_init(self):
        self.Sup1 = Supervisor("sup1@uwm.edu", "sup1pass")
        self.assertEqual(self.Sup1.email, "sup1@uwm.edu")
        self.assertEqual(self.Sup1.password, "sup1pass")
        self.assertEqual(self.Sup1.name, "DEFAULT")
        self.assertEqual(self.Sup1.phone_number, "DEFAULT")

    def test_assign_instructor_course(self):
        self.Sup1 = Supervisor("sup1@uwm.edu", "sup1pass")
        self.Ins1 = Instructor("ins1@uwm.edu", "ins1pass")
        self.Course1 = Course("CS101", 401)

        # best case
        self.Sup1.assign_instuctor("ins1@uwm.edu", "CS101", 401)



    def test_assign_ta_course(self):
        self.TA1 = TA("TA1@uwm.edu", "TA1")
        self.Course1 = Course("Intro to Computer Stuff", "CS101")

        # best case
        self.assertEqual(self.ui.command("assign_ta_course TA1@uwm.edu CS101"), "TA1@uwm.edu was assigned to CS101")

        # entered arguments that don't exist
        self.assertEqual(self.ui.command("assign_ta_course TA1, CS101"), "Error: invalid email address")
        self.assertEqual(self.ui.command("assign_ta_course TA2@uwm.edu, CS101"), "TA2@uwm.edu could not be assigned "
                                                                                 "since it does not exist")
        self.assertEqual(self.ui.command("assign_ta_course TA1@uwm.edu, CS102"), "CS102 could not be assigned since "
                                                                                 "it does not exist")

        # test number of arguments
        self.assertEqual(self.ui.command("assign_ta_course TA@uwm.edu"), "Error: too few arguments")
        self.assertEqual(self.ui.command("assign_ta_course"), "Error: too few arguments")

        # test against non-TAs
        self.SUP = Supervisor("SUP@uwm.edu", "SUP")
        self.ADMIN = Administrator("ADMN@uwm.edu", "ADMIN")
        self.INS = Instructor("INS@uwm.edu", "INS")
        self.assertEqual(self.ui.command("assign_ta_course INS@uwm.edu CS101"), "Error: INS@uwm.edu is not a TA")
        self.assertEqual(self.ui.command("assign_ta_course SUP@uwm.edu CS101"), "Error: SUP@uwm.edu is not a TA")
        self.assertEqual(self.ui.command("assign_ta_course ADMIN@uwm.edu CS101"), "Error: ADMIN@uwm.edu is not a TA")

    def test_assign_ta_lab(self):
        self.TA1 = TA("TA1@uwm.edu", "TA1")
        self.Course1 = Course("Intro to Computer Stuff", "CS101")
        self.Course1.section = 801
        self.assertEqual(self.ui.command("assign_ta_course TA1@uwm.edu CS101"), "TA1@uwm.edu was assigned to CS101")

        # best case
        self.assertEqual(self.ui.command("assign_ta_lab TA1@uwm.edu 801"), "TA1@uwm.edu was assigned to lab 801")

        # entered arguments that don't exist
        self.assertEqual(self.ui.command("assign_ta_lab TA1, 801"), "Error: invalid email address")
        self.assertEqual(self.ui.command("assign_ta_lab TA2@uwm.edu, 801"), "TA2@uwm.edu could not be assigned since "
                                                                            "it does not exist")
        self.assertEqual(self.ui.command("assign_ta_lab TA1@uwm.edu, 802"), "802 could not be assigned since "
                                                                            "it does not exist")

        # test number of arguments
        self.assertEqual(self.ui.command("assign_ta_lab TA@uwm.edu"), "Error: too few arguments")
        self.assertEqual(self.ui.command("assign_ta_lab"), "Error: too few arguments")

        # test if lab section already has a TA
        self.TA2 = TA("TA2@uwm.edu", "TA2")
        self.assertEqual(self.ui.command("assign_ta_lab TA2@uwm.edu 801"), "Lab 801 already has been assigned a TA")

        # test against non-TAs
        self.SUP = Supervisor("SUP@uwm.edu", "SUP")
        self.ADMIN = Administrator("ADMN@uwm.edu", "ADMIN")
        self.INS = Instructor("INS@uwm.edu", "INS")
        self.assertEqual(self.ui.command("assign_ta_lab INS@uwm.edu 801"), "Error: INS@uwm.edu is not a TA")
        self.assertEqual(self.ui.command("assign_ta_lab SUP@uwm.edu 801"), "Error: SUP@uwm.edu is not a TA")
        self.assertEqual(self.ui.command("assign_ta_lab ADMIN@uwm.edu 801"), "Error: ADMIN@uwm.edu is not a TA")

