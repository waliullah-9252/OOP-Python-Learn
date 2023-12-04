import random

class Bank:
    total_balance = 0
    total_loan = 0
    loan_status = True
    account_list = []

    def generate_auto_acc_number(self):
        return random.randint(100,200)

    def create_account(self,name, email, password, account_type):
        account_number = self.generate_auto_acc_number()
        admin = Account(name, email, password, account_number, account_type)
        self.account_list.append(admin)
        return admin
    
    def delete_account(self, account_number):
        for user in self.account_list:
            if user.account_number == account_number:
                self.account_list.remove(user)
                print(f"Account with account number {account_number} deleted.")
                return
            else:
                print(f"Account with account number {account_number} not found.")
    
    def show_user(self):
        for user_list in self.account_list:
            if self.account_list is user_list:
                print(f'{user_list}')
            else:
                print('No user found !')
    
    def total_balances(self):
        return f'Total balance: {self.total_balance} taka.'
    
    def total_loans(self):
        return f'Total Loans: {self.total_loan}'
    
    def loans_status(self):
        if self.loan_status == True:
            print('Loan Status is Enabled !')
        else:
            print('Loan Status is disabled !')
    


class Account:
    def __init__(self, name, email, password,account_number, account_type) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0
        self.loans = 0
        self.transaction_history = []

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposite {amount}')
            print(f'Depostie balance {amount} taka, Now your balance is {self.balance} taka.')
        else:
            print('Invalid balance !')
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw {amount}')
            print(f'Withdraw balance {amount} taka, Now your balance after withdraw {self.balance} taka.')
        else:
            print('Not ! enough money your account, please diposite first !')

    def checkAvailableBalance(self):
        print(f'Your current balance is {self.balance} taka.')

    def check_transction_history(self):
        return self.transaction_history
    
    def transfer(self, amount, recipient):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
            print(f"Transferred {amount} to {recipient.name} successfully.")
        else:
            print("Error: Insufficient balance for transfer.")

    def take_loan(self, amount):
        if Bank.loan_status and Bank.loan_status < 2:
            self.balance += amount
            Bank.loans += amount
            self.transaction_history.append(f'Loan taken: {amount}')
            print(f'Loan of {amount} credited to your account. Your balance is {self.balance}.')
        elif not Bank.loan_status:
            print('Loan feature is currently turned off by the bank.')
        else:
            print('You have already taken the maximum number of loans.')

    def showInfo(self):
        print(f'Information of {self.account_type} account by {self.name}')
        print(f'Account Type: {self.account_type}')
        print(f'Account Name: {self.name}')
        print(f'Email Address: {self.email}')
        print(f'Account Number: {self.account_number}')
        print(f'Account Balance: {self.balance}')
        print(f'Loan Taken: {self.loans}')
        print(f'Transction History: {self.transction_history}')
        for transction in self.transaction_history:
            print(transction)


class SavingsAccount(Account):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password,'Savings')
        # self.savings_account  = savings_account

        
class CurrentAccount(Account):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password, 'Current')
        # self.current_account = current_account



# main function 

bank = Bank()
currentuser = None
while True:
    print('Welcome Admin !')
    print('***Menu***')
    print('1. Create Account: ')
    print('2. Deleted User Account: ')
    print('3. User Account List: ')
    print('4. Total Available Balance: ')
    print('5. Total Loans: ')
    print('6. Loan Status: ')

    op = int(input('Enter Choose Your Option: '))

    if op == 1:
        if currentuser == None:
            print('No users logged in!')
            ch = input('Register or Login? (R/L): ')
            if ch == 'R':
                name = input('Enter Your Name: ')
                email = input('Enter Your Email: ')
                password = input('Enter Your Password: ')
                type = input('Savings account or current account? (sv/ca): ')
                if type == 'sv':
                    currentuser = SavingsAccount(name, email, password)
                elif type == 'ca':
                    currentuser = CurrentAccount(name, email, password)
                else:
                    print('Invalid account type !')
            else:
                email = input('Enter Your Email: ')
                password = input('Enter Your Password: ')
                for account in bank.account_list:
                    if account.email == email and account.password == password:
                        currentuser = account
                        break
                    elif account.password != password:
                        print('Incorrect Password ! ')

        else:
            print(f'Welcome {currentuser.name}')
            if currentuser.account_type == 'Savings' or currentuser.account_type == 'Current':
                print('***Menu***')
                print('1. Deposite Amount: ')
                print('2. Withdraw Amount: ')
                print('3. Check Available Balance: ')
                print('4. Transction History: ')
                print('5. Transfer Balance: ')
                print('6. Take Loan: ')
                print('7. Show Information List: ')

                op = int(input('Enter Choose Your Option: '))

                if op == 1:
                    deposite = int(input('Enter deposite balance: '))
                    currentuser.deposite(deposite)
                elif op == 2:
                    withdraw = int(input('Enter withdraw balance: '))
                    currentuser.withdraw(withdraw)
                elif op == 3:
                    currentuser.checkAvailableBalance()
                elif op == 4:
                    currentuser.check_transction_history()
                elif op == 5:
                    amount = int(input('Enter transfer amount: '))
                    name = input('Enter receiver name: ')
                    currentuser.transfer(amount,name)
                elif op == 6:
                    amount = int(input('How much loan amount: '))
                    currentuser.take_loan(amount)
                elif op == 7:
                    currentuser.showInfo()

    elif op == 2:
        account_number = bank.generate_auto_acc_number()
        bank.delete_account(account_number)
        print(f'Succesfully Deleted Account and account number is {account_number}.')
    elif op == 3:
        bank.show_user()
    elif op == 4:
        bank.total_balances()
    elif op == 5:
        bank.total_loans()
    elif op == 6:
        bank.loans_status()
                   

                           

     

    