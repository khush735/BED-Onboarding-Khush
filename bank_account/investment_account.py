from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float):
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = ManagementFeeStrategy(date_created, management_fee)

    def get_service_charges(self) -> float:
        return self._strategy.calculate_service_charges(self)