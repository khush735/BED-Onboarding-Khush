import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        """Set up a SavingsAccount instance for testing."""
        self.account = SavingsAccount(123456, 7890, 1000.0, date(2020, 1, 1), 500.0)

    def test_init_valid_inputs(self):
        """Test that attributes are set correctly with valid inputs."""
        self.assertEqual(self.account.account_number, 123456)
        self.assertEqual(self.account.client_number, 7890)
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.date_opened, date(2020, 1, 1))
        self.assertEqual(self.account._minimum_balance, 500.0)

    def test_init_invalid_minimum_balance(self):
        """Test that minimum_balance defaults to 50.0 if invalid."""
        account = SavingsAccount(123456, 7890, 1000.0, date(2020, 1, 1), "invalid")
        self.assertEqual(account._minimum_balance, 50.0)

    def test_get_service_charges_above_minimum(self):
        """Test service charges when balance is above the minimum balance."""
        self.assertEqual(self.account.get_service_charges(), 0.50)

    def test_get_service_charges_at_minimum(self):
        """Test service charges when balance is equal to the minimum balance."""
        self.account.update_balance(-500.0)  # Balance = 500.0
        self.assertEqual(self.account.get_service_charges(), 0.50)

    def test_get_service_charges_below_minimum(self):
        """Test service charges when balance is below the minimum balance."""
        self.account.update_balance(-600.0)  # Balance = 400.0
        self.assertEqual(self.account.get_service_charges(), 0.50 * 2.0)

    def test_str_representation(self):
        """Test the string representation of the SavingsAccount."""
        expected_output = (
            "Account No: 123456, Balance: $1000.00\n"
            "Minimum Balance: $500.00"
        )
        self.assertEqual(str(self.account), expected_output)

if __name__ == "__main__":
    unittest.main()