# created by Grant

from unittest import TestCase
from classes.Person import Person


class TestPerson(TestCase):
    def test_init_(self):
        self.person1 = Person("DEFAULT_EMAIL", "DEFAULT_PASSWORD")
        self.assertEquals(self.person1.email, "DEFAULT_EMAIL")
        self.assertEquals(self.person1.password, "DEFAULT_PASSWORD")
        self.assertEquals(self.person1.name, "DEFAULT")
        self.assertEquals(self.person1.phone_number, "0000000000")

    def test_change_password(self):
        self.person1.change_password("DEFAULT_PASSWORD", "password")
        self.assertEquals(self.person1.password, "password")

    def test_change_email(self):
        self.person1.change_email("snoop@uwm.edu")
        self.assertEquals(self.person1.email, "snoop@uwm.edu")

    def test_change_phone(self):
        self.person1.change_phone(4144244343)
        self.assertEquals(self.person1.phone_number, 4144244343)

    def test_change_name(self):
        self.person1.change_name("Snoop Doggy Dog")
        self.assertEquals(self.person1.name, "Snoop Doggy Dog")

    def test_get_contact_info(self):
        self.assertEquals(self.test_get_contact_info(), "Snoop Doggy Dog, snoop@uwm.edu, 4144244343")

    def test_login(self):
        self.assertEquals(self.person1.login("snoop@uwm.edu", "password"), "Login successful.")

    def test_logout(self):
        self.assertTrue(self.person1.logout())
