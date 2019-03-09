# created by Matt

from classes.Administrator import Administrator
from unittest import TestCase


class TestAdministrator(TestCase):
    def setUp(self):
        self.ad1 = Administrator("ad1@uwm.edu", "ad1pass")

    def test_create_course(self):
        self.assertTrue(self.ad1.create_course("CS361", 401))
        self.course1 = ("CS337", 401)
        # course already exists
        self.assertFalse(self.ad1.create_course("CS337", 401))

    def test_create_account(self):
        self.assertTrue(self.ad1.create_account("DustyBottoms@uwm.edu", "better_password"))
        self.ad2 = Administrator("ad2@uwm.edu", "ad2pass")
        # taken email
        self.assertFalse(self.ad1.create_account("ad2@uwm.edu", "new_pass"))
        # taken password
        self.assertFalse(self.ad1.create_account("George_Likes_Beef@uwm.edu", "better_password"))

    def test_edit_account(self):
        self.random_user = ("rando@uwm.edu", "im_random")
        self.ad1.edit_account("random@uwm.edu", )

    def test_delete_account(self):

    def test_send_notification(self):
        self.assertTrue(self.ad1.send_notification("I Like To Eat French Fries In The Rain"))

    def test_access_info(self):
