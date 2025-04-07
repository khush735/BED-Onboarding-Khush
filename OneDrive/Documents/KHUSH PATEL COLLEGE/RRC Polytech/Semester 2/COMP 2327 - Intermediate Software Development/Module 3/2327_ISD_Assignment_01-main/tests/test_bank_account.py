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

class DummyBankAccount(BankAccount):
    def get_service_charges(self) -> float:
        return 0.0

class BankAccountTests(unittest.TestCase):
    def test_valid_account_creation(self):
        account = DummyBankAccount(12345, 6789, 1000.00, date.today())
        self.assertEqual(account.account_number, 12345)
        self.assertEqual(account.client_number, 6789)
        self.assertEqual(account.balance, 1000.00)

    def test_invalid_account_number_type(self):
        with self.assertRaises(ValueError):
            DummyBankAccount("12345", 6789, 1000.00, date.today())

    def test_invalid_client_number_type(self):
        with self.assertRaises(ValueError):
            DummyBankAccount(12345, "6789", 1000.00, date.today())

    def test_invalid_balance_input(self):
        account = DummyBankAccount(12345, 6789, "invalid_balance", date.today())
        self.assertEqual(account.balance, 0.0)

    def test_deposit_positive_amount(self):
        account = DummyBankAccount(98765, 4321, 500.00, date.today())
        account.deposit(200.00)
        self.assertEqual(account.balance, 700.00)

    def test_withdraw_valid_amount(self):
        account = DummyBankAccount(98765, 4321, 500.00, date.today())
        account.withdraw(150.00)
        self.assertEqual(account.balance, 350.00)

    def test_withdraw_exceeding_balance(self):
        account = DummyBankAccount(98765, 4321, 100.00, date.today())
        with self.assertRaises(ValueError):
            account.withdraw(200.00)

if __name__ == '__main__':
    unittest.main()
