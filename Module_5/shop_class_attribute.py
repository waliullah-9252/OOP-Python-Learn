class Shop:
    cart = [] # calss attribute 
    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_cart(self,item):
        self.cart.append(item)

mehjabeeeen = Shop('Mehjabin')
mehjabeeeen.add_to_cart('Shoes')
mehjabeeeen.add_to_cart('Sunglass')
mehjabeeeen.add_to_cart('Daimond Ring')
print('Mehjabins Cart List: ', mehjabeeeen.cart)

Afran_Nisho = Shop("Afran Nisho")
Afran_Nisho.add_to_cart('Watch')
Afran_Nisho.add_to_cart('Phone')
Afran_Nisho.add_to_cart('Cap')
print('Afran Nisho cart List: ',Afran_Nisho.cart)