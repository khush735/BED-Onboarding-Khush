class BankAccount:
    """
    A class to represent a bank account with basic operations such as deposits, withdrawals, and balance management.

    Attributes:
        account_number (int): A unique identifier for the bank account.
        client_number (int): A unique identifier for the account holder.
        balance (float): The current balance in the account.

    Methods:
        deposit(amount): Adds a specified amount to the account balance.
        withdraw(amount): Reduces the account balance by a specified amount, subject to sufficient funds.
        update_balance(amount): Adjusts the balance by a given amount, either positive or negative.
        __str__(): Returns a string with the account's number and current balance.
    """

    def __init__(self, account_number: int, client_number: int, balance: float):
        """
        Initializes the bank account with an account number, client number, and an initial balance.

        Args:
            account_number (int): The number associated with the account.
            client_number (int): The ID associated with the account holder.
            balance (float): The initial balance to start the account with.

        Raises:
            ValueError: If either the account number or client number is not an integer, or if the balance is not a valid float.
        """
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

    def __str__(self) -> str:
        """
        Returns a string representation of the account's number and its current balance.

        Returns:
            str: A string showing the account number and the balance formatted to two decimal places.
        """
        return f"Account No: {self._account_number}, Balance: ${self._balance:.2f}"
