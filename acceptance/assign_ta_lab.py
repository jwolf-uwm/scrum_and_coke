self.TA1 = TA("TA1@uwm.edu", "TA1")
        self.Course1 = Course("Intro to Computer Stuff", "CS101")
        self.Course1.section = 801
        self.assertEqual(self.ui.command("assign_ta_course TA1@uwm.edu CS101"), "TA1@uwm.edu was assigned to CS101")

        # best case
        self.assertEqual(self.ui.command("assign_ta_lab TA1@uwm.edu 801"), "TA1@uwm.edu was assigned to lab 801")

        # entered arguments that don't exist
        self.assertEqual(self.ui.command("assign_ta_lab TA1, 801"), "Error: invalid email address")
        self.assertEqual(self.ui.command("assign_ta_lab TA2@uwm.edu, 801"), "TA2@uwm.edu could not be assigned since "
                                                                            "it does not exist")
        self.assertEqual(self.ui.command("assign_ta_lab TA1@uwm.edu, 802"), "802 could not be assigned since "
                                                                            "it does not exist")


        # test number of arguments
        self.assertEqual(self.ui.command("assign_ta_lab TA@uwm.edu"), "Error: too few arguments")
        self.assertEqual(self.ui.command("assign_ta_lab"), "Error: too few arguments")

        # test if lab section already has a TA
        self.TA2 = TA("TA2@uwm.edu", "TA2")
        self.assertEqual(self.ui.command("assign_ta_lab TA2@uwm.edu 801"), "Lab 801 already has been assigned a TA")

        # test against non-TAs
        self.SUP = Supervisor("SUP@uwm.edu", "SUP")
        self.ADMIN = Administrator("ADMN@uwm.edu", "ADMIN")
        self.INS = Instructor("INS@uwm.edu", "INS")
        self.assertEqual(self.ui.command("assign_ta_lab INS@uwm.edu 801"), "Error: INS@uwm.edu is not a TA")
        self.assertEqual(self.ui.command("assign_ta_lab SUP@uwm.edu 801"), "Error: SUP@uwm.edu is not a TA")
        self.assertEqual(self.ui.command("assign_ta_lab ADMIN@uwm.edu 801"), "Error: ADMIN@uwm.edu is not a TA")
