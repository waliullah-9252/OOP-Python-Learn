def doubled(x):
    return x*2
result = doubled(55)
print(result)

doubled1 = lambda x : x * 2
res = doubled1(54)
print(res)

square = lambda x : x * x
print(square(6))

# multiple paramenters
add = lambda x,y : x + y
print(add(3,4))

numbers = [12,34,45,23,12,34,46,56,23]
print(numbers)
double_nums = map(lambda x : x * 2, numbers)
print(list(double_nums))
square_nums = map(lambda x : x * x, numbers)
print(list(square_nums))


actors = [
    {'name': 'Sabana', 'age': 65},
    {'name': 'Sabnor', 'age': 45},
    {'name': 'Sabila nur', 'age': 28},
    {'name': 'Mehjabin', 'age': 32},
    {'name': 'Tanjin Tisa', 'age': 30},
]

joniur = filter(lambda actor : actor['age'] < 40, actors)
print(list(joniur))
again = filter(lambda actor: actor['age'] % 5 == 0, actors)
print(list(again))

numbers = [10, 20, 30, 40, 50]
print(numbers[-4:-1])

numbers = [9, 15, 2, 36]
numbers[1:4] = [20, 14, 36]
print(numbers)

person_info = {"name": "Sakib", "salary": 80000}
value = person_info.get("salary")
print(value)