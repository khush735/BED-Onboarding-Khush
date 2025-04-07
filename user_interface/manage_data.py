__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Khush Patel"

import os
import sys
import csv
import logging
from datetime import datetime

# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# **************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE

root_dir = os.path.dirname(os.path.dirname(__file__))

log_dir = os.path.join(root_dir, 'logs')
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, 'manage_data.log')

logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')

data_dir = os.path.join(root_dir, 'data')
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')

# END GIVEN LOGGING AND FILE ACCESS CODE
# **************************************************************************

from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount

def load_data() -> tuple[dict, dict]:
    """
    Reads client and account data from CSV files,
    creates Client and BankAccount objects, and returns two dictionaries.

    Returns:
        tuple: (client_listing, accounts)
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA
    try:
        with open(clients_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    client_number = int(row['client_number'])
                    first_name = row['first_name']
                    last_name = row['last_name']
                    email = row['email_address']
                    client = Client(client_number, first_name, last_name, email)
                    client_listing[client_number] = client
                except Exception as e:
                    logging.error(f"Unable to create client: {e}")
    except Exception as e:
        logging.error(f"Error reading client file: {e}")

    # READ ACCOUNT DATA
    try:
        with open(accounts_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    account_number = int(row['account_number'])
                    client_number = int(row['client_number'])
                    balance = float(row['balance'])
                    date_created = row['date_created']
                    account_type = row['account_type']

                    account = None

                    if account_type == "ChequingAccount":
                        overdraft_limit = float(row['overdraft_limit'])
                        overdraft_rate = float(row['overdraft_rate'])
                        account = ChequingAccount(account_number, client_number, balance,
                                                   date_created, overdraft_limit, overdraft_rate)

                    elif account_type == "SavingsAccount":
                        minimum_balance = float(row['minimum_balance'])
                        account = SavingsAccount(account_number, client_number, balance,
                                                 date_created, minimum_balance)

                    elif account_type == "InvestmentAccount":
                        management_fee = float(row['management_fee'])
                        account = InvestmentAccount(account_number, client_number, balance,
                                                    date_created, management_fee)

                    else:
                        logging.error(f"Not a valid account type: {account_type}")
                        continue

                    if client_number in client_listing:
                        accounts[account_number] = account
                    else:
                        logging.error(f"Bank Account: {account_number} contains invalid Client Number: {client_number}")

                except Exception as e:
                    logging.error(f"Unable to create bank account: {e}")
    except Exception as e:
        logging.error(f"Error reading account file: {e}")

    return client_listing, accounts


def update_data(updated_account: BankAccount) -> None:
    """
    Updates the accounts.csv file with balance data from the updated BankAccount.
    Args:
        updated_account (BankAccount): Updated bank account object.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames

        for row in reader:
            account_number = int(row['account_number'])
            if account_number == updated_account.account_number:
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    with open(accounts_csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# **************************************************************************
# GIVEN TESTING SECTION
# **************************************************************************

if __name__ == "__main__":
    clients, accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"Account Number: {account.account_number} Balance: ${account.balance:,.2f}")

                if account.__class__.__name__ == "ChequingAccount":
                    print(f"Overdraft Limit: ${account.overdraft_limit:,.2f} "
                          f"Overdraft Rate: {account.overdraft_rate * 100:.2f}% Account Type: Chequing\n")

                elif account.__class__.__name__ == "SavingsAccount":
                    print(f"Minimum Balance: ${account.minimum_balance:,.2f} Account Type: Savings\n")

                elif account.__class__.__name__ == "InvestmentAccount":
                    print(f"Management Fee: ${account.management_fee:,.2f} Account Type: Investment\n")

        print("=========================================")
