# created by Jeff

from classes.Instructor import Instructor
from classes.TA import TA
from classes.Course import Course
from unittest import TestCase


class TestInstructor(TestCase):

    def test___init__(self):
        self.instructor1 = Instructor("DEFAULT_EMAIL", "DEFAULT_PASSWORD")
        self.assertEquals(self.instructor1.email, "DEFAULT_EMAIL")
        self.assertEquals(self.instructor1.password, "DEFAULT_PASSWORD")
        self.assertEquals(self.instructor1.name, "DEFAULT")
        self.assertEquals(self.instructor1.phone_number, "DEFAULT")

    def test_login(self):
        # still using instructor1
        self.assertEquals(self.instructor1.login("DEFAULT_EMAIL", "DEFAULT_PASSWORD"),
                          "Logged in successfully")

    def test_logout(self):
        # still using instructor1
        self.assertEquals(self.instructor1.logout(), "Logged out.")

    def test_edit_contact(self):
        # still using instructor1
        self.instructor1.edit_contact_info("name", "Bob Ross")
        self.assertEquals(self.instructor1.name, "Bob Ross")

        self.instructor1.edit_contact_info("phone", "1-900-MIXALOT")
        self.assertEquals(self.instructor1.phone_number, "1-900-MIXALOT")

        self.instructor1.edit_contact_info("email", "bob_ross@not_real.arf")
        self.assertEquals(self.instructor1.email, "bob_ross@not_real.arf")


