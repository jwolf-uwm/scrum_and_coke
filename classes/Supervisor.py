# created by Evan

from classes import Person


class Supervisor(Person):
    def __init__(self, email, password):
        super().__init__(email, password)

    def assign_instructor_course(self, email, course_id, section_id):
        """
        assigns the given instructor's course to the course parameter
        """
        return

    def assign_ta_course(self, email, course_id, course_section):
        """
        assigns the given TA's course to the course parameter
        """
        return

    def assign_ta_lab(self, email, lab_section):
        """
        assigns the given TA's lab
        """
        return

