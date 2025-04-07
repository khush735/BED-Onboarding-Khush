from patterns.strategy.overdraft_strategy import OverdraftStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """
    A class used to represent a Chequing Account, which is a type of Bank Account.
    """
    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

    def get_service_charges(self) -> float:
        return self._strategy.calculate_service_charges(self)

    @property
    def overdraft_limit(self) -> float:
        """
        Returns the overdraft limit.
        """
        return self._strategy._overdraft_limit

    @property
    def overdraft_rate(self) -> float:
        """
        Returns the overdraft rate.
        """
        return self._strategy._overdraft_rate
