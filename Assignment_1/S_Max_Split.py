string = str(input())
count_L = count_R = splits = 0 
result = ""
for char in string:
    if char == 'L':
        count_L += 1
    else:
        count_R += 1

    if count_L == count_R:
        splits += 1

print(splits)

for char in string:
    result += char
    if char == 'L':
        count_L += 1
    else:
        count_R += 1

    if count_L == count_R:
        print(result)
        result = ""
