from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    """
    A class representing a Savings Account, with service charges based
    on maintaining a minimum required balance.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float):
        """
        Initializes the SavingsAccount with a minimum balance requirement.

        Args:
            account_number (int): Unique identifier for the account.
            client_number (int): Client's ID number.
            balance (float): Initial balance of the account.
            date_created (date): The creation date of the account.
            minimum_balance (float): Required minimum balance to avoid premium charges.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = MinimumBalanceStrategy(minimum_balance)

    def get_service_charges(self) -> float:
        """Calculate and return service charges using MinimumBalanceStrategy."""
        return self._strategy.calculate_service_charges(self)
