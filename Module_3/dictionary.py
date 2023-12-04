numbers = [1,4,6,7,34,5,6,7]
print(numbers)

person1 = ['kala pakhi', 'kaliapur', '23', 'student']
print(person1)
# key value of pair
# dictionary
# hash table 
# overlpa with set
# {key:value, key:value, key:value}

person2 = {'name:': 'kala pakhi', 'address:': 'kaliapur', 'age:': '23', 'job:': 'facebooker'}
print(person2)
print(person2['job:'])
print(person2.keys())
print(person2.values())
person2['language:'] = 'python'
person2['name:'] = 'sada pakhi'
print(person2)
del person2['age:']
print(person2)

# spicaily dictionary looping 
for items in person2:
    print(items)

for key,value in person2.items():
    print(key,value)