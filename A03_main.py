"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Khush Patel"

# 1. Import all BankAccount types using the bank_account package
# Import date
# Import Client
from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from client.client import Client


# 2. Create a Client object with data of your choice.
client1 = Client(1001, "John", "Doe", "john.doe@example.com")


# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_account = ChequingAccount(12345, 1001, 500.0, date.today(), 100.0, 0.05)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
savings_account = SavingsAccount(67890, 1001, 1000.0, date.today(), 200.0)


# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a. Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
chequing_account.attach(client1)

# 4b. Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
savings_account.attach(client1)


# 5a. Create a second Client object with data of your choice.
client2 = Client(1002, "Jane", "Smith", "jane.smith@example.com")

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
savings_account2 = SavingsAccount(54321, 1002, 1500.0, date.today(), 300.0)


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer. Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.


# Transactions for ChequingAccount
try:
    print(f"Balance before deposit for ChequingAccount: ${chequing_account.balance:.2f}")
    chequing_account.deposit(200.0)  # Normal transaction (no notification)
    print(f"Balance after deposit for ChequingAccount: ${chequing_account.balance:.2f}")

    print(f"Balance before withdrawal for ChequingAccount: ${chequing_account.balance:.2f}")
    chequing_account.withdraw(50.0)   # Normal transaction (no notification)
    print(f"Balance after withdrawal for ChequingAccount: ${chequing_account.balance:.2f}")

    print(f"Balance before withdrawal for ChequingAccount: ${chequing_account.balance:.2f}")
    chequing_account.withdraw(1000.0) # Large transaction (notification)
    print(f"Balance after withdrawal for ChequingAccount: ${chequing_account.balance:.2f}")
except Exception as e:
    print(f"Error during ChequingAccount transaction: {e}")


# Transactions for SavingsAccount
try:
    print(f"Balance before deposit for SavingsAccount: ${savings_account.balance:.2f}")
    savings_account.deposit(100.0)    # Normal transaction (no notification)
    print(f"Balance after deposit for SavingsAccount: ${savings_account.balance:.2f}")

    print(f"Balance before withdrawal for SavingsAccount: ${savings_account.balance:.2f}")
    savings_account.withdraw(50.0)    # Normal transaction (no notification)
    print(f"Balance after withdrawal for SavingsAccount: ${savings_account.balance:.2f}")

    print(f"Balance before withdrawal for SavingsAccount: ${savings_account.balance:.2f}")
    savings_account.withdraw(300.0)   # Low balance (notification)
    print(f"Balance after withdrawal for SavingsAccount: ${savings_account.balance:.2f}")
except Exception as e:
    print(f"Error during SavingsAccount transaction: {e}")


# Transactions for SavingsAccount2
try:
    print(f"Balance before deposit for SavingsAccount2: ${savings_account2.balance:.2f}")
    savings_account2.deposit(500.0)   # Normal transaction (no notification)
    print(f"Balance after deposit for SavingsAccount2: ${savings_account2.balance:.2f}")

    print(f"Balance before withdrawal for SavingsAccount2: ${savings_account2.balance:.2f}")
    savings_account2.withdraw(200.0)  # Normal transaction (no notification)
    print(f"Balance after withdrawal for SavingsAccount2: ${savings_account2.balance:.2f}")

    print(f"Balance before withdrawal for SavingsAccount2: ${savings_account2.balance:.2f}")
    savings_account2.withdraw(2000.0) # Large transaction (notification)
    print(f"Balance after withdrawal for SavingsAccount2: ${savings_account2.balance:.2f}")
except Exception as e:
    print(f"Error during SavingsAccount2 transaction: {e}")
