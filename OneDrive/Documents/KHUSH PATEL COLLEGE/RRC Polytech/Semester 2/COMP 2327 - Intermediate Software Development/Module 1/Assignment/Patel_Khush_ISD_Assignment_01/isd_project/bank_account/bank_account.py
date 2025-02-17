from datetime import date

class BankAccount:
    """
    A class to represent a bank account with basic operations such as deposits, withdrawals, and balance management.

    Attributes:
        account_number (int): A unique identifier for the bank account.
        client_number (int): A unique identifier for the account holder.
        balance (float): The current balance in the account.
        date_opened (date): The date the account was opened.
    """

    BASE_SERVICE_CHARGE = 0.50  # Base service charge for all accounts

    def __init__(self, account_number: int, client_number: int, balance: float, date_opened: date):
        """
        Initializes the bank account with an account number, client number, balance, and date opened.

        Args:
            account_number (int): The number associated with the account.
            client_number (int): The ID associated with the account holder.
            balance (float): The initial balance to start the account with.
            date_opened (date): The date the account was opened.

        Raises:
            ValueError: If account number or client number is not an integer, or if balance is not a valid float.
        """
        if not isinstance(account_number, int):
            raise ValueError("The account number must be an integer.")
        self._account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("The client number must be an integer.")
        self._client_number = client_number

        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0

        if not isinstance(date_opened, date):
            self._date_opened = date.today()  # Default to today's date if invalid
        else:
            self._date_opened = date_opened

    @property
    def account_number(self) -> int:
        """Returns the account's unique identifier."""
        return self._account_number

    @property
    def client_number(self) -> int:
        """Returns the client's unique identifier."""
        return self._client_number

    @property
    def balance(self) -> float:
        """Returns the current balance of the account."""
        return self._balance

    @property
    def date_opened(self) -> date:
        """Returns the date the account was opened."""
        return self._date_opened

    def update_balance(self, amount: float):
        """
        Updates the account balance by a specified amount.

        Args:
            amount (float): The amount to add (or subtract if negative) from the balance.
        """
        try:
            amount = float(amount)
            self._balance += amount
        except ValueError:
            pass  # Ignore invalid amount if it's not a number

    def deposit(self, amount: float):
        """
        Deposits a positive amount into the account.

        Args:
            amount (float): The deposit amount to add to the balance.

        Raises:
            ValueError: If the amount is not a valid number or is non-positive.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("The deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.update_balance(amount)

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount from the account, provided there are sufficient funds.

        Args:
            amount (float): The withdrawal amount to subtract from the balance.

        Raises:
            ValueError: If the withdrawal amount exceeds the balance or is invalid.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("The withdrawal amount must be numeric.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds for the requested withdrawal.")
        self.update_balance(-amount)

    def get_service_charges(self) -> float:
        """
        Returns the base service charge for the account.

        Returns:
            float: The base service charge.
        """
        return self.BASE_SERVICE_CHARGE

    def __str__(self) -> str:
        """
        Returns a string representation of the account's number and its current balance.

        Returns:
            str: A string showing the account number and the balance formatted to two decimal places.
        """
        return f"Account No: {self._account_number}, Balance: ${self._balance:.2f}"