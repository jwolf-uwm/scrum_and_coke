# created by Jeff

from classes.Instructor import Instructor
from unittest import TestCase


class TestInstructor(TestCase):

    def test___init__(self):
        self.instructor1 = Instructor("DEFAULT_EMAIL", "DEFAULT_PASSWORD")
        self.assertEquals(self.instructor1.email, "DEFAULT_EMAIL")
        self.assertEquals(self.instructor1.username, "DEFAULT_USERNAME")
        self.assertEquals(self.instructor1.password, "DEFAULT_PASSWORD")
        self.assertEquals(self.instructor1.name, "DEFAULT")
        self.assertEquals(self.instructor1.phone_number, "DEFAULT")

