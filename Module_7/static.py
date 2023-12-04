# static attribute or (class attribute in python )
# static mehtod 
# class method 
# difference between in static mehtod vs class method

""" 
Class Method
1. The class method takes cls (class) as first argument.
2. Class method can access and modify the class state.
3. The class method takes the class as parameter to know about the state of that class.
4. @classmethod decorator is used here.

Static Method
1. The static method does not take any specific parameter.
2. Static Method cannot access or modify the class state.
3. Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters.
4. 
@staticmethod decorator is used here.

"""

class Shoping:
    cart = [] # calss attribute or static attribute
    origin = 'china'

    def __init__(self,name,location) -> None:
        self.name = name
        self.location = location

    def perchase(self,item, price, amount):
        remaining = amount - price
        print(f'Bying : {item} and price: {price} and remaing balance: {remaining}')

    @staticmethod
    def multiply(a,b):
        result = a * b
        print(result)

    @classmethod
    def hudai(self,item,price):
        print(f'Hudai dakci {item} ta , {price} taka ato dam diya keda kinbe amar kase ato taka nai!')
   

basundhara = Shoping('Basundhara City Shoping Mall', 'Panthopath')
# basundhara.perchase('Phone', 30000, 50000)

Shoping.hudai('pant', 5000) # class method use
basundhara.hudai('pnat', 5000)

Shoping.multiply(5,6) # static method use
basundhara.multiply(5,7)
