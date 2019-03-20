# created by Matt

from classes.Person import Person
from classes.Instructor import Instructor
from classes.TA import TA


class Administrator(Person):
    """
    an instance represents an administrator within the schools
    system
    must have username
    must have password
    must be able to create courses
    must be able to create accounts
    must be able to edit accounts
    must be able to delete account
    must be able to send notification
    must be able to access information
    """
    def __init__(self, email, password):
        self.password = password
        self.email = email

    def create_course(self, course_id, num_labs):
        return

    def create_account(self, email, password, account_type):

        parse_at_symbol = email.split("@")
        parse_period = parse_at_symbol[1].split(".")

        if parse_period[0] != "uwm":
            return "Email address must be a UWM address."

        if account_type == "instructor":
            new_instructor = Instructor(email, password)
            return new_instructor

        elif account_type == "ta":
            new_ta = TA(email, password)
            return new_ta

        return "Not a valid account type for creation."

    def edit_account(self, email, field, content):
        return

    def delete_account(self, email):
        return

    def send_notification(self, notification):
        return

    def access_info(self):
        return
