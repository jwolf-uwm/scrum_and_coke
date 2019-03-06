# made by Matt

import unittest


class EmailTests(unittest.TestCase):
    def setup(self):
        self.ui.command("create_user Admin AdminPassword")
        self.ui.command("create_user TA TAPassword")
        self.ui.command("create_user Student StuPassword")
        self.ui.command("create_user Supervisor SupPassword")
        self.ui.command("send_notification Message")

    """
        When the send notification command, it takes one parameter
        -the message to be sent
        if the message is sent successfully via email, send notification is a success
        -"Message sent successfully"
        If message is not sent, send notification failed
        -"Message not sent"
        if access is denied
        -"access denied"
    """
    def test_admin_user(self):
        self.ui.command(self.ui.command("login_Supervisor Sup SupPassword"), "login successful")
        self.ui.command(self.ui.command("send_notification Message"), "Access Denied")
        self.ui.command(self.ui.command("login_TA TA TAPassword"), "login successful")
        self.ui.command(self.ui.command("send_notification Message"), "Access Denied")
        self.ui.command(self.ui.command("login_Student Stu StuPassword"), "login successful")
        self.ui.command(self.ui.command("send_notification Message"), "Access Denied")

    def test_email_connected(self):
        self.assertEqual(self.ui.command("email Person"), "email not in system")
        self.assertEqual(self.ui.command("send_notification Message"), "Email not connected")

    def test_send_notification_correct(self):
        self.ui.command(self.ui.command("login_Admin Admin AdminPassword"), "login successful")
        self.assertEqual(self.ui.command("send_notification Message"), "Message sent successfully")

    def test_send_notification_fail(self):
        self.ui.command(self.ui.command("login_Admin Admin AdminPassword"), "login successful")
        self.assertEqual(self.ui.command("send_notification Message"), "Message not sent")

    def test_send_notification_no_message(self):
        self.assertEqual(self.ui.command("send_notification "), "No message to send")
