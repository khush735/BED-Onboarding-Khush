from datetime import date
from bank_account.bank_account import BankAccount


class SavingsAccount(BankAccount):
    """
    A subclass of BankAccount representing a savings account with a minimum balance requirement.
    """

    SERVICE_CHARGE_PREMIUM = 2.0  # Premium applied when balance is below minimum

    def __init__(self, account_number: int, client_number: int, balance: float, date_opened: date, minimum_balance: float):
        """
        Initializes a SavingsAccount with a minimum balance requirement.

        Args:
            minimum_balance (float): The minimum balance required to avoid additional charges.
        """
        super().__init__(account_number, client_number, balance, date_opened)
        self._minimum_balance = float(minimum_balance) if isinstance(minimum_balance, (int, float)) else 50.0

    def get_service_charges(self) -> float:
        """
        Calculates service charges based on the account's balance and minimum balance requirement.

        Returns:
            float: The calculated service charges.
        """
        if self._balance >= self._minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    def __str__(self) -> str:
        """
        Returns a string representation of the SavingsAccount.

        Returns:
            str: A string showing account details, including minimum balance.
        """
        return (f"Account No: {self._account_number}, Balance: ${self._balance:.2f}\n"
                f"Minimum Balance: ${self._minimum_balance:.2f}")