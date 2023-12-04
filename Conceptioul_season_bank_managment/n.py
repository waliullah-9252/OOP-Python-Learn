class Shop:
    def __init__(self) -> None:
        self.cus_account = []
        self.sell_account = []

    def customer_account(self, name, email, password):
        cus_info = {'Name': name, 'email': email, 'password': password}
        self.cus_account.append(cus_info)

    def seller_account(self, name, email, password):
        sell_info = {'Name': name, 'email': email, 'password': password}
        self.sell_account.append(sell_info)


c1=Shop()
while True:
    print('1 : Customer create new account')
    print('2 : Seller create new account')
    print('3 : See All Account')
    op=int(input('Enter Your Option : '))
    if op==1:
        name=input('Your name : ')
        email=input('Your Email : ')
        password=int(input('Your Password : '))
        c1.customer_account(name,email,password)
        print("Customer Accounts:", c1.cus_account)

    elif op==2:
        name=input('Your name : ')
        email=input('Your Email : ')
        password=int(input('Your Password : '))
        c1.seller_account(name,email,password)
        print("Customer Accounts:", c1.sell_account)
        
    elif op==3:
        print("Customer Accounts:", len(c1.cus_account))
        print("Seller Accounts:", len(c1.sell_account))