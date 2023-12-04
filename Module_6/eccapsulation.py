# encapsulation ---> hide details
# access modifiers: public , protected , private
class Bank:
    def __init__(self,holder_name,initial_deposite) -> None:
        self.holder_name = holder_name  # public attribute
        self._brance = 'Bannai Bank'  # protected 
        self.__balance = initial_deposite  # private 

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f'Fokira taka nai!'
    

rafsan = Bank('RafsanThe ChotoBhai' , 20000)
print(rafsan.holder_name)
rafsan.holder_name = 'Boro bhai'
rafsan.deposite(40000)
print(rafsan.get_balance())
print(rafsan.holder_name)
rafsan.withdraw(30000)
print(rafsan.get_balance())
print(rafsan._brance)
# print(dir(rafsan))
print(rafsan._Bank__balance)