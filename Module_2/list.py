#list or array is same 
#index =   0   1   2   3   4   5    6    7    8   9   10
numbers = [1 , 5 , 6 , 8 , 4 , 12 , 15 , 45 , 6 , 3 , 8]
#index = -11  -10 -9  -8  -7   -6   -5   -4  -3  -2  -1

#index wise print a value in array or list
print(numbers[3],numbers[-5])

# list start : end 
# start point is the start value but end point is previous value to access in list
print(numbers[3:8])
print(numbers[1:8])
print(numbers[-2:-8])

# list start : end : step
print(numbers[3:9:1])
print(numbers[3:9:2])
print(numbers[3:9:-1])
print(numbers[9:3:-1])
print(numbers[4:])
print(numbers[:8])
print(numbers[:]) # a list all value access
print(numbers[::-1]) # a list value reverse wise print

# numbers.append(10)
# print(numbers[:])
# numbers.insert(6,66)
# print(numbers[:])
# numbers.remove(66)
# print(numbers[:])
# numbers.pop()
# print(numbers[:])
# numbers.reverse()
# print(numbers[:])
numbers.index(12)
print(numbers)
# numbers.clear()
# print(numbers[:])
