from patterns.strategy.overdraft_strategy import OverdraftStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """
    A class used to represent a Chequing Account, which is a type of Bank Account.
    Attributes
    ----------
    account_number : int
        The account number of the chequing account.
    client_number : int
        The client number associated with the chequing account.
    balance : float
        The current balance of the chequing account.
    date_created : date
        The date when the chequing account was created.
    overdraft_limit : float
        The overdraft limit for the chequing account.
    overdraft_rate : float
        The overdraft rate for the chequing account.
    Methods
    -------
    get_service_charges() -> float
        Calculates and returns the service charges for the chequing account.
    """
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit: float, overdraft_rate: float):
        super().__init__(account_number, client_number, balance, date_created)
        self._strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

    def get_service_charges(self) -> float:
        return self._strategy.calculate_service_charges(self)