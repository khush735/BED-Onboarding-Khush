# bank_account/chequing_account.py

from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit: float, overdraft_rate: float):
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

    def get_service_charges(self) -> float:
        return self._strategy.calculate_service_charges(self)