def sum(num1 , num2 , num3 = 0 , num4 = 0 , num5 = 0):
    result = num1 + num2 + num3 + num4 + num5
    return result

total = sum(45,44,4,5,6)
# print('Total value is : ', total)

def all_sum(num1,*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum

total = all_sum(45,55,7,4,6)
print('Total value is : ',total)