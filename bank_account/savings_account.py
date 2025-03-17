from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = MinimumBalanceStrategy(minimum_balance)

    def get_service_charges(self) -> float:
        return self._strategy.calculate_service_charges(self)