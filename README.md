# ATM Management System (2025)

![ATM System Demo](demo.gif) <!-- You can add a screenshot/gif later -->

A modern Python-based ATM management system simulating 2025 banking features including cash withdrawal/deposit, bill payments, and transaction history with secure PIN authentication.

## Features

- 🔒 **Secure 4-digit PIN authentication** with attempt limiting
- 💵 **Cash withdrawal** with preset amounts ($10-$500) or custom amounts (up to $1000)
- 🏦 **Cash deposit** functionality
- 💡 **Bill payments** (water, electricity, gas) directly from account
- 📜 **Transaction history** tracking
- 💰 **Realistic account simulation** with random balance generation
- ⏱️ **Processing delays** for authentic ATM experience

## Technologies Used

- Python 3.x

- Built-in modules:

  - `random` - For generating random account balance

  - `time` - For realistic processing delays

  - `getpass` - For secure PIN input

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/atm-management-system.git
   cd atm-management-system

  python --version
  
  #Run the File
  
  python atm_system.py

  #Code Structure

  ATMSystem
├── __init__() - Initializes account with random balance

├── authenticate() - Handles PIN verification

├── display_menu() - Shows main menu options

├── check_balance() - Displays current balance

├── cash_withdrawal() - Handles money withdrawal

├── cash_deposit() - Processes deposits

├── pay_bills() - Manages utility payments

├── show_transaction_history() - Displays past transactions

└── run() - Main program loop


#OUTPUT OF THE PROGRAM

===== Welcome to NextGen ATM (2025) =====

Please insert your card...

Enter your 4-digit PIN: ****


===== ATM MENU (2025) =====

1. Check Balance

2. Cash Withdrawal

3. Cash Deposit

4. Pay Bills

5. Transaction History

6. Exit

Enter your choice (1-6): 2


Cash Withdrawal Options:

1. $10     4. $100
2. $50     5. $500
3. $100    6. Custom Amount

Select withdrawal amount (1-6): 5

Dispensing $500...

Transaction completed. Remaining balance: $7342



#Future Enhancement
  
Add database integration for persistent accounts

  Implement OTP verification for transactions

  Add check deposit functionality

  Support for multiple user accounts

  Graphical user interface (GUI)
