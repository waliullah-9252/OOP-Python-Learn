from abc import ABC,abstractmethod
class Account(ABC):
    account_list = []
    def __init__(self,name, accountNumber, password, accountType) -> None:
        self.name = name
        self.accountNumber = accountNumber
        self.password = password
        self.accountType = accountType
        self.balance = 0
        Account.account_list.append(self)

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposite Balance is {amount} taka. Now , Your Balance is {self.balance} taka.')
        else:
            print('Invalid Balance !')

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Withdraw balance is {amount} taka. Now , Your balance after withdraw {self.balance} taka.')
        else:
            print(f'Your Acount not enough money, you can first deposite !')

    @abstractmethod
    def showInfo(self):
        raise NotImplementedError

    def changeInfo(self,name):
        self.name = name
        print(f'Name is changed of {self.accountNumber}')

    # overloading method by changeInfo function
    def changeInfo(self,name,password):
        self.name = name
        self.password = password
        print(f'Name and password change of {self.accountNumber}')


class SavingsAccount(Account):
    def __init__(self, name, accountNumber, password, interstRate) -> None:
        super().__init__(name, accountNumber, password, 'Savings')
        self.interestRate = interstRate
    
    def showInfo(self):
        print(f'Information of {self.accountType} account by {self.name}')
        print(f'Account Type: {self.accountType}')
        print(f'Account Name: {self.name}')
        print(f'Account Number: {self.accountNumber}')
        print(f'Account Balance: {self.balance}')
    
    def applyInterest(self):
        interst = self.balance * (self.interestRate / 100)
        print(f'Interest is applied and interest balance is {interst} taka.')
        self.deposite(interst)

class SpcialAccount(Account):
    def __init__(self, name, accountNumber, password, limit) -> None:
        super().__init__(name, accountNumber, password, 'Spcial')
        self.limit = limit

    def showInfo(self):
        print(f'Information of {self.accountType} account by {self.name}')
        print(f'Account Type: {self.accountType}')
        print(f'Account Name: {self.name}')
        print(f'Account Number: {self.accountNumber}')
        print(f'Account Balance: {self.balance}')

    def withdraw(self, amount):
        if amount > 0 and amount >= self.limit:
            self.balance -= amount
            print(f'Withdraw balance is {amount} taka. Now , your balance is {self.balance} taka.')
        else:
            print('Invalid balance !')



# main function implement or object create

currentUsers = None
while True:
    if currentUsers == None:
        print('No users logged in !')
        ch = input('Resigter or Login? (R/L): ')
        if ch == 'R':
            name = input('Type Your Name: ')
            accountNumber = input('Type Your Account Number: ')
            password = input('Type Your Password: ')
            type = input('Savings Account or Spcial Account? (sv/sp)')
            if type =='sv':
                interestRate = int(input('Enter Your InterstRate: '))
                currentUsers = SavingsAccount(name,accountNumber,password,interestRate)
            elif type == 'sp':
                limit = int(input('OverDrft Limit : '))
                currentUsers = SpcialAccount(name,accountNumber,password,limit)
            else:
                print('Invalid Account Type ! Please enter valid account type.')
        else:
            accountNumber = input('Type Your Account Number: ')
            password = input('Type Your Password: ')
            for account in Account.account_list:
                if account.accountNumber == accountNumber and account.password == password:
                    currentUsers = account
                    break
                elif account.password != password:
                    print(f'Incorrect Password ! plase enter your valid password !')

    else:
        print(f'Welcome {currentUsers.name} !')
        if currentUsers.accountType == 'Savings':
            print('***Menu***')
            print('1. Show Information: ')
            print('2. Deposite: ')
            print('3. Withdraw: ')
            print('4. Change Information: ')
            print('5. Apply Interest: ')
            print('6. Logout: ')

            op = int(input('Choose Your Option: '))

            if op == 1:
                currentUsers.showInfo()
            elif op == 2:
                amount = int(input('Enter Deposite amount: '))
                currentUsers.deposite(amount)
            elif op == 3:
                amount = int(input('Enter withdraw amount: '))
                currentUsers.withdraw(amount)
            elif op == 4:
                name = input('Enter new name: ')
                password = input('Enter new password: ')
                currentUsers.changeInfo(name,password)
            elif op == 5:
                currentUsers.applyInterest()
            elif op == 6:
                currentUsers = None
            else:
                print('Invalid Option !')
        
        elif currentUsers.accountType == 'Spcial':
            print('***Menu***')
            print('1. Show Information: ')
            print('2. Deposite: ')
            print('3. Withdraw: ')
            print('4. Change Information: ')
            print('5. Logout: ')

            op = int(input('Choose Your Option: '))

            if op == 1:
                currentUsers.showInfo()
            elif op == 2:
                amount = int(input('Enter Deposite amount: '))
                currentUsers.deposite(amount)
            elif op == 3:
                amount = int(input('Enter Withdraw amount: '))
                currentUsers.withdraw(amount)
            elif op == 4:
                name = input('Enter new name: ')
                password = input('Enter new password: ')
                currentUsers.changeInfo(name,password)
            elif op == 5:
                currentUsers = None
            else:
                print('Invalid Option !')
        else:
            print('Invalid Acoount type ! please enter valid account type !')

    
