t = int(input())
while t!=0:
    t-=1
    x,y = map(int,input(' ').split())
    if x > y:
        x,y = y,x
    sum = 0
    for num in range(x+1,y,1):
        if num % 2 == 1:
            sum += num
    print(sum)