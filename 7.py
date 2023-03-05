count = 1 # 1 - первый делитель, то есть кол-во сразу 1
num = int(input())

# считаем все числа от 2 до самого числа
for i in range(2, num + 1):
    if num % i == 0:
        count += 1

print(count)