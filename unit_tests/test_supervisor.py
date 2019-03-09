# created by Evan

from unittest import TestCase
from classes.Supervisor import Supervisor
from classes.Instructor import Instructor
from classes.Course import Course
from classes.TA import TA
from classes.Administrator import Administrator


class TestSupervisor(TestCase):

    def test_init(self):
        sup1 = Supervisor("sup1@uwm.edu", "sup1pass")
        self.assertEqual(sup1.email, "sup1@uwm.edu")
        self.assertEqual(sup1.password, "sup1pass")
        self.assertEqual(sup1.name, "DEFAULT")
        self.assertEqual(sup1.phone_number, "DEFAULT")

    def test_assign_instructor_course(self):
        sup1 = Supervisor("sup1@uwm.edu", "sup1pass")
        self.Ins1 = Instructor("ins1@uwm.edu", "ins1pass")
        self.Course1 = Course("CS101", 401)

        # best case
        sup1.assign_instuctor("ins1@uwm.edu", "CS101", 401)
        self.assertEqual(Ins1.course)

    def test_assign_ta_course(self):
        ta1 = TA("TA1@uwm.edu", "TA1")
        course1 = Course("Intro to Computer Stuff", "CS101")



    def test_assign_ta_lab(self):

