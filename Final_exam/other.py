import random

class Bank:
    total_balance = 0
    total_loan = 0
    loan_status = True
    account_list = []

    def generate_auto_acc_number(self):
        return random.randint(100, 200)

    def create_account(self, name, email, password, account_type):
        account_number = self.generate_auto_acc_number()
        if account_type == 'Savings':
            user = SavingsAccount(name, email, password, account_number)
        elif account_type == 'Current':
            user = CurrentAccount(name, email, password, account_number)
        elif account_type == 'Admin':
            user = Admin(name,email,password,account_number)
        else:
            print('Invalid account type!')
            return None

        self.account_list.append(user)
        return user

    def delete_account(self, account_number):
        for user in self.account_list:
            if user.account_number == account_number:
                self.account_list.remove(user)
                print(f"Account with account number {account_number} deleted.")
                return
        print(f"Account with account number {account_number} not found.")

    def show_users(self):
        for user in self.account_list:
            print(f'Name : {user.name}')

    def total_balances(self):
        print(f'Total balance: {self.total_balance} taka.')

    def total_loans(self):
        return f'Total Loans: {self.total_loan}'

    def loans_status(self):
        if self.loan_status:
            print('Loan Status is Enabled!')
        else:
            print('Loan Status is disabled!')


class Account:
    def __init__(self, name, email, password, account_number, account_type) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0
        self.loans = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposit {amount}')
            Bank.total_balance += amount
            print(f'Deposited {amount} taka. Now your balance is {self.balance} taka.')
        else:
            print('Invalid balance!')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw {amount}')
            print(f'Withdrawn {amount} taka. Now your balance is {self.balance} taka.')
        else:
            print('Not enough money in your account. Please deposit first!')

    def check_available_balance(self):
        print(f'Your current balance is {self.balance} taka.')

    def check_transaction_history(self):
        print(f'Transction History: {self.transaction_history}')

    def transfer(self, amount, receive):
            for name in self.name:
                if amount > 0 and self.balance >= amount and name == self.name:
                    self.balance -= amount
                    receive.balance += amount
                    self.transaction_history.append(f"Transferred: {amount} to {receive.name}")
                    print(f"Transferred {amount} taka to {receive.name} successfully.")
                else:
                    print("Error: Insufficient balance for transfer.")

    def take_loan(self, amount):
        if Bank.loan_status and self.loans <= 2:
            self.balance += amount
            self.loans += amount
            Bank.total_loan += amount
            self.transaction_history.append(f'Loan taken: {amount}')
            print(f'Loan of {amount} taka credited to your account. Your balance is {self.balance}.')
        elif not Bank.loan_status:
            print('Loan feature is currently turned off by the bank.')
        else:
            print('You have already taken the maximum number of loans.')

    def show_info(self):
        print(f'Information of {self.account_type} account by {self.name}')
        print(f'Account Type: {self.account_type}')
        print(f'Account Name: {self.name}')
        print(f'Email Address: {self.email}')
        print(f'Account Number: {self.account_number}')
        print(f'Account Balance: {self.balance}')
        print(f'Loan Taken: {self.loans}')
        print(f'Transaction History: {self.transaction_history}')
        for transaction in self.transaction_history:
            print(transaction)


class SavingsAccount(Account):
    def __init__(self, name, email, password, account_number) -> None:
        super().__init__(name, email, password, account_number, 'Savings')


class CurrentAccount(Account):
    def __init__(self, name, email, password, account_number) -> None:
        super().__init__(name, email, password, account_number, 'Current')

class Admin(Account):
    def __init__(self,name,email, password,account_number) -> None:
        super().__init__(name,email,password,account_number,'Admin')
    


# Main function

bank = Bank()
current_user = None
admin = None

while True:
    print('1. Admin: ')
    print('2. User: ')
    print('3. Exit')

    choice = int(input('Enter Your Option: '))

    if choice == 1:
        # Add admin functionality here if needed
        print('***Menu***')
        print('1. Create Account')
        print('2. Delete User Account')
        print('3. User Account List')
        print('4. Total Available Balance')
        print('5. Total Loans')
        print('6. Loan Status')
        print('7. Logout')

        op = int(input('Enter your option: '))

        if op == 1:
            if admin == None:
                print('No admin logged in !')
                ch = input('Register or Login? (R/L): ')
                if ch == 'R':
                    name = input('Enter your name: ')
                    email = input('Enter your email: ')
                    password = input('Enter your password: ')
                    account_type = input('Admin? (Admin): ')
                    if account_type in ['Admin']:
                        admin = bank.create_account(name,email, password,account_type)
                        print(f'Welcome {admin.name}')
                elif ch == 'L':
                    name = input('Enter your username: ')
                    password = input('Enter your password: ')
                    for account in bank.account_list:
                        if account.name == name and account.password == password:
                            admin = account
                        elif account.password != password:
                            print('Incorrect password !')
        elif op == 2:
            accNumber = int(input('Enter deleting account number: '))
            bank.delete_account(accNumber)
        elif op == 3:
            bank.show_users()
        elif op == 4:
            bank.total_balances()
        elif op == 5:
            bank.total_loans()
        elif op == 6:
            bank.loans_status()
        elif op == 7:
            admin = None
        else:
            print('Invalid choice !')

    elif choice == 2:
        if current_user == None:
            print('No users logged in!')
            ch = input('Register or Login? (R/L): ')
            if ch == 'R':
                # Registration logic
                name = input('Enter your name: ')
                email = input('Enter your email: ')
                password = input('Enter your password: ')
                account_type = input('Savings account or Current account? (Savings/Current): ')
                if account_type in ['Savings','Current']:
                    current_user = bank.create_account(name,email,password,account_type)
                else:
                    print('Invalid account type !')
            elif ch == 'L':
                # Login logic
                email = input('Enter your eamil: ')
                password = input('Enter your password: ')
                for account in bank.account_list:
                    if account.email == email and account.password == password:
                        current_user = account
                    elif account.password == password:
                        print('Incorrect password !')
            else:
                print('Invalid choice!')
        else:
            print(f'Welcome {current_user.name}')
            if current_user.account_type in ['Savings','Current']:
                print('***Menu***')
                print('1. Deposit Amount: ')
                print('2. Withdraw Amount: ')
                print('3. Check Available Balance: ')
                print('4. Transaction History: ')
                print('5. Transfer Balance: ')
                print('6. Take Loan: ')
                print('7. Show Information List: ')
                print('8. Logout: ')

                option = int(input('Enter choice: '))

                if option == 1:
                    deposit_amount = int(input('Enter deposit amount: '))
                    current_user.deposit(deposit_amount)
                elif option == 2:
                    withdraw_amount = int(input('Enter withdraw amount: '))
                    current_user.withdraw(withdraw_amount)
                elif option == 3:
                    current_user.check_available_balance()
                elif option == 4:
                    current_user.check_transaction_history()
                elif option == 5:
                    transfer_amount = int(input('Enter transfer amount: '))
                    account_name = input('Enter recipient account name: ')
                    current_user.transfer(transfer_amount,account_name)
                elif option == 6:
                    amount = int(input('How much loan amount: '))
                    current_user.take_loan(amount)
                elif option == 7:
                    current_user.show_info()
                elif option == 8:
                    current_user = None
                else:
                    print('Invalid Choose !')

    elif choice == 3:
        print('Exiting program. Goodbye!')
        break
    else:
        print('Invalid choice!')

