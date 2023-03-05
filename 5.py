x = int(input())
# определяем максимальное число и их кол-во
max_num, count = 0, 1

while x != 0:
    # если x > max_num, то заменяем максимальное число и обнуляем кол-во
    if x > max_num:
        max_num, count = x, 1
    elif x == max_num:
        count += 1

    x = int(input())

print(count)