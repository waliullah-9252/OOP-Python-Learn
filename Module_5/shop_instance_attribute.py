class Shop:
    Shoping_Mall = 'Jamuna Future Park'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self,item):
        self.cart.append(item)

mehjabin = Shop('Mehjabin')
mehjabin.add_to_cart('Shoes')
mehjabin.add_to_cart('Sunglass')
mehjabin.add_to_cart('Daimond Ring')
print('Mehjabin cart list: ', mehjabin.cart)

nisho = Shop('Nisho')
nisho.add_to_cart('Watch')
nisho.add_to_cart('Phone')
nisho.add_to_cart('Cap')
print('Nisho cart list: ', nisho.cart)

apurbo = Shop('Aprubo')
apurbo.add_to_cart('T-Shrt')
apurbo.add_to_cart('Pnat')
print('Apurbo cart List: ',apurbo.cart)

