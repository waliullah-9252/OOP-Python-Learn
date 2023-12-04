class Shoping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self, items, price, quantity):
        product = {'item' : items, 'price' : price , 'quantity' : quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('Total Price: ',total)
        if amount < total:
            print(f'You can provide {total - amount} money more!')
        else:
            print(f'Please back my extra {amount - total} money!')

    

wali = Shoping("Waliullah")
wali.add_to_cart('Book', 300, 6)
wali.add_to_cart('Khata', 50,5)
wali.add_to_cart('Pen', 5, 24)
print(wali.cart)

wali.checkout(2000)