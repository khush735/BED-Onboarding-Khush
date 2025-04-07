__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Khush Patel"

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, Signal
from ui_superclasses.details_window import DetailsWindow
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):

    balance_updated = Signal(BankAccount)

    def __init__(self, account):
        super().__init__()

        if not isinstance(account, BankAccount):
            self.reject()
            return

        self.account = copy.copy(account)
        self.account_number_label.setText(str(self.account.account_number))
        self.balance_label.setText(f"${self.account.balance:,.2f}")

        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)

    def __on_apply_transaction(self):
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.critical(self, "Deposit Failed",
                                 "Transaction amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            sender = self.sender()
            if sender == self.deposit_button:
                transaction = "Deposit"
                self.account.deposit(amount)
            elif sender == self.withdraw_button:
                transaction = "Withdraw"
                self.account.withdraw(amount)
            else:
                return

            self.balance_label.setText(f"${self.account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
            self.balance_updated.emit(self.account)

        except Exception as e:
            QMessageBox.critical(self, "Transaction Failed",
                                 f"{transaction} Failed: {str(e)}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    def __on_exit(self):
        self.close()
