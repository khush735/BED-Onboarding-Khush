from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        """
        Initializes a SavingsAccount instance.

        Args:
            account_number (int): The account number of the savings account.
            client_number (int): The client number associated with the account.
            balance (float): The current balance of the account.
            date_created (date): The date the account was created.
            minimum_balance (float): The minimum balance required for the account.

        """
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = MinimumBalanceStrategy(minimum_balance)

    def get_service_charges(self) -> float:
        return self._strategy.calculate_service_charges(self)