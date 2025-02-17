import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    def setUp(self):
        """Set up a ChequingAccount instance for testing."""
        self.account = ChequingAccount(123456, 7890, 1000.0, date(2020, 1, 1), -100.0, 0.05)

    def test_init_valid_inputs(self):
        """Test that attributes are set correctly with valid inputs."""
        self.assertEqual(self.account.account_number, 123456)
        self.assertEqual(self.account.client_number, 7890)
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.date_opened, date(2020, 1, 1))
        self.assertEqual(self.account._overdraft_limit, -100.0)
        self.assertEqual(self.account._overdraft_rate, 0.05)

    def test_init_invalid_overdraft_limit(self):
        """Test that overdraft_limit defaults to -100.0 if invalid."""
        account = ChequingAccount(123456, 7890, 1000.0, date(2020, 1, 1), "invalid", 0.05)
        self.assertEqual(account._overdraft_limit, -100.0)

    def test_init_invalid_overdraft_rate(self):
        """Test that overdraft_rate defaults to 0.05 if invalid."""
        account = ChequingAccount(123456, 7890, 1000.0, date(2020, 1, 1), -100.0, "invalid")
        self.assertEqual(account._overdraft_rate, 0.05)

    def test_init_invalid_date_opened(self):
        """Test that date_opened defaults to today's date if invalid."""
        account = ChequingAccount(123456, 7890, 1000.0, "2020-01-01", -100.0, 0.05)
        self.assertEqual(account.date_opened, date.today())

    def test_get_service_charges_above_overdraft(self):
        """Test service charges when balance is above the overdraft limit."""
        self.assertEqual(self.account.get_service_charges(), 0.50)

    def test_get_service_charges_below_overdraft(self):
        """Test service charges when balance is below the overdraft limit."""
        self.account.update_balance(-1100.0)  # Balance = -100.0
        self.assertEqual(self.account.get_service_charges(), 0.50 + (-100.0 - (-100.0)) * 0.05)

    def test_get_service_charges_at_overdraft_limit(self):
        """Test service charges when balance is equal to the overdraft limit."""
        self.account.update_balance(-900.0)  # Balance = -100.0
        self.assertEqual(self.account.get_service_charges(), 0.50)

    def test_str_representation(self):
        """Test the string representation of the ChequingAccount."""
        expected_output = (
            "Account No: 123456, Balance: $1000.00\n"
            "Overdraft Limit: $-100.00, Overdraft Rate: 5.00%"
        )
        self.assertEqual(str(self.account), expected_output)

if __name__ == "__main__":
    unittest.main()