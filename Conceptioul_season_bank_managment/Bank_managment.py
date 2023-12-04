from abc import ABC, abstractmethod
import random

class Bank:
    users = []
    loans = 0
    loan_feature = True

    @classmethod
    def generate_account_number(cls):
        return random.randint(100000, 999999)

    @classmethod
    def get_user_by_account_number(cls, account_number):
        for user in cls.users:
            if user.account_number == account_number:
                return user
        return None

    @classmethod
    def get_user_by_email(cls, email):
        for user in cls.users:
            if user.email == email:
                return user
        return None

    @classmethod
    def get_total_balance(cls):
        return sum(user.balance for user in cls.users)

    @classmethod
    def get_total_loans(cls):
        return cls.loans

    @classmethod
    def toggle_loan_feature(cls):
        cls.loan_feature = not cls.loan_feature


class Account(ABC):
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = Bank.generate_account_number()
        self.balance = 0
        self.transactions = []
        Bank.users.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f'Deposited ${amount}')
            print(f'Deposit successful. Your balance is ${self.balance}.')
        else:
            print('Invalid deposit amount!')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'Withdrawn ${amount}')
            print(f'Withdrawal successful. Your balance is ${self.balance}.')
        else:
            print('Withdrawal amount exceeded or invalid amount!')

    def check_balance(self):
        return f'Available balance: ${self.balance}'

    def check_transactions(self):
        return self.transactions

    def take_loan(self, amount):
        if Bank.loan_feature and Bank.loans < 2:
            self.balance += amount
            Bank.loans += amount
            self.transactions.append(f'Loan taken: ${amount}')
            print(f'Loan of ${amount} credited to your account. Your balance is ${self.balance}.')
        elif not Bank.loan_feature:
            print('Loan feature is currently turned off by the bank.')
        else:
            print('You have already taken the maximum number of loans.')

    def transfer(self, amount, target_account):
        target_user = Bank.get_user_by_account_number(target_account)
        if target_user:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                target_user.balance += amount
                self.transactions.append(f'Transferred ${amount} to account {target_account}')
                print(f'Transfer successful. Your balance is ${self.balance}.')
            else:
                print('Invalid transfer amount or insufficient balance!')
        else:
            print('Target account does not exist!')

    @abstractmethod
    def show_info(self):
        pass


class SavingsAccount(Account):
    def __init__(self, name, email, address, interest_rate) -> None:
        super().__init__(name, email, address, 'Savings')
        self.interest_rate = interest_rate

    def show_info(self):
        print(f'Information of {self.account_type} account by {self.name}')
        print(f'Account Type: {self.account_type}')
        print(f'Account Name: {self.name}')
        print(f'Account Number: {self.account_number}')
        print(f'Account Balance: ${self.balance}')

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)
        print(f'Interest applied. Interest balance is ${interest}.')


class SpecialAccount(Account):
    def __init__(self, name, email, address, overdraft_limit) -> None:
        super().__init__(name, email, address, 'Special')
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            self.transactions.append(f'Withdrawn ${amount}')
            print(f'Withdrawal successful. Your balance is ${self.balance}.')
        else:
            print('Invalid withdrawal amount or exceeding overdraft limit!')

    def show_info(self):
        print(f'Information of {self.account_type} account by {self.name}')
        print(f'Account Type: {self.account_type}')
        print(f'Account Name: {self.name}')
        print(f'Account Number: {self.account_number}')
        print(f'Account Balance: ${self.balance}')


class Admin:
    def create_account(self, name, email, address, account_type, interest_rate=None, overdraft_limit=None):
        if Bank.get_user_by_email(email) is None:
            if account_type == 'Savings':
                return SavingsAccount(name, email, address, interest_rate)
            elif account_type == 'Special':
                return SpecialAccount(name, email, address, overdraft_limit)
            else:
                print('Invalid account type!')
        else:
            print('User with this email already exists.')

    def delete_account(self, account_number):
        user = Bank.get_user_by_account_number(account_number)
        if user:
            Bank.users.remove(user)
            print(f'User with account number {account_number} deleted successfully.')
        else:
            print('User not found.')

    def view_all_accounts(self):
        return [user.__dict__ for user in Bank.users]

    def check_total_balance(self):
        return f'Total available balance in the bank: ${Bank.get_total_balance()}'

    def check_total_loans(self):
        return f'Total loans in the bank: ${Bank.get_total_loans()}'

    def toggle_loan_feature(self):
        Bank.toggle_loan_feature()
        status = 'enabled' if Bank.loan_feature else 'disabled'
        print(f'Loan feature is now {status}.')


