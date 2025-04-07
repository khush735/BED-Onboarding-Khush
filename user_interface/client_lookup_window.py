__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Khush Patel"

from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt, Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.manage_data import load_data, update_data
from user_interface.account_details_window import AccountDetailsWindow

class ClientLookupWindow(LookupWindow):

    def __init__(self):
        super().__init__()
        self.client_listing, self.accounts = load_data()
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)

    def on_lookup_client(self):
        client_num_str = self.client_number_edit.text()

        try:
            client_num = int(client_num_str)
        except ValueError:
            QMessageBox.critical(self, "Non-Numeric Client",
                                 "Client Number must be a valid number.")
            self.reset_display()
            return

        if client_num not in self.client_listing:
            QMessageBox.critical(self, "Client Not Found",
                                 f"Client Number {client_num} not found.")
            self.reset_display()
            return

        client = self.client_listing[client_num]
        self.client_info_label.setText(str(client))

        self.account_table.setRowCount(0)
        for account in self.accounts.values():
            if account.client_number == client_num:
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)

                acc_number_item = QTableWidgetItem(str(account.account_number))
                acc_number_item.setTextAlignment(Qt.AlignCenter)

                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight)

                date_item = QTableWidgetItem(str(account.date_created))
                date_item.setTextAlignment(Qt.AlignCenter)

                acc_type_item = QTableWidgetItem(account.__class__.__name__)
                acc_type_item.setTextAlignment(Qt.AlignCenter)

                self.account_table.setItem(row, 0, acc_number_item)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, date_item)
                self.account_table.setItem(row, 3, acc_type_item)

        self.account_table.resizeColumnsToContents()

    def on_text_changed(self):
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        acc_item = self.account_table.item(row, 0)

        if not acc_item:
            QMessageBox.warning(self, "Invalid Selection", "Selected item is empty.")
            return

        acc_num_str = acc_item.text().strip()

        if not acc_num_str:
            QMessageBox.warning(self, "Invalid Selection", "Account Number cannot be blank.")
            return

        try:
            acc_num = int(acc_num_str)
        except ValueError:
            QMessageBox.critical(self, "Bank Account does not Exist", "Account Number is invalid.")
            return

        if acc_num in self.accounts:
            selected_account = self.accounts[acc_num]
            details_window = AccountDetailsWindow(selected_account)
            details_window.balance_updated.connect(self.update_data)
            details_window.exec()
        else:
            QMessageBox.critical(self, "Bank Account does not Exist",
                                 "Selected account is not found in system.")

    def update_data(self, updated_account):
        for row in range(self.account_table.rowCount()):
            acc_num = int(self.account_table.item(row, 0).text())
            if acc_num == updated_account.account_number:
                self.account_table.item(row, 1).setText(f"${updated_account.balance:,.2f}")
                break
        self.accounts[updated_account.account_number] = updated_account
        update_data(updated_account)

