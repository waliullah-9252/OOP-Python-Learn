balance = 3000

def buying_something(item,price):
    global balance
    print('Before buying anything balance is : ',balance)
    balance = balance - price
    print('After buying sunglass then balance is : ',balance)

buying_something('sunleglass',1000)