# Example Usage:
admin = Admin()

# Creating user accounts
user1 = admin.create_account("John Doe", "john@example.com", "123 Main St", "Savings", interest_rate=5)
user2 = admin.create_account("Jane Smith", "jane@example.com", "456 Oak St", "Special", overdraft_limit=1000)

# Depositing and withdrawing from user accounts
user1.deposit(1000)
user1.withdraw(500)

user2.deposit(2000)
user2.withdraw(1500)

# Checking balances and transactions
print(user1.check_balance())
print(user1.check_transactions())

print(user2.check_balance())
print(user2.check_transactions())

# Taking a loan
user1.take_loan(200)
user2.take_loan(500)

# Transferring money between accounts
user1.transfer(300, user2.account_number)

# Admin tasks
print(admin.view_all_accounts())
print(admin.check_total_balance())
print(admin.toggle)


























# currntusers = None
# while True:
#     if currntusers == None:
#         print('No users logged in !')
#         ch = input('Register or Login? (R/L): ')
#         if ch == 'R':
#             name = input('Enter your name: ')
#             email = input('Enter your email: ')
#             password = input('Enter your password: ')
#             acc_type = input('Savings or Current Account? (sv/ca)')
#             if acc_type == 'sv':
#                 currntusers = SavingsAccount(name,email,password)
#             elif acc_type == 'ca':
#                 currntusers = CurrentAccount(name,email,password)
#             else:
#                 print('Invalid account type !')
#         else:
#             email = input('Enter your email: ')
#             password = input('Enter your password: ')
#             for account in Account.users:
#                 if account.email == email and account.password == password:
#                     currntusers = account
#                     break
#                 elif account.email != email and account.password != password:
#                     print('Incorrect email and password !')

#     else:
#         print(f'Welcome {currntusers.name} !')
#         if currntusers.account_type == 'Savings':
#             print('***Menu***')
#             print('1. Show Information: ')
#             print('2. Deposite: ')
#             print('3. Withdraw: ')
#             print('4. Change Information: ')
#             print('5. Apply Interest: ')
#             print('6. Logout: ')

#             op = int(input('Choose Your Option: '))

#             if op == 1:
#                 currntusers.showInfo()
#             elif op == 2:
#                 amount = int(input('Enter Deposite amount: '))
#                 currntusers.deposite(amount)
#             elif op == 3:
#                 amount = int(input('Enter withdraw amount: '))
#                 currntusers.withdraw(amount)
#             elif op == 4:
#                 name = input('Enter new name: ')
#                 password = input('Enter new password: ')
#                 currntusers.changeInfo(name,password)
#             elif op == 5:
#                 currntusers.applyInterest()
#             elif op == 6:
#                 currntusers = None
#             else:
#                 print('Invalid Option !')
        
#         elif currntusers.accountType == 'Spcial':
#             print('***Menu***')
#             print('1. Show Information: ')
#             print('2. Deposite: ')
#             print('3. Withdraw: ')
#             print('4. Change Information: ')
#             print('5. Logout: ')

#             op = int(input('Choose Your Option: '))

#             if op == 1:
#                 currntusers.showInfo()
#             elif op == 2:
#                 amount = int(input('Enter Deposite amount: '))
#                 currntusers.deposite(amount)
#             elif op == 3:
#                 amount = int(input('Enter Withdraw amount: '))
#                 currntusers.withdraw(amount)
#             elif op == 4:
#                 name = input('Enter new name: ')
#                 password = input('Enter new password: ')
#                 currntusers.changeInfo(name,password)
#             elif op == 5:
#                 currntusers = None
#             else:
#                 print('Invalid Option !')
#         else:
#             print('Invalid Acoount type ! please enter valid account type !')



