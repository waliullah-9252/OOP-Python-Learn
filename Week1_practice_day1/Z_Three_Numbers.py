k,s = map(int,input().split())
count = 0
for x in range(0,k):
    for y in range(0,k):
        for z in range(0,k):
            if x+y+z == s and x>=0 and y>=0 and z>=0 and x<=k and y<=k and z<=k:
                count += 1
print(count)