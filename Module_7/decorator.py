import math
import time
def timer(func):
    def inner(*args, **kwargs):
        print('Time Started')
        start = time.time()
        # print(func)
        func(*args, **kwargs)
        print('Time Ended')
        end = time.time()
        print(f'Total time taken: {end - start}')
    return inner

# timer()()

@timer
def get_factorial(n):
    print('Starting factorial')
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')

get_factorial(100)