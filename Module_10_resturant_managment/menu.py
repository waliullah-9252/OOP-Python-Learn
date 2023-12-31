class Food:
    def __init__(self,name , price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def __init__(self, name, price,meat,ingredients) -> None:
        self.meat = meat
        self.ingredients = ingredients
        super().__init__(name, price)

class Pizza(Food):
    def __init__(self, name, price,size,toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings

class Drinks(Food):
    def __init__(self, name, price,isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold


# composition 

class Menu:
    def __init__(self) -> None:
        self.burgers = []
        self.pizzas = []
        self.drinks = []

    def add_menu_items(self,item_type,item):
        if item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'drink':
            self.drinks.append(item)
    
    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

    def remove_burger(self,burger):
        if burger in self.burgers:
            self.burgers.remove(burger)

    def remove_drinks(self,drink):
        if drink in self.drinks:
            self.drinks.remove(drink)

    def show_menu(self):
        print('---------All Buger List----------')
        for burger in self.burgers:
            print(f'Burger Name: {burger.name} and Price: {burger.price}')
        print('-------------------------------')
        print('----------All Pizzas List-----------')
        for pizza in self.pizzas:
            print(f'Pizza Name: {pizza.name} and Price: {pizza.price}')
        print('-------------------------------')
        print('---------All Drinks List-----------')
        for drink in self.drinks:
            print(f'Drinks Name: {drink.name} and Price: {drink.price}')
        print('-------------------------------')
