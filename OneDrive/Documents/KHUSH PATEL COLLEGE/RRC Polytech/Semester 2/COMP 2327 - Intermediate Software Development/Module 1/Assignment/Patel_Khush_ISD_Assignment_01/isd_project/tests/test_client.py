"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""


import unittest
from client.client import Client
from email_validator import EmailNotValidError

class TestClient(unittest.TestCase):
    def test_valid_client(self):
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(client.client_number, 1010)
        self.assertEqual(client.first_name, "Susan")
        self.assertEqual(client.last_name, "Clark")
        self.assertEqual(client.email_address, "susanclark@pixell.com")

    def test_invalid_client_number(self):
        with self.assertRaises(ValueError):
            Client("1010", "Susan", "Clark", "susanclark@pixell.com")

    def test_blank_first_name(self):
        with self.assertRaises(ValueError):
            Client(1010, "  ", "Clark", "susanclark@pixell.com")

    def test_blank_last_name(self):
        with self.assertRaises(ValueError):
            Client(1010, "Susan", "  ", "susanclark@pixell.com")

    def test_invalid_email(self):
        client = Client(1010, "Susan", "Clark", "invalid-email")
        self.assertEqual(client.email_address, "email@pixell-river.com")

    def test_str_method(self):
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(str(client), "Clark, Susan [1010] - susanclark@pixell.com\n")

if __name__ == "__main__":
    unittest.main()
