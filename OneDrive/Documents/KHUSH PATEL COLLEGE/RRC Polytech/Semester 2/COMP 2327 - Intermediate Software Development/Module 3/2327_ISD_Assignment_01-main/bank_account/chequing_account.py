from patterns.strategy.overdraft_strategy import OverdraftStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """
    A class representing a Chequing Account with overdraft support,
    utilizing the Strategy Pattern to calculate service charges.

    Attributes:
        overdraft_limit (float): Maximum amount allowed for overdraft.
        overdraft_rate (float): Rate applied to overdrafted amount.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the ChequingAccount with overdraft settings.

        Args:
            account_number (int): Unique identifier for the account.
            client_number (int): Client's ID number.
            balance (float): Initial balance of the account.
            date_created (date): The creation date of the account.
            overdraft_limit (float): Allowed overdraft limit.
            overdraft_rate (float): Interest rate on overdrafted amount.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

    def get_service_charges(self) -> float:
        """Calculate and return service charges using OverdraftStrategy."""
        return self._strategy.calculate_service_charges(self)
