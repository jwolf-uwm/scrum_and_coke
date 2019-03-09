# created by Evan

from unittest import TestCase
from classes import Supervisor
from classes import Instructor
from classes import Course
from classes import TA
from classes import Administrator


class TestSupervisor(TestCase):

    def test_init(self):
        self.Sup1 = Supervisor("sup1@uwm.edu", "sup1name", "sup1pass")
        self.assertEqual(self.Sup1.email, "sup1@uwm.edu")
        self.assertEqual(self.Sup1.username, "sup1name")
        self.assertEqual(self.Sup1.password, "sup1pass")
        self.assertEqual(self.Sup1.name, "DEFAULT")
        self.assertEqual(self.Sup1.phone_number, "DEFAULT")

    def test_assign_instructor_course(self):
        self.Ins1 = Instructor("ins1@uwm.edu", "ins1name", "ins1pass")
        self.Course1 = Course("Intro to Computer Stuff", "CS101")

        # best case
        self.assertEqual(self.ui.command("assign_instructor ins1name CS101"), "sup1name was assigned to CS101")

        # entered arguments that don't exist
        self.assertEqual(self.ui.command("assign_instructor ins1name CS102"), "CS102 could not be assigned since"
                                                                              " it does not exist")
        self.assertEqual(self.ui.command("assign_instructor ins2name CS101"), "ins2name could not be assigned since"
                                                                              " it does not exist")

        # test number of arguments
        self.assertEqual(self.ui.command("assign_instructor ins1name"), "Error: too few arguments")
        self.assertEqual(self.ui.command("assign_instructor"), "Error: too few arguments")

        # test if class already has instructor
        self.Ins2 = Instructor("ins2@uwm.edu", "ins2name", "ins2pass")
        self.assertEqual(self.ui.command("assign_instructor ins2name CS101"), "CS101 already has been assigned an"
                                                                              " instructor")

        # test against non-instructors
        self.TA = TA("TA@uwm.edu", "TA", "TA")
        self.SUP = Supervisor("SUP@uwm.edu", "SUP", "SUP")
        self.ADMIN = Administrator("ADMN@uwm.edu", "ADMIN", "ADMIN")
        self.assertEqual(self.ui.command("assign_instructor TA CS101"), "Error: TA is not an instructor")
        self.assertEqual(self.ui.command("assign_instructor SUP CS101"), "Error: SUP is not an instructor")
        self.assertEqual(self.ui.command("assign_instructor ADMIN CS101"), "Error: ADMIN is not an instructor")

    def test_assign_ta_course(self):
        self.TA1 = TA("TA1@uwm.edu", "TA1", "TA1")
        self.Course1 = Course("Intro to Computer Stuff", "CS101")

        # best case
        self.assertEqual(self.ui.command("assign_ta_course TA1 CS101"), "TA1 was assigned to CS101")

        # entered arguments that don't exist
        self.assertEqual(self.ui.command("assign_ta_course TA2, CS101"), "TA2 could not be assigned since "
                                                                         "it does not exist")
        self.assertEqual(self.ui.command("assign_ta_course TA1, CS102"), "CS102 could not be assigned since "
                                                                         "it does not exist")

        # test number of arguments
        self.assertEqual(self.ui.command("assign_ta_course TA"), "Error: too few arguments")
        self.assertEqual(self.ui.command("assign_ta_course"), "Error: too few arguments")

        # test against non-TAs
        self.SUP = Supervisor("SUP@uwm.edu", "SUP", "SUP")
        self.ADMIN = Administrator("ADMN@uwm.edu", "ADMIN", "ADMIN")
        self.INS = Instructor("INS@uwm.edu", "INS", "INS")
        self.assertEqual(self.ui.command("assign_ta_course INS CS101"), "Error: INS is not a TA")
        self.assertEqual(self.ui.command("assign_ta_course SUP CS101"), "Error: SUP is not a TA")
        self.assertEqual(self.ui.command("assign_ta_course ADMIN CS101"), "Error: ADMIN is not a TA")

    def test_assign_ta_lab(self):
        self.TA1 = TA("TA1@uwm.edu", "TA1", "TA1")
        self.Course1 = Course("Intro to Computer Stuff", "CS101")
        self.Course1.section = 801
        self.assertEqual(self.ui.command("assign_ta_course TA1 CS101"), "TA1 was assigned to CS101")

        # best case
        self.assertEqual(self.ui.command("assign_ta_lab TA1 801"), "TA1 was assigned to lab 801")

        # entered arguments that don't exist
        self.assertEqual(self.ui.command("assign_ta_lab TA2, 801"), "TA2 could not be assigned since "
                                                                    "it does not exist")
        self.assertEqual(self.ui.command("assign_ta_lab TA1, 802"), "802 could not be assigned since "
                                                                    "it does not exist")

        # test number of arguments
        self.assertEqual(self.ui.command("assign_ta_lab TA"), "Error: too few arguments")
        self.assertEqual(self.ui.command("assign_ta_lab"), "Error: too few arguments")

        # test if lab section already has a TA
        self.TA2 = TA("TA2@uwm.edu", "TA2", "TA2")
        self.assertEqual(self.ui.command("assign_ta_lab TA2 801"), "Lab 801 already has been assigned a TA")

        # test against non-TAs
        self.SUP = Supervisor("SUP@uwm.edu", "SUP", "SUP")
        self.ADMIN = Administrator("ADMN@uwm.edu", "ADMIN", "ADMIN")
        self.INS = Instructor("INS@uwm.edu", "INS", "INS")
        self.assertEqual(self.ui.command("assign_ta_lab INS 801"), "Error: INS is not a TA")
        self.assertEqual(self.ui.command("assign_ta_lab SUP 801"), "Error: SUP is not a TA")
        self.assertEqual(self.ui.command("assign_ta_lab ADMIN 801"), "Error: ADMIN is not a TA")

