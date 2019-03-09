# created by Evan

from unittest import TestCase
from classes.Supervisor import Supervisor


class TestSupervisor(TestCase):
    def setUp(self):
        self.sup = Supervisor("sup@uwm.edu", "sup_pass")

        # fake instructors
        self.ins1_courses = []
        self.ins1 = "ins1@uwm.edu"
        self.ins2_courses = []
        self.ins2 = "in2s@uwm.edu"

        # fake course
        self.course1_tas = []
        self.course1_instructor
        self.course1 = ("CS101", 2)
        self.course2_tas = []
        self.course2_instructor
        self.course2 = ("CS202", 0)

        # fake ta
        self.ta_sections = []
        self.tas = "tas@uwm.edu"

    def test_assign_instructor_course(self):
        # instructor 1 is assigned CS101
        self.sup.assign_instructor(self.ins1, self.course1[0])
        self.assertEqual(self.ins1_courses[0], "CS101")
        self.assertEqual(self.course1_instructor, "ins1@uwm.edu")

        # assign instructor 1 another course
        self.sup.assign_instructor(self.ins1, self.course2[0])
        self.assertEqual(self.ins1_courses[1], "CS202")
        self.assertEqual(self.course2_instructor, "ins1@uwm.edu")

        # instructor 2 is assigned CS101
        self.sup.assign_instructor(self.ins2, self.course1[0])
        self.assertEqual(self.ins2_courses[0], "CS101")
        self.assertEqual(self.course1_instructor, "ins2@uwm.edu")
        self.assertNotEqual(self.ins1_courses[0], "CS101")

        self.assertRaises(self.sup.assign_instructor(self.tas, self.course1[0]), TypeError)

    def test_assign_ta_course(self):


    def test_assign_ta_lab(self):

