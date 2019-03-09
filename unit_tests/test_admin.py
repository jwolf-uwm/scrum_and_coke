# created by Matt

from classes.Administrator import Administrator
from unittest import TestCase


class TestAdministrator(TestCase):
    def test_create_course(self):
        self.ad1 = Administrator("ad1@uwm.edu", "ad1pas")
        self.ad2 = Administrator("ad22@uwm.edu", "ad2pass")

        self.assertTrue(self, self.ad1.createAccount("people", "pass", "thatguy@uwm.edu"))
        self.assertTrue(self, self.ad1.createAccount("people1", "pass2", "thatguy2@uwm.edu"))
        self.assertFalse(self, self.ad1.createAccount("people", "pass", "thatguy@uwm.edu"))

    def test_create_account(self):
        self.ad1 = Administrator("admin", "testpass", "blah@uwm.edu")
        self.ad2 = Administrator("admin2", "testpass2", "blah2@uwm.edu")

        self.assertTrue(self, self.ad1.createCourse("CS337"))
        self.assertTrue(self, self.ad2.createCourse("CS315"))
        self.assertFalse(self, self.ad1.createCourse("CS337"))

    def test_edit_account(self):
        self.ad1 = Administrator("admin", "testpass", "blah@uwm.edu")
        self.ad2 = Administrator("admin2", "testpass2", "blah2@uwm.edu")

    def test_delete_account(self):
        self.fail()

    def test_send_notification(self):
        self.fail()

    def test_access_info(self):
        self.fail()
