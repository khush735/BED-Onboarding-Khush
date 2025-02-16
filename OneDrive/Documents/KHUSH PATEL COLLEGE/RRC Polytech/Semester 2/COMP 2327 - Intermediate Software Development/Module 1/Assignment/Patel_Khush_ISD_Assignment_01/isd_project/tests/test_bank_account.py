"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""


import unittest
from datetime import date
from bank_account.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    """
    Test suite for the BankAccount class to verify the correctness of its methods and functionality.
    """

    def setUp(self):
        """Set up a BankAccount instance for testing."""
        self.account = BankAccount(12345, 6789, 1000.00, date(2020, 1, 1))

    def test_valid_account_creation(self):
        """Tests if a BankAccount is correctly created with valid inputs."""
        self.assertEqual(self.account.account_number, 12345)
        self.assertEqual(self.account.client_number, 6789)
        self.assertEqual(self.account.balance, 1000.00)
        self.assertEqual(self.account.date_opened, date(2020, 1, 1))

    def test_invalid_account_number_type(self):
        """Tests if a ValueError is raised when an invalid account number is provided."""
        with self.assertRaises(ValueError):
            BankAccount("12345", 6789, 1000.00, date(2020, 1, 1))

    def test_invalid_client_number_type(self):
        """Tests if a ValueError is raised when an invalid client number is provided."""
        with self.assertRaises(ValueError):
            BankAccount(12345, "6789", 1000.00, date(2020, 1, 1))

    def test_invalid_balance_input(self):
        """Tests if the balance is correctly set to 0.0 when an invalid balance is provided."""
        account = BankAccount(12345, 6789, "invalid_balance", date(2020, 1, 1))
        self.assertEqual(account.balance, 0.0)

    def test_deposit_positive_amount(self):
        """Tests the deposit method with a valid positive amount."""
        self.account.deposit(200.00)
        self.assertEqual(self.account.balance, 1200.00)

    def test_withdraw_valid_amount(self):
        """Tests the withdrawal method with a valid amount."""
        self.account.withdraw(150.00)
        self.assertEqual(self.account.balance, 850.00)

    def test_withdraw_exceeding_balance(self):
        """Tests if a ValueError is raised when trying to withdraw more than the available balance."""
        with self.assertRaises(ValueError):
            self.account.withdraw(2000.00)

if __name__ == "__main__":
    unittest.main()