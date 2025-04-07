import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    def test_service_charge_above_min_balance(self):
        account = SavingsAccount(201, 2, 300.0, date.today(), 200.0)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_service_charge_below_min_balance(self):
        account = SavingsAccount(202, 2, 100.0, date.today(), 200.0)
        self.assertEqual(account.get_service_charges(), 2.0)

if __name__ == "__main__":
    unittest.main()
