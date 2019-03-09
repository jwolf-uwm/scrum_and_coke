# created by Evan

from unittest import TestCase
from classes.Supervisor import Supervisor


class TestSupervisor(TestCase):
    def setUp(self):
        self.sup = Supervisor("sup@uwm.edu", "sup_pass")
        # fake fields
        self.adm = ("adm@uwm.edu", "amd_pass")
        self.ins = ("ins@uwm.edu", "ins_pass")
        self.tas = ("tas@uwm.edu", "tas_pass")

    def test_assign_instructor_course(self):


    def test_assign_ta_course(self):


    def test_assign_ta_lab(self):

