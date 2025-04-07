import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    def test_service_charge_no_overdraft(self):
        account = ChequingAccount(101, 1, 100.0, date.today(), 500.0, 0.1)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_service_charge_with_overdraft(self):
        account = ChequingAccount(102, 1, -200.0, date.today(), 500.0, 0.1)
        self.assertAlmostEqual(account.get_service_charges(), 20.0)

if __name__ == "__main__":
    unittest.main()
