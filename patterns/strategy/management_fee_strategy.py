from datetime import date, timedelta
from .service_charge_strategy import ServiceChargeStrategy
from bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        self._date_created = date_created
        self._management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges for a given bank account.

        This method calculates the service charges based on the account's creation date.
        If the account was created more than ten years ago, it returns the management fee.
        Otherwise, it returns the base service charge.

        Args:
            account (BankAccount): The bank account for which to calculate the service charges.

        Returns:
            float: The calculated service charges.
        """
        if self._date_created < self.TEN_YEARS_AGO:
            return self._management_fee
        return self.BASE_SERVICE_CHARGE