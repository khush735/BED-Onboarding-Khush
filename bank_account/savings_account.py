from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float):
        """
        Initializes a SavingsAccount instance.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = MinimumBalanceStrategy(minimum_balance)

    def get_service_charges(self) -> float:
        return self._strategy.calculate_service_charges(self)

    @property
    def minimum_balance(self) -> float:
        """
        Returns the minimum balance required for this account.
        """
        return self._strategy._minimum_balance
