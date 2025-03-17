from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class InvestmentAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float):
        """
        Initializes an InvestmentAccount instance.

        Args:
            account_number (int): The account number of the investment account.
            client_number (int): The client number associated with the account.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            management_fee (float): The management fee associated with the account.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = ManagementFeeStrategy(date_created, management_fee)

    def get_service_charges(self) -> float:
        return self._strategy.calculate_service_charges(self)