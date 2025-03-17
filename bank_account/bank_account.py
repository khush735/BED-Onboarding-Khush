from abc import ABC
from patterns.observer.subject import Subject
from datetime import date
print(date)
import os
print(os.getcwd())


class BankAccount(Subject, ABC):
    """
    A class to represent a bank account with basic operations such as deposits, withdrawals, and balance management.
    This class also acts as a Subject in the Observer Pattern to notify clients of significant account activities.

    Attributes:
        account_number (int): A unique identifier for the bank account.
        client_number (int): A unique identifier for the account holder.
        balance (float): The current balance in the account.
        date_created (date): The date the account was created.
    """

    # Constants for Observer Pattern notifications
    LARGE_TRANSACTION_THRESHOLD: float = 9999.99
    LOW_BALANCE_LEVEL: float = 50.0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        """
        Initializes the bank account with an account number, client number, an initial balance, and a creation date.

        Args:
            account_number (int): The number associated with the account.
            client_number (int): The ID associated with the account holder.
            balance (float): The initial balance to start the account with.
            date_created (date): The date the account was created.

        Raises:
            ValueError: If either the account number or client number is not an integer, or if the balance is not a valid float.
        """
        super().__init__()  # Initialize the Subject class
        # Ensuring account number is an integer
        if not isinstance(account_number, int):
            raise ValueError("The account number must be an integer.")
        self._account_number = account_number

        # Ensuring client number is an integer
        if not isinstance(client_number, int):
            raise ValueError("The client number must be an integer.")
        self._client_number = client_number

        # Assigning and validating the balance
        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0

        # Assigning the creation date
        self._date_created = date_created

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
    def date_created(self) -> date:
        """Returns the date the account was created."""
        return self._date_created

    def update_balance(self, amount: float):
        """
        Updates the account balance by a specified amount and notifies observers if necessary.

        Args:
            amount (float): The amount to add (or subtract if negative) from the balance.
        """
        try:
            amount = float(amount)
            self._balance += amount

            # Notify observers if the balance drops below the minimum threshold
            if self._balance < self.LOW_BALANCE_LEVEL:
                self.notify(f"Low balance warning ${self._balance:.2f}: on account {self._account_number}.")

            # Notify observers if the transaction amount exceeds the large transaction threshold
            if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
                self.notify(f"Large transaction ${amount:.2f}: on account {self._account_number}.")

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

    def __str__(self) -> str:
        """
        Returns a string representation of the account's number and its current balance.

        Returns:
            str: A string showing the account number and the balance formatted to two decimal places.
        """
        return f"Account No: {self._account_number}, Balance: ${self._balance:.2f}"