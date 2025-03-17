"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""


import unittest
from bank_account.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    """
    Test suite for the BankAccount class to verify the correctness of its methods and functionality.
    """

    def test_valid_account_creation(self):
        """Tests if a BankAccount is correctly created with valid inputs."""
        account = BankAccount(12345, 6789, 1000.00)
        self.assertEqual(account.account_number, 12345)
        self.assertEqual(account.client_number, 6789)
        self.assertEqual(account.balance, 1000.00)

    def test_invalid_account_number_type(self):
        """Tests if a ValueError is raised when an invalid account number is provided."""
        with self.assertRaises(ValueError):
            BankAccount("12345", 6789, 1000.00)

    def test_invalid_client_number_type(self):
        """Tests if a ValueError is raised when an invalid client number is provided."""
        with self.assertRaises(ValueError):
            BankAccount(12345, "6789", 1000.00)

    def test_invalid_balance_input(self):
        """Tests if the balance is correctly set to 0.0 when an invalid balance is provided."""
        account = BankAccount(12345, 6789, "invalid_balance")
        self.assertEqual(account.balance, 0.0)

    def test_deposit_positive_amount(self):
        """Tests the deposit method with a valid positive amount."""
        account = BankAccount(98765, 4321, 500.00)
        account.deposit(200.00)
        self.assertEqual(account.balance, 700.00)

    def test_withdraw_valid_amount(self):
        """Tests the withdrawal method with a valid amount."""
        account = BankAccount(98765, 4321, 500.00)
        account.withdraw(150.00)
        self.assertEqual(account.balance, 350.00)

    def test_withdraw_exceeding_balance(self):
        """Tests if a ValueError is raised when trying to withdraw more than the available balance."""
        account = BankAccount(98765, 4321, 100.00)
        with self.assertRaises(ValueError):
            account.withdraw(200.00)

if __name__ == '__main__':
    unittest.main()
