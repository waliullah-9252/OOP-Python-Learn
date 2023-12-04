n, q = map(int, input().split())
a = list(map(int, input().strip().split()))[:n]
while q != 0:
    q = q - 1
    l, r = map(int, input().split())
    sum_result = 0
    for item in a[l-1:r]:
        sum_result += item
    print(sum_result)
