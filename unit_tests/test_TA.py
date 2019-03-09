# created by Dillan

from unittest import TestCase
from classes.TA import TA


class TestTA(TestCase):

    def setup(self):
        self.ta1 = TA("DEFAULT_EMAIL@uwm.edu", "DEFAULT_PASSWORD")
        self.instructor1 = ("DEFAULT_EMAIL@uwm.edu", "DEFAULT_PASSWORD")
        self.instructor2 = ("DEFAULT_EMAIL@uwm.edu", "DEFAULT_PASSWORD")
        self.instructor3 = ("DEFAULT_EMAIL@uwm.edu", "DEFAULT_PASSWORD")
        self.course1 = ("DEFAULT_ID", 101, self.instructor1, [])
        self.course_catalog = (("DEFAULT_ID1", 101, self.instructor1, [self.ta1]),
                              ("DEFAULT_ID2", 101, self.instructor1, []),
                              ("DEFAULT_ID3", 101, self.instructor1, [self.ta1]),
                              ("DEFAULT_ID4", 101, self.instructor1, []))
        self.class_list = (self.instructor1, self.instructor2, self.instructor3, self.ta1)

    def test_view_ta_assignments(self):
        self.assertEqual(self.ta1.view_ta_assignment(self.course_catalog), ["DEFAULT_ID1", "DEFAULT_ID3"])

    def test_read_public_contact(self):
        self.assertEqual(self.ta1.read_public_contact(self.class_list))

    def test_edit_contact_info(self):
        # still using instructor1
        self.ta1.edit_contact_info("name", "Bob Ross")
        self.assertNotEquals(self.ta1.name, "DEFAULT")
        self.assertEquals(self.ta1.name, "Bob Ross")

        self.ta1.edit_contact_info("phone", "4145459999")
        self.assertNotEquals(self.ta1.phone_number, "0000000000")
        self.assertEquals(self.ta1.phone_number, "4145459999")

        self.ta1.edit_contact_info("email", "bob_ross@uwm.edu")
        self.assertNotEquals(self.ta1.email, "instructor1@uwm.edu")
        self.assertEquals(self.ta1.email, "bob_ross@uwm.edu")

        with self.assertRaises(TypeError):
            self.ta1.edit_contact_info(2, "Ted")

        with self.assertRaises(TypeError):
            self.ta1.edit_contact_info("name", 41.6)
