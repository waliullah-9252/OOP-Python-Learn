n = int(input())
a = list(map(int,input().split()))
count = 0
even = True
while True:
    for i in range(n):
        if a[i] % 2 == 1:
            even = False
            break
    if not even:
        break
    for i in range(n):
        a[i] /= 2
    count += 1
print(count)

