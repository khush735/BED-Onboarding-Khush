from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    A subclass of BankAccount representing a chequing account with overdraft functionality.
    """

    def __init__(self, account_number: int, client_number: int, balance: float, date_opened: date, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes a ChequingAccount with an overdraft limit and rate.

        Args:
            overdraft_limit (float): The maximum amount the account can be overdrawn.
            overdraft_rate (float): The rate applied to overdraft amounts.
        """
        super().__init__(account_number, client_number, balance, date_opened)
        self._overdraft_limit = float(overdraft_limit) if isinstance(overdraft_limit, (int, float)) else -100.0
        self._overdraft_rate = float(overdraft_rate) if isinstance(overdraft_rate, (int, float)) else 0.05

    def get_service_charges(self) -> float:
        """
        Calculates service charges based on the account's balance and overdraft status.

        Returns:
            float: The calculated service charges.
        """
        if self._balance >= self._overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + (self._overdraft_limit - self._balance) * self._overdraft_rate

    def __str__(self) -> str:
        """
        Returns a string representation of the ChequingAccount.

        Returns:
            str: A string showing account details, including overdraft limit and rate.
        """
        return (f"Account No: {self._account_number}, Balance: ${self._balance:.2f}\n"
                f"Overdraft Limit: ${self._overdraft_limit:.2f}, Overdraft Rate: {self._overdraft_rate * 100:.2f}%")