# function is a first class object
def double_deacker():
    print('Started a Double deacker')
    def inner_fun():
        print('inside in inner')
        return 3000
    return inner_fun


# print(double_deacker()())

def do_something(work):
    print('Work Started')
    # print(work)
    work()
    print('Word Ended')

# do_something(3)
# do_something('ami onk busy aj')

def codding():
    print('Now coding in python programming !')

# do_something(codding)

def sleeping():
    print('Now I am sleeping and dream python codding !')

do_something(sleeping)