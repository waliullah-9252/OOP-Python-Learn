class Resturant:
    def __init__(self,name,rent,menu = []) -> None:
        self.name = name
        self.rent = rent
        self.orders = []
        self.menu = menu
        self.chefs = None
        self.servers = None
        self.managers = None
        # self.chefs = []
        # self.servers = []
        # self.managers = []
        self.revenue = 0
        self.balance = 0
        self.expense = 0
        self.profit = 0

    def add_employee(self,employee_type,employee):
        if employee_type == 'chef':
            # self.chefs.append(employee)
            self.chefs = employee
        elif employee_type == 'server':
            # self.servers.append(employee)
            self.servers = employee
        elif employee_type == 'manager':
            # self.managers.append(employee)
            self.managers = employee

    def add_order(self,order):
        self.orders.append(order)

    def receive_payment(self,amount,order,coustomer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            coustomer.due_bill = 0
            print(f'You can back {amount - order.bill} taka.')
        else:
            print(f'Not enough money, pay more {order.bill - amount}')
        
    def pay_expense(self,amount,description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'Not enough money to pay {amount}')

    def pay_salary(self,employee):
        print(f'Paying salary for {employee.name} and they are salary: {employee.salary}')
        if employee.salary < self.balance:
            self.expense += employee.salary
            self.balance -= employee.salary
            employee.receive_salary()

    def show_employees(self):
        print('----------All Manager List----------')
        # for manager in self.managers:
        if self.managers is not None:
            print(f'Manager Name: {self.managers.name} with Salary: {self.managers.salary}')
        print('----------All Chef List----------')
        # for chef in self.chefs:
        if self.chefs is not None:
            print(f'Chef Name: {self.chefs.name} with Salary: {self.chefs.salary}')
        print('----------All Server List----------')
        # for server in self.servers:
        if self.servers is not None:
            print(f'Server Name: {self.managers.name} with Salary: {self.managers.salary}')
        