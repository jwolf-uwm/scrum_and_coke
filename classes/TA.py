# created by Dillan

from classes.Person import Person


class TA(Person):

    def __init__(self, email, password):
        super().__init__(email, password)
        self.courses = []
        self.section = []

    def view_ta_assignments(self):
        return

    def read_public_contact(self):
        return

    def edit_contact_info(self):
        return
