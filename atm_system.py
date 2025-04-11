import random
import time
import getpass

class ATMSystem:
    def __init__(self):
        # Initialize with random account balance between $1000 and $10000
        self.account_balance = random.randint(1000, 10000)
        self.pin = "1234"  # Default PIN (in real system, this would be hashed)
        self.is_authenticated = False
        self.transaction_history = []
        
    def authenticate(self):
        attempts = 3
        while attempts > 0:
            pin_input = getpass.getpass("Enter your 4-digit PIN: ")
            if pin_input == self.pin:
                self.is_authenticated = True
                return True
            else:
                attempts -= 1
                print(f"Invalid PIN. {attempts} attempts remaining.")
        print("Too many incorrect attempts. Card temporarily blocked.")
        return False
    
    def display_menu(self):
        print("\n===== ATM MENU (2025) =====")
        print("1. Check Balance")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Pay Bills")
        print("5. Transaction History")
        print("6. Exit")
    
    def check_balance(self):
        print("\nProcessing...")
        time.sleep(1)
        print(f"Your available balance is: ${self.account_balance}")
    
    def cash_withdrawal(self):
        print("\nCash Withdrawal Options:")
        print("1. $10     4. $100")
        print("2. $50     5. $500")
        print("3. $100    6. Custom Amount (up to $1000)")
        
        try:
            choice = int(input("Select withdrawal amount (1-6): "))
            amounts = {1: 10, 2: 50, 3: 100, 4: 100, 5: 500, 6: None}
            
            if choice == 6:
                amount = float(input("Enter amount to withdraw (max $1000): "))
                if amount > 1000:
                    print("Maximum withdrawal amount is $1000.")
                    return
            else:
                amount = amounts.get(choice, 0)
            
            if amount > self.account_balance:
                print("Insufficient funds.")
            else:
                print(f"Dispensing ${amount}...")
                time.sleep(2)
                self.account_balance -= amount
                self.transaction_history.append(f"Withdrawal: -${amount}")
                print(f"Transaction completed. Remaining balance: ${self.account_balance}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def cash_deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be positive.")
                return
            
            print(f"Depositing ${amount}...")
            time.sleep(1)
            self.account_balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            print(f"Deposit successful. New balance: ${self.account_balance}")
        except ValueError:
            print("Invalid amount entered.")
    
    def pay_bills(self):
        print("\nBill Payment Options:")
        print("1. Water Bill")
        print("2. Electricity Bill")
        print("3. Gas Bill")
        
        try:
            choice = int(input("Select bill type (1-3): "))
            bill_types = {1: "Water", 2: "Electricity", 3: "Gas"}
            bill_type = bill_types.get(choice, "Unknown")
            
            if bill_type == "Unknown":
                print("Invalid selection.")
                return
            
            amount = float(input(f"Enter {bill_type} bill amount: "))
            
            if amount > self.account_balance:
                print("Insufficient funds.")
            else:
                print(f"Paying ${amount} for {bill_type} bill...")
                time.sleep(1)
                self.account_balance -= amount
                self.transaction_history.append(f"Bill Payment ({bill_type}): -${amount}")
                print(f"Payment successful. Remaining balance: ${self.account_balance}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def show_transaction_history(self):
        print("\nTransaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for i, transaction in enumerate(self.transaction_history, 1):
                print(f"{i}. {transaction}")
    
    def run(self):
        print("===== Welcome to NextGen ATM (2025) =====")
        print("Please insert your card...")
        time.sleep(1)
        
        if not self.authenticate():
            return
        
        while self.is_authenticated:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-6): "))
                
                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    self.cash_withdrawal()
                elif choice == 3:
                    self.cash_deposit()
                elif choice == 4:
                    self.pay_bills()
                elif choice == 5:
                    self.show_transaction_history()
                elif choice == 6:
                    print("Thank you for using NextGen ATM. Goodbye!")
                    self.is_authenticated = False
                else:
                    print("Invalid choice. Please select 1-6.")
                
                if self.is_authenticated and choice != 6:
                    input("\nPress Enter to continue...")
            except ValueError:
                print("Invalid input. Please enter a number (1-6).")

# Main program
if __name__ == "__main__":
    atm = ATMSystem()
    atm.run()