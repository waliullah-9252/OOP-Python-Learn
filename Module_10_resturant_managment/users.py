from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        super().__init__()

class Coustomer(User):
    def __init__(self, name,phone,email,address,money) -> None:
        self.wallet = money
        self.__order = None
        self.due_bill = 0
        super().__init__(name,phone,email,address)

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order = order

    def place_order(self,order):
        self.order = order
        self.due_bill += order.bill
        print(f'{self.name} is place an order with bill {order.bill}')

    def eat_food(self,order):
        print(f'{self.name} now there eating food {order.items}')

    def pay_for_order(self,amount):
        pass

    def give_tips(self,tips_amount):
        pass

    def write_review(self):
        pass

class Employee(User):
    def __init__(self, name, phone, email, address,salary, startint_date,deparment) -> None:
        self.salary = salary
        self.starting_date = startint_date
        self.department = deparment
        super().__init__(name, phone, email, address)
    
    def receive_salary(self):
        self.due = 0

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, startint_date, deparment,cooking_items) -> None:
        self.cooking_items = cooking_items
        super().__init__(name, phone, email, address, salary, startint_date, deparment)

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, startint_date, deparment) -> None:
        super().__init__(name, phone, email, address, salary, startint_date, deparment)
        self.tips_amount = 0

    def take_order(self,order):
        pass

    def transfer_order(self,order):
        pass

    def serve_food(self,order):
        pass

    def receive_tips(self,amount):
        self.tips_amount += amount
        
class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, startint_date, deparment) -> None:
        super().__init__(name, phone, email, address, salary, startint_date, deparment)