n = int(input())
fibo_f_s = [0,1]
for i in range(2,n,1):
    next_value = fibo_f_s[i-1] + fibo_f_s[i-2]
    fibo_f_s.append(next_value)
print(' '.join(map(str,fibo_f_s)))

