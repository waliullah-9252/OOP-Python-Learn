class Phone():
    Manufactured = 'China'

    # intitialized or constructor in a class
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self,phone,sms):
        text = f'Sending to : {phone} and message is : {sms}'
        print(text)


my_phone = Phone('Waliullah', 'Realme', 20000)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone('Jakia', 'Samsung', 18000)
print(her_phone.owner, her_phone.brand, her_phone.price)

dad_phone = Phone('Hamidullah', 'Oppo', 14500)
print(dad_phone.owner, dad_phone.brand, dad_phone.price)
