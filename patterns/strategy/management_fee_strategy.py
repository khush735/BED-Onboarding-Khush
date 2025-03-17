from datetime import date, timedelta
from .service_charge_strategy import ServiceChargeStrategy
from bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        self._date_created = date_created
        self._management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        if self._date_created < self.TEN_YEARS_AGO:
            return self._management_fee
        return self.BASE_SERVICE_CHARGE