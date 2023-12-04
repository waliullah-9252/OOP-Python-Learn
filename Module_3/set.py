# list --> []
# tuple --> ()
# set --> {}

numbers = [12,34,45,23,12,34,46,56,23]
print(numbers)
set_of_numbers = set(numbers)
print(set_of_numbers)
set_of_numbers.add(66)
print(set_of_numbers)
set_of_numbers.remove(12)
print(set_of_numbers)

if 23 in set_of_numbers:
    print('Yes')
else:
    print('No')

for items in set_of_numbers:
    print(items)

A = {1,2,4,6}
B = {3,4,7,9}
print(A&B) # only common or duplicate is two set of value show
print(A | B) #only common or duplicate value is show one times two sets 