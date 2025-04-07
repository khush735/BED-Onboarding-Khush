from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class InvestmentAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """
        Initializes an InvestmentAccount instance.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = ManagementFeeStrategy(date_created, management_fee)

    def get_service_charges(self) -> float:
        return self._strategy.calculate_service_charges(self)

    @property
    def management_fee(self) -> float:
        """
        Returns the management fee for this investment account.
        """
        return self._strategy._management_fee
