n = int(input())
arr = list(map(int,input().strip().split()))[:n]
mx = max(arr)
mx_pos = arr.index(mx)
mn = min(arr)
mn_pos = arr.index(mn)
arr[mx_pos],arr[mn_pos] = arr[mn_pos],arr[mx_pos]
print(*arr)
