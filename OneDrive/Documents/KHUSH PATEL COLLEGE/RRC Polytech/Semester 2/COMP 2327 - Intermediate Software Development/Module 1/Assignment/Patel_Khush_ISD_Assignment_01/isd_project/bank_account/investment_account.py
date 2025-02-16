from datetime import date
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    A subclass of BankAccount representing an investment account with a management fee.
    """

    TEN_YEARS_AGO = date(date.today().year - 10, date.today().month, date.today().day)  # 10 years ago

    def __init__(self, account_number: int, client_number: int, balance: float, date_opened: date, management_fee: float):
        """
        Initializes an InvestmentAccount with a management fee.

        Args:
            management_fee (float): The fee charged for managing the account.
        """
        super().__init__(account_number, client_number, balance, date_opened)
        self._management_fee = float(management_fee) if isinstance(management_fee, (int, float)) else 2.55

    def get_service_charges(self) -> float:
        """
        Calculates service charges based on the account's age and management fee.

        Returns:
            float: The calculated service charges.
        """
        if self._date_opened <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self._management_fee

    def __str__(self) -> str:
        """
        Returns a string representation of the InvestmentAccount.

        Returns:
            str: A string showing account details, including management fee.
        """
        fee_status = "Waived" if self._date_opened <= self.TEN_YEARS_AGO else f"${self._management_fee:.2f}"
        return (f"Account No: {self._account_number}, Balance: ${self._balance:.2f}\n"
                f"Date Opened: {self._date_opened}, Management Fee: {fee_status}")