#!/usr/bin/python3
"""Test for console"""

import unittest
import pep8
import console
import tests
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Tests for the console"""

    @classmethod
    def setUpClass(self):
        """Setup for the test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Remove tests"""
        pass

    def test_pep8_console(self):
        """Check pep8 style console.py"""
        style = pep8.StyleGuide(quiet=True)
        val_style = style.check_files(["console.py"])
        self.assertEqual(val_style.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        """Checks docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
