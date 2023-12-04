def calculate_equation_result(x, n):
    result = 0
    power = 0
    for i in range(0, n, 2):
        result += x**i

    if power % 2 == 0:
        result -= 1
    return result

x, n = map(int, input().split())
result = calculate_equation_result(x, n)
print(result)
