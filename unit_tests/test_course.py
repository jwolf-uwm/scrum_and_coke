from unittest import TestCase
from classes.Course import Course


class TestCourse(TestCase):

    def setup(self):
        course1 = Course("CS251", ["401", "402"])
        self.instructor1 = ("DEFAULT_EMAIL@uwm.edu", "DEFAULT_PASSWORD")
        self.instructor2 = ("DEFAULT_EMAIL@uwm.edu", "DEFAULT_PASSWORD")
        self.ta1 = ("DEFAULT_EMAIL@uwm.edu", "DEFAULT_PASSWORD")

    def test__init__(self):
        self.assertEquals(self.course1.course_id, "CS251")
        self.assertEquals(self.course1.lab_sections, ["401", "402"])
        self.assertEquals(self.course1.instructor, "Dr. Default")
        self.assertEquals(self.course1.tee_ays, [])

    def test_set_course_id(self):
        self.assertEqual(self.course1.course_id, "CS251")
        self.course1.set_course_id("CS250")
        self.assertEqual(self.course1.course_id, "CS250")
        self.assertNotEquals(self.course1.course_id, "CS251")

    def test_set_course_section(self):
        self.assertEqual(self.course1.course_section, ["401", "402"])
        self.course1.set_course_section(["502"])
        self.assertEqual(self.course1.course_section, ["502"])
        self.assertNotEquals(self.course1.course_id, ["401", "402"])

    def test_set_instructor(self):
        self.assertEqual(self.course1.instructor, self.instructor1)
        self.course1.set_instructor(self.instructor2)
        self.assertEqual(self.course1.instructor, self.instructor2)
        self.assertNotEquals(self.course1.instructor, self.instructor1)

    def test_add_lab_section(self):
        self.fail()

    def test_add_tee_ay(self):
        self.fail()

    def test_get_course_id(self):
        self.fail()

    def test_get_course_name(self):
        self.fail()

    def test_get_course_section(self):
        self.fail()

    def test_get_lab_sections(self):
        self.fail()

    def test_get_tee_ays(self):
        self.fail()
