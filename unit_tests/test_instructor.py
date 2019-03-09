# created by Jeff

from classes.Instructor import Instructor
from classes.TA import TA
from classes.Course import Course
from unittest import TestCase


class TestInstructor(TestCase):

    def setup(self):
        self.instructor1 = Instructor("DEFAULT_EMAIL", "DEFAULT_PASSWORD")
        self.ta1 = TA("DEFAULT_TA1_EMAIL", "DEFAULT_PASSWORD")
        self.course1 = Course("DEFAULT_ID", 101)

    def test___init__(self):
        self.assertEquals(self.instructor1.email, "DEFAULT_EMAIL")
        self.assertEquals(self.instructor1.password, "DEFAULT_PASSWORD")
        self.assertEquals(self.instructor1.name, "DEFAULT")
        self.assertEquals(self.instructor1.phone_number, "DEFAULT")

    def test_edit_contact(self):
        # still using instructor1
        self.instructor1.edit_contact_info("name", "Bob Ross")
        self.assertEquals(self.instructor1.name, "Bob Ross")

        self.instructor1.edit_contact_info("phone", "1-900-MIXALOT")
        self.assertEquals(self.instructor1.phone_number, "1-900-MIXALOT")

        self.instructor1.edit_contact_info("email", "bob_ross@not_real.arf")
        self.assertEquals(self.instructor1.email, "bob_ross@not_real.arf")

        with self.assertRaises(TypeError):
            self.instructor1.edit_contact_info(2, "Ted")

        with self.assertRaises(TypeError):
            self.instructor1.edit_contact_info("name", 41.6)

    def test_read_public_contact(self):
        self.assertEquals(self.instructor1.read_public_contact(), "Bob Ross, bob_ross@not_real.arf")

    def test_send_notification_ta(self):
        self.assertTrue(self.instructor1.send_notification_ta("DEFAULT_TA_EMAIL", "Hi!"))
        self.assertFalse(self.instructor1.send_notification_ta("ROAR", "Woof!"))

    def test_view_course(self):
        self.assertEquals(self.instructor1.view_course_assign(), "No courses assigned.")
        self.instructor1.courses.append(self.course1)
        self.assertEquals(self.instructor1.view_course_assign(), "DEFAULT_ID - 101")

    def test_view_ta_assign(self):
        self.assertEquals(self.instructor1.view_ta_assign()[0], self.ta1)
