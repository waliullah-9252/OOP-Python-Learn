# ***Difference between list and dictionary in Python:

# ***List***
# 1. List is an order collection of elements of index value,like array couse list and array is same terms.
# 2. List initialized with [].
# 3. List is mutable,and allows duplicates values.

# ***Dictionary***
# 1. Dictionary is key value pair.
# 2. Dictionary initialized with {}.
# 3. Dictionary is unordered and mutable and not allowed duplicates values.



# *** args is a non keyword arguments
# *** In this function , we should use * before parameters name. The paramenters passed a tuple value. If I want the print single value taht is possible like example below this code 

def all_sum(num1,*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum

total = all_sum(45,55,7,4,6)
print('Total value is : ',total)

# *** kargs is a keyword arguments
# *** In this function , we use ** before parameters name. The argumnents are passed dictionary . As I know that Dictionary is a key and value pair 

def famous_name(first,last,**addition):
    name = f'The famous name is : {first} {last}'
    print(addition)
    for key,value in addition.items():
        print(key,value)
    return name

name = famous_name(first='Abduls',last='Salam',title='Doctor',addition='Md.',title2='Shayek',last2='alhadisi')
print(name)
