from .service_charge_strategy import ServiceChargeStrategy
from bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float):
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for a given bank account based on its balance.

        Args:
            account (BankAccount): The bank account for which to calculate service charges.

        Returns:
            float: The service charge amount. If the account balance is below the minimum balance,
                   a premium service charge is applied. Otherwise, the base service charge is applied.
        """
        if account.balance < self._minimum_balance:
            return self.SERVICE_CHARGE_PREMIUM
        return self.BASE_SERVICE_CHARGE