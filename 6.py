res = 1

# пробегаемся по всем числам от 1 до заданного
for i in range(1, int(input()) + 1):
    fact = 1
    # считаем факториал для i
    for j in range(1, i + 1):
        fact *= j
    res += 1 / fact

print(res)