n = int(input())
arr = list(map(int,input().strip().split()))[:n]
arr.reverse()
if arr == arr[::-1]:
    print("YES")
else:
    print("NO")