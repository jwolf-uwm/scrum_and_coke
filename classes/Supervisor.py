# created by Evan

from classes import Person


class Supervisor(Person):
    def __init__(self, email, username, password):
        super().__init__(email, username, password)

    def assign_instructor_course(self, instructor, course):
        """
        assigns the given instructor's course to the course parameter
        """
        return

    def assign_ta_course(self, ta, course):
        """
        assigns the given TA's course to the course parameter
        """
        return

    def assign_ta_lab(self, ta, lab):
        """
        assigns the given TA's lab
        """
        return

