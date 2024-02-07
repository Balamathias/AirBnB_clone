import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            self.assertFalse(self.console.onecmd("create UnknownClass"))
            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(self.console.onecmd("create User"))

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            self.assertFalse(self.console.onecmd("show UnknownClass"))
            self.assertFalse(self.console.onecmd("show BaseModel"))
            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(self.console.onecmd("show BaseModel"))

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertFalse(self.console.onecmd("destroy UnknownClass"))
            self.assertFalse(self.console.onecmd("destroy BaseModel"))
            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(self.console.onecmd("destroy BaseModel"))

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all"))
            self.assertFalse(self.console.onecmd("all UnknownClass"))
            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(self.console.onecmd("all"))

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("count"))
            self.assertFalse(self.console.onecmd("count UnknownClass"))
            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(self.console.onecmd("count BaseModel"))

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            self.assertFalse(self.console.onecmd("update UnknownClass"))
            self.assertFalse(self.console.onecmd("update BaseModel"))
            self.assertFalse(self.console.onecmd("update BaseModel 123"))
            self.assertFalse(self.console.onecmd("update BaseModel 123 attr_name"))
            self.assertFalse(self.console.onecmd("update BaseModel 123 attr_name value"))
            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(self.console.onecmd("update BaseModel 123 email 'new_email@example.com'"))

    def test_update_dict(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update_dict"))
            self.assertFalse(self.console.onecmd("update_dict UnknownClass"))
            self.assertFalse(self.console.onecmd("update_dict BaseModel"))
            self.assertFalse(self.console.onecmd("update_dict BaseModel 123"))
            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(self.console.onecmd("update_dict BaseModel 123 {'email': 'new_email@example.com', 'name': 'John'}"))

    def test_all_with_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all UnknownClass"))
            self.assertTrue(self.console.onecmd("create BaseModel"))
            self.assertTrue(self.console.onecmd("all BaseModel"))

    # Add more tests for other commands

if __name__ == '__main__':
    unittest.main()
