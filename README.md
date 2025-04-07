# Intermediate Software Development: Automated Teller Project

This project is developed in phases across multiple assignments, gradually building a complete banking system. The system manages bank clients, their accounts, and various transaction types, and concludes with a fully interactive PySide6 GUI application.

## Author

**Khush Patel**

---

## Assignment

### Assignment 1: Development of `Client` and `BankAccount` Classes

This assignment focuses on creating two foundational classes: `Client`, which manages client information, and `BankAccount`, which handles banking transactions. These classes implement encapsulation and validation to ensure data integrity and secure account management.

---

### Assignment 2: Extending the BankAccount Class with Inheritance and Polymorphism

In this phase, the BankAccount class is extended using object-oriented principles. Three specialized account types were introduced:
- `ChequingAccount`
- `SavingsAccount`
- `InvestmentAccount`

Each subclass overrides the service charge calculation, demonstrating **polymorphism** through customized logic.

---

### Assignment 3: Applying Design Patterns (Strategy and Observer)

### Strategy Pattern
- Service charge calculations are decoupled from account classes using the **Strategy Pattern**.
- Specific strategies:
  - `OverdraftStrategy` for Chequing Accounts
  - `MinimumBalanceStrategy` for Savings Accounts
  - `ManagementFeeStrategy` for Investment Accounts

### Observer Pattern
- Used to simulate notifications for key events (like low balances or large withdrawals).
- `BankAccount` acts as the subject.
- `Client` acts as the observer that receives simulated email alerts.

---

### Assignment 4: GUI and Event-Driven Programming with PySide6

This assignment incorporates a full GUI using PySide6. Users can:
- Look up clients by number
- View their associated accounts
- Select an account and perform deposit/withdraw actions
- View updated balances dynamically

All interactions are handled using the **Event-Driven Programming Paradigm**.

---

## Encapsulation

Encapsulation is a key principle in object-oriented programming that helps protect the internal state of an object. In the `BankAccount` class, we achieve this by defining critical attributes such as `account_number`, `client_number`, and `balance` as private.

Access to these attributes is controlled via public getter methods and controlled operations (`deposit()` and `withdraw()`), which enforce validation rules (e.g., no overdraw without permission). This ensures that the data remains consistent and tamper-resistant throughout the system.

---

## Event-Driven Programming Paradigm

This application demonstrates the **Event-Driven Programming Paradigm** using PySide6. User interface widgets such as buttons, input fields, and tables emit signals based on user actions (e.g., clicks or text changes).

These signals are connected to slot methods (event handlers) that perform real-time logic like:
- Searching for clients
- Displaying account details
- Opening a transaction dialog
- Updating account balances

This paradigm allows the system to behave interactively and responsively, reacting to events rather than following a fixed execution order. It leads to a user-friendly and maintainable application design.
