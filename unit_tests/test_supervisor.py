# created by Evan

from unittest import TestCase
from classes.Supervisor import Supervisor
from classes.Administrator import Administrator
from classes.Instructor import Instructor
from classes.TA import TA
from classes.Course import Course


class TestSupervisor(TestCase):
    sup = Supervisor("sup@uwm.edu", "sup_pass")
    admin = Administrator("admin@uwm.edu", "admin_pass")
    ins = Instructor("ins@uwm.edu", "ins_pass")
    ta = TA("ta@uwm.edu", "ta_pass")
    course1 = Course("Intro to Computer Stuff", "CS101")

    def test_assign_instructor_course(self):
        

    def test_assign_ta_course(self):


    def test_assign_ta_lab(self):

