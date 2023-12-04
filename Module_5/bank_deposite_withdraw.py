class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 500000

    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'Sorry! Enough balance your account! You can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'Sorry! Not Enough balance in this bank, You can withdraw higest {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'You can withdraw now {amount}')
            print(f'Now your account balance after Withdraw {self.get_balance()}')


brac = Bank(50000)
brac.withdraw(400)
brac.withdraw(100000000)
brac.withdraw(30000)

dbbl = Bank(10000)
dbbl.deposite(5000)
dbbl.deposite(6000)
print(dbbl.balance)

dbbl.withdraw(8000)
