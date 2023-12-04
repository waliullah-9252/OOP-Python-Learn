class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to {self.name}'s inventory.")

    def buy_product(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                if product.stock >= quantity:
                    product.stock -= quantity
                    print(f"Congratulations! You have successfully bought {quantity} units of {product.name}.")
                else:
                    print(f"Sorry, {product.name} is out of stock.")
                return
        print(f"Product with ID {product_id} not found in {self.name}'s inventory.")

    def checkout(self, amount):
        total = 0
        for item in self.products:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price', total)
        if amount < total:
            print(f'Please provide {total -amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money: {extra}')

# Example usage:

# Creating products
product1 = Product(1, "Laptop", 1000, 10)
product2 = Product(2, "Phone", 500, 20)

# Creating a shop
my_shop = Shop("My Electronics Store")

# Adding products to the shop
my_shop.add_product(product1)
my_shop.add_product(product2)

# Buying products from the shop
my_shop.buy_product(1, 5)  # Buying 5 laptops
my_shop.buy_product(2, 30)  # Trying to buy 30 phones (not enough stock)
my_shop.buy_product(3, 1)  # Trying to buy a non-existent product

shapan = Shop('Allen Shapan')

shapan.checkout(2000)
