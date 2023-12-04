n = int(input())
a = list(map(int, input().split()))

my_dictionary = {}
for num in a:
    if num in my_dictionary:
        my_dictionary[num] += 1
    else:
        my_dictionary[num] = 1

remove = 0

for num, cnt in my_dictionary.items():
    if cnt > num:
        remove += cnt - num
    elif cnt < num:
        remove += cnt

print(remove)
