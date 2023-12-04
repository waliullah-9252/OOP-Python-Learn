import random

class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def generate_account_number(self):
        return random.randint(100000, 999999)

    def create_account(self, name, email, address, account_type):
        account_number = self.generate_account_number()
        user = User(name, email, address, account_type, account_number)
        self.users.append(user)
        return user

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print(f"Account with account number {account_number} deleted.")
                return
        print(f"Account with account number {account_number} not found.")

    def show_all_accounts(self):
        for user in self.users:
            user.display_account_info()

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        status = "enabled" if self.loan_feature_enabled else "disabled"
        print(f"Loan feature is now {status}.")

class User:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.loan_taken = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Deposited {amount} successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrew {amount} successfully. Current balance: {self.balance}")

    def check_balance(self):
        return self.balance

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
            print(f"Transferred {amount} to {recipient.name} successfully.")
        else:
            print("Error: Insufficient balance for transfer.")

    def take_loan(self, amount):
        if len(self.transaction_history) <= 2 and self.loan_taken == 0 and bank.loan_feature_enabled:
            self.balance += amount
            self.loan_taken = amount
            self.transaction_history.append(f"Loan taken: {amount}")
            print(f"Loan of {amount} taken successfully. Current balance: {self.balance}")
            bank.total_loan_amount += amount
        else:
            print("Error: Unable to take a loan.")

    def display_account_info(self):
        print(f"Account Information for {self.name} (Account Number: {self.account_number}):")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}")
        print(f"Loan Taken: {self.loan_taken}")
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
        print("\n")

# Example Usage:

bank = Bank()

# Create user accounts
user1 = bank.create_account("John Doe", "john@example.com", "123 Main St", "Savings")
user2 = bank.create_account("Jane Doe", "jane@example.com", "456 Oak St", "Current")

# Admin operations
admin = bank.create_account("Admin", "admin@example.com", "Bank HQ", "Admin")
admin.delete_account(user2.account_number)
bank.toggle_loan_feature()

# User operations
user1.deposit(1000)
user1.withdraw(500)
user1.transfer(200, user2)
user1.take_loan(1000)

# Display account information
print("\nUser Account Information:")
user1.display_account_info()

# Display all accounts
print("\nAll User Accounts:")
bank.show_all_accounts()

# Display bank information
print(f"\nTotal Bank Balance: {bank.get_total_balance()}")
print(f"Total Loan Amount: {bank.get_total_loan_amount()}")
