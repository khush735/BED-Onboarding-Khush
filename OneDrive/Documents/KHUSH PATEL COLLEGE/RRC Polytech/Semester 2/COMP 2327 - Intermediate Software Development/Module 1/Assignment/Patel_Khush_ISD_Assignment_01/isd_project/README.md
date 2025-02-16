# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments. Each assignment will build on the work done in the previous assignment(s). Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Khush Patel

## Assignment
Assignment 1: Development of `Client` and `BankAccount` Classes
- This assignment focuses on creating two foundational classes: `Client`, which manages client information, and `BankAccount`, which handles client banking transactions. The classes must implement encapsulation and validation to ensure data integrity and security.

Assignment 2: Extending the BankAccount Class with Inheritance and Polymorphism
- This assignment builds upon the BankAccount class from Assignment 1 by introducing three specialized account types: ChequingAccount, InvestmentAccount, and SavingsAccount. Each subclass inherits from the BankAccount class and implements its own unique logic for calculating service charges, demonstrating polymorphism.


## Encapsulation

Encapsulation is a key principle in object-oriented programming that helps protect the internal state of an object. In the `BankAccount` class, we achieve this by defining important attributes (like `account_number`, `client_number`, and `balance`) as private, meaning they cannot be accessed directly from outside the class.

Instead of allowing external code to change these values directly, we provide specific methods (such as `deposit` and `withdraw`) that you must use. This way, we can implement checks and rules to ensure that all changes to the account are valid and safe, such as preventing withdrawals that exceed the account balance.

By using encapsulation, we ensure that the data within a `BankAccount` instance remains secure and consistent, ultimately leading to a more reliable banking system.