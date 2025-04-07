from .service_charge_strategy import ServiceChargeStrategy
from bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float):
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        if account.balance < self._minimum_balance:
            return self.SERVICE_CHARGE_PREMIUM
        return self.BASE_SERVICE_CHARGE
