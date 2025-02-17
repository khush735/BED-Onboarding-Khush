import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    def setUp(self):
        """Set up an InvestmentAccount instance for testing."""
        self.account = InvestmentAccount(123456, 7890, 10000.0, date(2020, 1, 1), 1.99)

    def test_init_valid_inputs(self):
        """Test that attributes are set correctly with valid inputs."""
        self.assertEqual(self.account.account_number, 123456)
        self.assertEqual(self.account.client_number, 7890)
        self.assertEqual(self.account.balance, 10000.0)
        self.assertEqual(self.account.date_opened, date(2020, 1, 1))
        self.assertEqual(self.account._management_fee, 1.99)

    def test_init_invalid_management_fee(self):
        """Test that management_fee defaults to 2.55 if invalid."""
        account = InvestmentAccount(123456, 7890, 10000.0, date(2020, 1, 1), "invalid")
        self.assertEqual(account._management_fee, 2.55)

    def test_get_service_charges_old_account(self):
        """Test service charges when date_opened is more than 10 years ago."""
        old_date = date.today() - timedelta(days=10 * 365.25 + 1)  # More than 10 years ago
        account = InvestmentAccount(123456, 7890, 10000.0, old_date, 1.99)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_get_service_charges_exactly_10_years_ago(self):
        """Test service charges when date_opened is exactly 10 years ago."""
        ten_years_ago = date.today() - timedelta(days=10 * 365.25)
        account = InvestmentAccount(123456, 7890, 10000.0, ten_years_ago, 1.99)
        self.assertEqual(account.get_service_charges(), 0.50 + 1.99)

    def test_get_service_charges_recent_account(self):
        """Test service charges when date_opened is within the last 10 years."""
        self.assertEqual(self.account.get_service_charges(), 0.50 + 1.99)

    def test_str_representation_old_account(self):
        """Test string representation when date_opened is more than 10 years ago."""
        old_date = date.today() - timedelta(days=10 * 365.25 + 1)  # More than 10 years ago
        account = InvestmentAccount(123456, 7890, 10000.0, old_date, 1.99)
        expected_output = (
            "Account No: 123456, Balance: $10000.00\n"
            "Date Opened: {old_date}, Management Fee: Waived"
        )
        self.assertEqual(str(account), expected_output.format(old_date=old_date))

    def test_str_representation_recent_account(self):
        """Test string representation when date_opened is within the last 10 years."""
        expected_output = (
            "Account No: 123456, Balance: $10000.00\n"
            "Date Opened: 2020-01-01, Management Fee: $1.99"
        )
        self.assertEqual(str(self.account), expected_output)

if __name__ == "__main__":
    unittest.main()