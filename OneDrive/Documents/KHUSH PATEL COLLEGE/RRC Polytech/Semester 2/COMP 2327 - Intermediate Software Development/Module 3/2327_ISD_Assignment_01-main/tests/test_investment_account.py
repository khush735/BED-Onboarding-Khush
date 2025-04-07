import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    def test_service_charge_new_account(self):
        recent_date = date.today()
        account = InvestmentAccount(301, 3, 1000.0, recent_date, 15.0)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_service_charge_old_account(self):
        old_date = date.today() - timedelta(days=365.25 * 11)
        account = InvestmentAccount(302, 3, 1000.0, old_date, 15.0)
        self.assertEqual(account.get_service_charges(), 15.0)

if __name__ == "__main__":
    unittest.main()
