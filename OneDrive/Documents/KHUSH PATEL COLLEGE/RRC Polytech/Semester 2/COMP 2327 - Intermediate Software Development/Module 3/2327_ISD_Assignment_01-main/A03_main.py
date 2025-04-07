"""
Description: A client program written to verify implementation 
of the Observer Pattern and Strategy Pattern.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Khush Patel"

from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import Client

# 1. Create a Client object
client1 = Client(1001, "John", "Doe", "john.doe@example.com")

# 2. Create bank accounts for client1
chequing_account = ChequingAccount(12345, 1001, 500.0, date.today(), 100.0, 0.05)
savings_account = SavingsAccount(67890, 1001, 1000.0, date.today(), 200.0)

# 3. Attach client1 to their accounts
chequing_account.attach(client1)
savings_account.attach(client1)

# 4. Create a second Client and their SavingsAccount
client2 = Client(1002, "Jane", "Smith", "jane.smith@example.com")
savings_account2 = SavingsAccount(54321, 1002, 1500.0, date.today(), 300.0)
savings_account2.attach(client2)

# 5. Transactions for ChequingAccount
try:
    print(f"\n[ChequingAccount Transactions]")
    print(f"Before deposit: ${chequing_account.balance:.2f}")
    chequing_account.deposit(200.0)  # No notification
    print(f"After deposit: ${chequing_account.balance:.2f}")

    print(f"Before withdrawal: ${chequing_account.balance:.2f}")
    chequing_account.withdraw(50.0)  # No notification
    print(f"After withdrawal: ${chequing_account.balance:.2f}")

    print(f"Before large withdrawal: ${chequing_account.balance:.2f}")
    chequing_account.withdraw(1000.0)  # Triggers large transaction notification
    print(f"After withdrawal: ${chequing_account.balance:.2f}")
except Exception as e:
    print(f"Error during ChequingAccount transaction: {e}")

# 6. Transactions for SavingsAccount
try:
    print(f"\n[SavingsAccount Transactions]")
    print(f"Before deposit: ${savings_account.balance:.2f}")
    savings_account.deposit(100.0)  # No notification
    print(f"After deposit: ${savings_account.balance:.2f}")

    print(f"Before withdrawal: ${savings_account.balance:.2f}")
    savings_account.withdraw(50.0)  # No notification
    print(f"After withdrawal: ${savings_account.balance:.2f}")

    print(f"Before low-balance withdrawal: ${savings_account.balance:.2f}")
    savings_account.withdraw(300.0)  # Triggers low balance notification
    print(f"After withdrawal: ${savings_account.balance:.2f}")
except Exception as e:
    print(f"Error during SavingsAccount transaction: {e}")

# 7. Transactions for SavingsAccount2
try:
    print(f"\n[SavingsAccount2 Transactions]")
    print(f"Before deposit: ${savings_account2.balance:.2f}")
    savings_account2.deposit(500.0)  # No notification
    print(f"After deposit: ${savings_account2.balance:.2f}")

    print(f"Before withdrawal: ${savings_account2.balance:.2f}")
    savings_account2.withdraw(200.0)  # No notification
    print(f"After withdrawal: ${savings_account2.balance:.2f}")

    print(f"Before large withdrawal: ${savings_account2.balance:.2f}")
    savings_account2.withdraw(2000.0)  # Triggers large transaction notification
    print(f"After withdrawal: ${savings_account2.balance:.2f}")
except Exception as e:
    print(f"Error during SavingsAccount2 transaction: {e}")
