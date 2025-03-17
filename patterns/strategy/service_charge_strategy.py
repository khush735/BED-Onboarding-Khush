from abc import ABC, abstractmethod
from bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for a given bank account.

        Args:
            account (BankAccount): The bank account for which to calculate the service charges.

        Returns:
            float: The calculated service charges for the account.
        """
        pass