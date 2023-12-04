# improt to other function and built the main function
from menu import Burger,Pizza,Drinks,Menu
from resturent import Resturant
from users import Coustomer,Chef,Server,Manager
from order import Order

def main():

    menu = Menu()
    # creating some Burgers
    burger1 = Burger('Naga Burger', 550, 'Chicken', ['onion', 'souce', 'chili'])
    menu.add_menu_items('burger',burger1)
    burger2 = Burger('Beef Burger', 700, 'Beef', ['beef', 'onion', 'brade'])
    menu.add_menu_items('burger',burger2)

    #crateing some pizzas
    pizz1 = Pizza('Chicken Chess Pizza', 650, 'Large', ['chicken', 'onion', 'chese'])
    menu.add_menu_items('pizza', pizz1)
    pizz2 = Pizza('Beff Extra Chese Pizza', 950, 'Large', ['beff', 'onion','extra chese'])
    menu.add_menu_items('pizza',pizz2)

    #creating some drinks
    coke = Drinks('Coca Cola', 50, True)
    menu.add_menu_items('drink',coke)
    coffe = Drinks('Capachino Coffe', 450, False)
    menu.add_menu_items('drink',coffe)

    #show menu
    # menu.show_menu()


    # creating a resturant
    resturant = Resturant('Siblings Resturant',2000,menu)

    # add employees
    # create some manager
    manager1 = Manager('Rahim Mia', 932074, 'rahim@mia.com', 'MohammdPur,Dhaka', 2000, 'Jan 1,2021','Core')
    resturant.add_employee('manager',manager1)
    manager2 = Manager('Karim Mia', 349743, 'karim@mia.com', 'Farmgate,Dhaka', 2000, 'Feb 1,2021','Core')
    resturant.add_employee('manager',manager2)

    # create some chef
    chef1 = Chef('Abdul Salam', 34793, 'abdul@salam.com', 'Puran Dhaka', 3000, 'Jan 1, 2021','Chef','Everything')
    resturant.add_employee('chef',chef1)
    chef2 = Chef('Usman Mia', 349493, 'usman@mia.com', 'Gulsan, Dhaka', 3000, 'Jan 4, 2021','Chef','Everything')
    resturant.add_employee('chef',chef2)

    # create some server
    server1 = Server('Alice', 3049843, 'alice@email.com', 'Mirpur 10', 3333, 'Feb 2, 2022', 'Server')
    resturant.add_employee('server',server1)
    server2 = Server('Jhon', 3049843, 'jhon@email.com', 'Mirpur 12', 3432, 'Feb 5, 2022', 'Server')
    resturant.add_employee('server',server2)

    # showing employees
    # resturant.show_employees()

    # customer 1 placing an order
    coustomer1 = Coustomer('Tamim Iqbal', 340957430, 'tamim@iqbal.com', 'Gulshan 2', 100000)
    order1 = Order(coustomer1,[burger2,coke,coffe,pizz2])
    coustomer1.place_order(order1)
    resturant.add_order(order1)

    # coustomer one pay in an order1
    resturant.receive_payment(20000,order1,coustomer1)
    print(f'After payment first coustomenr , revenue: {resturant.revenue} and total balance: {resturant.balance}')


    # customer 2 placing an order
    coustomer2 = Coustomer('Sakib Khan', 340957430, 'shakib@khan.com', 'Gulshan 2', 100000)
    order2 = Order(coustomer1,[burger2,coke,burger1,pizz1])
    coustomer2.place_order(order2)
    resturant.add_order(order2)

    # coustomer one pay in an order1
    resturant.receive_payment(20000,order2,coustomer2)
    print(f'After payment second coustomenr , revenue: {resturant.revenue} and total balance: {resturant.balance}')


    # pay rent 
    resturant.pay_expense(resturant.rent,'Rent')
    print(f'After payment resturant rent, revenue: {resturant.revenue} and total balance: {resturant.balance} and Expense balance: {resturant.expense}')

    # pay salary 
    resturant.pay_salary(manager1)
    print(f'After payment manager 1 salary , revenue: {resturant.revenue} and total balance: {resturant.balance} and Expense balance: {resturant.expense}')












# calling main function method
if __name__ == '__main__':
    main()
