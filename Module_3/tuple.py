def numtiple():
    return 3,4
print(numtiple())

things = 'phone','charger','tripod','laptop','camera','mouse'
print(things)
print(type(things))
print(things[0])
print(things[4])
print(things[-3])
print(things[2:5])
print(things[::-1])

if 'cover' in things:
    print('Yes')
else:
    print('No')

for items in things:
    print(items)

# things[0] = 'wagon'
# print(things)

print(len(things))
mega = ([2,3,4],[5,6,7])
print(mega)
print(mega[0])
print(mega[1])
mega[0][1] = 55
print(mega)
