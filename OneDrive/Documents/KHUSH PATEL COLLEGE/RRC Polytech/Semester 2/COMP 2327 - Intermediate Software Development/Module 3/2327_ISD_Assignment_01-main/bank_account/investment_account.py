from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class InvestmentAccount(BankAccount):
    """
    A class representing an Investment Account, which applies a
    management fee based on the age of the account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """
        Initializes the InvestmentAccount.

        Args:
            account_number (int): Unique identifier for the account.
            client_number (int): Client's ID number.
            balance (float): Initial balance of the account.
            date_created (date): The date the account was opened.
            management_fee (float): The recurring management fee.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = ManagementFeeStrategy(date_created, management_fee)

    def get_service_charges(self) -> float:
        """Calculate and return service charges using ManagementFeeStrategy."""
        return self._strategy.calculate_service_charges(self)
