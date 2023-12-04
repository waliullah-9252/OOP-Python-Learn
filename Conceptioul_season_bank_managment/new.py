import random

class Bank:
    def __init__(self):
        self.users = []
        self.loans = 0
        self.loan_feature = True

    def generate_account_number(self):
        return random.randint(100000, 999999)

    def get_user_by_account_number(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None

    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def get_total_balance(self):
        return sum(user.balance for user in self.users)

    def get_total_loans(self):
        return self.loans

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature


class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = None
        self.balance = 0
        self.transactions = []
        self.loan_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdrawal amount exceeded"
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            return f"Withdrawal successful. Available balance: ${self.balance}"

    def check_balance(self):
        return f"Available balance: ${self.balance}"

    def check_transactions(self):
        return self.transactions

    def take_loan(self, amount, bank):
        if bank.loan_feature and self.loan_taken < 2:
            self.balance += amount
            self.loan_taken += 1
            bank.loans += amount
            self.transactions.append(f"Loan taken: ${amount}")
            return f"Loan of ${amount} credited to your account. Available balance: ${self.balance}"
        elif not bank.loan_feature:
            return "Loan feature is currently turned off by the bank."
        else:
            return "You have already taken the maximum number of loans."


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_user(self, name, email, address, account_type):
        if self.bank.get_user_by_email(email) is None:
            user = User(name, email, address, account_type)
            user.account_number = self.bank.generate_account_number()
            self.bank.users.append(user)
            return f"Account created successfully. Account number: {user.account_number}"
        else:
            return "User with this email already exists."

    def delete_user(self, account_number):
        user = self.bank.get_user_by_account_number(account_number)
        if user:
            self.bank.users.remove(user)
            return f"User with account number {account_number} deleted successfully."
        else:
            return "User not found."

    def view_all_users(self):
        return [user.__dict__ for user in self.bank.users]

    def check_total_balance(self):
        return f"Total available balance in the bank: ${self.bank.get_total_balance()}"

    def check_total_loans(self):
        return f"Total loans in the bank: ${self.bank.get_total_loans()}"

    def toggle_loan_feature(self):
        self.bank.toggle_loan_feature()
        return f"Loan feature is now {'enabled' if self.bank.loan_feature else 'disabled'}."


# Example Usage:
bank = Bank()
admin = Admin(bank)

# Creating a user account
user_account = admin.create_user("John Doe", "john@example.com", "123 Main St", "Savings")
print(user_account)

# Depositing and withdrawing from the user account
john = bank.get_user_by_email("john@example.com")
john.deposit(1000)
print(john.withdraw(500))

# Checking balance and transactions
print(john.check_balance())
print(john.check_transactions())

# Taking a loan
print(john.take_loan(200, bank))

# Admin tasks
print(admin.view_all_users())
print(admin.check_total_balance())
print(admin.toggle_loan_feature())
