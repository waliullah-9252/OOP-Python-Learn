class Product:
    def __init__(self,name,price,stock) -> None:
        self.name = name
        self.price = price
        self.stock = stock


class Shop:
    def __init__(self,name) -> None:
        self.name = name
        self.products = []

    def add_to_cart(self,product):
        self.products.append(product)
        print(f'{product.name} to added in this cart!')

    def buy_product(self,quntity):
        for product in self.products:
                if product.stock >= quntity:
                    product.stock -= quntity
                    print(f'Congratualation, You have succesfully bought {quntity} units of {product.name} !')
                else:
                    print(f'Sorry, {product.name} is not stock!')




items1 = Product('Laptop',30000,5)
items2 = Product('Phone',20000,3)
items3 = Product('Sunglass',350,6)

my_shop = Shop('Gadget and Care')
my_shop.add_to_cart(items1)
my_shop.add_to_cart(items2)
my_shop.add_to_cart(items3)

my_shop.buy_product(5)



