class Pen:
    Manufactured = 'Bangladesh'

    def __init__(self,onwer,brand,price):
        self.onwer = onwer
        self.brand = brand
        self.price = price


my_pen = Pen('Waliullah', 'Matador Hi-School', 5)
her_pen = Pen('Jakia Sultana', 'Matador Pin-point', 6)
dad_pen = Pen('Hamidullah', 'Econo DX', 4)
print(my_pen.onwer, my_pen.brand, my_pen.price)
print(her_pen.onwer, her_pen.brand, her_pen.price)
print(dad_pen.onwer, dad_pen.brand, dad_pen.price)