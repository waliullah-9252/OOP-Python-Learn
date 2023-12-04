def call():
    print('Calling someone person who do not know this')

class Phone:
    brand = 'Realme'
    color = 'Blue'
    price = 20000
    features = ['Camera', 'Falsh Light', 'Music']

    def call(self):
        text = 'Calling one persion'
        return text
    
    def send_sms(self,phone,sms):
        text = f"Sending to :{phone} and message : {sms}"
        return text
    


my_phone = Phone()
print(my_phone.features)
res = my_phone.call()
print(res)
result = my_phone.send_sms(9658976, 'I Miss you, EveryDay!!')
print(result)


