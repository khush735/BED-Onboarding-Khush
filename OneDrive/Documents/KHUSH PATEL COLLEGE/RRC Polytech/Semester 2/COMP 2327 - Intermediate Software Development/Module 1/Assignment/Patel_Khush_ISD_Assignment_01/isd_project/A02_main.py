"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Khush Patel"

# 1. Import all BankAccount types using the bank_account package
#    Import date from datetime
from datetime import date, timedelta
from bank_account import BankAccount, ChequingAccount, SavingsAccount, InvestmentAccount

# 2. Create an instance of a ChequingAccount with values of your 
#    choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(
    account_number=123456,
    client_number=7890,
    balance=-200.0,  
    date_opened=date(2020, 1, 1),
    overdraft_limit=-100.0,
    overdraft_rate=0.05
)

# 3. Print the ChequingAccount created in step 2.
print("Chequing Account (Initial State):")
print(chequing_account)

# 3b. Print the service charges amount if calculated based on the 
#     current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing_account.get_service_charges():.2f}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
#     enough money into the chequing account to avoid overdraft fees.
chequing_account.deposit(300.0)  # Bring balance above overdraft limit

# 4b. Print the ChequingAccount
print("\nChequing Account (After Deposit):")
print(chequing_account)

# 4c. Print the service charges amount if calculated based on the 
#     current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing_account.get_service_charges():.2f}")

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
#    choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(
    account_number=654321,
    client_number=7890,
    balance=1000.0,  
    date_opened=date(2020, 1, 1),
    minimum_balance=500.0
)

# 6. Print the SavingsAccount created in step 5.
print("Savings Account (Initial State):")
print(savings_account)

# 6b. Print the service charges amount if calculated based on the 
#     current state of the SavingsAccount created in step 5.
print(f"Service Charges: ${savings_account.get_service_charges():.2f}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
#     enough money from the savings account to cause the balance to fall 
#     below the minimum balance.
savings_account.withdraw(600.0)  

# 7b. Print the SavingsAccount.
print("\nSavings Account (After Withdrawal):")
print(savings_account)

# 7c. Print the service charges amount if calculated based on the 
#     current state of the SavingsAccount created in step 5.
print(f"Service Charges: ${savings_account.get_service_charges():.2f}")

print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
#    choice including a date created within the last 10 years.
investment_account_recent = InvestmentAccount(
    account_number=987654,
    client_number=7890,
    balance=10000.0,
    date_opened=date(2020, 1, 1),  # Within last 10 years
    management_fee=1.99
)

# 9a. Print the InvestmentAccount created in step 8.
print("Investment Account (Recent):")
print(investment_account_recent)

# 9b. Print the service charges amount if calculated based on the 
#     current state of the InvestmentAccount created in step 8.
print(f"Service Charges: ${investment_account_recent.get_service_charges():.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
#     choice including a date created prior to 10 years ago.
investment_account_old = InvestmentAccount(
    account_number=987655,
    client_number=7890,
    balance=10000.0,
    date_opened=date(2010, 1, 1),  # More than 10 years ago
    management_fee=1.99
)

# 11a. Print the InvestmentAccount created in step 10.
print("\nInvestment Account (Old):")
print(investment_account_old)

# 11b. Print the service charges amount if calculated based on the 
#      current state of the InvestmentAccount created in step 10.
print(f"Service Charges: ${investment_account_old.get_service_charges():.2f}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
#     by using the withdraw method of the superclass and withdrawing 
#     the service charges determined by each instance invoking the 
#     polymorphic get_service_charges method.
accounts = [chequing_account, savings_account, investment_account_recent, investment_account_old]

for account in accounts:
    service_charges = account.get_service_charges()
    account.withdraw(service_charges)

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print("Final State of All Accounts:")
for account in accounts:
    print(account)
    print(f"Service Charges: ${account.get_service_charges():.2f}\n")