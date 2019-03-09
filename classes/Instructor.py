# created by Jeff

from classes import Person


class InstructorClass(Person):

    def __init__(self, email, username, password):
        super().__init__(email, username, password)
        self.courses = []

    def assign_ta_course(self, email, course_id, course_section):
        return

    def assign_ta_lab(self, email, lab_section):
        return

    def view_course_assign(self):
        return

    def read_public_contact(self):
        return

    def view_ta_assign(self):
        return

    def edit_contact_info(self):
        return
