import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def test_do_quit(self):
        with self.assertRaises(SystemExit) as cm:
            self.hbnb_cmd.onecmd("quit")
        self.assertEqual(cm.exception.code, True)

    def test_do_EOF(self):
        with self.assertRaises(SystemExit) as cm:
            self.hbnb_cmd.onecmd("EOF")
        self.assertEqual(cm.exception.code, True)

    def test_do_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_do_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("show BaseModel 1234-5678")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_do_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("destroy BaseModel 1234-5678")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_do_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_do_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_do_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("update BaseModel 1234-5678 {'name': 'test'}")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_do_help(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("help")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_invalid_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_cmd.onecmd("invalid_command")
            output = mock_stdout.getvalue().strip()
            self.assertTrue("** Unrecognized command" in output)


if __name__ == '__main__':
    unittest.main()
