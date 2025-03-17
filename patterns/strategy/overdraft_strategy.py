from .service_charge_strategy import ServiceChargeStrategy
from bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        if account.balance < 0:
            return abs(account.balance) * self._overdraft_rate
        return self.BASE_SERVICE_CHARGE