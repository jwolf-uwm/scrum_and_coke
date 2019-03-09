# created by Matt

from classes import Person


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

    def create_course(self, course_id, course_section):
        return

    def create_account(self, email, password):
        return

    def edit_account(self, email):
        return

    def delete_account(self, email):
        return

    def send_notification(self, notification):
        return

    def access_info(self):
        return
