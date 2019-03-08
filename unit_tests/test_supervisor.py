# created by Evan

from unittest import TestCase
from classes import Supervisor
from classes import Instructor
from classes import Course


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
        self.assertEqual(self.ui.command("assign_instructor ins1name CS101"), "sup1name was assigned to CS101")
        self.assertEqual(self.ui.command("assign_instructor ins1name CS102"), "CS102 could not be assigned since"
                                                                              " it does not exist")
        self.assertEqual(self.ui.command("assign_instructor ins2name CS101"), "ins2name could not be assigned since"
                                                                              " it does not exist")
        self.assertEqual(self.ui.command("assign_instructor ins1name"), "Error: too few arguments")
        self.assertEqual(self.ui.command("assign_instructor"), "Error: too few arguments")

        self.Ins2 = Instructor("ins2@uwm.edu", "ins2name", "ins2pass")
        self.assertEqual(self.ui.command("assign_instructor ins2name CS101"), "CS101 already has been assigned an"
                                                                              " instructor")
        self.TA = Instructor("TA@uwm.edu", "TA", "TA")
        self.SUP = Instructor("SUP@uwm.edu", "SUP", "SUP")
        self.ADMIN = Instructor("ADMN@uwm.edu", "ADMIN", "ADMIN")

        self.assertEqual(self.ui.command("assign_instructor TA CS101"), "Error: TA is not an instructor")
        self.assertEqual(self.ui.command("assign_instructor SUP CS101"), "Error: SUP is not an instructor")
        self.assertEqual(self.ui.command("assign_instructor ADMIN CS101"), "Error: ADMIN is not an instructor")

    def test_assign_ta_course(self):
        self.fail()

    def test_assign_ta_lab(self):
        self.fail()
