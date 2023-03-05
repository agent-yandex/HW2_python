flag = True # флаг истинный, если не встретили ни один 0

# пробегаемся по всем значениям введенных чисел
for i in range(int(input())):
    # находим 0, флаг - ложный и печатаем йес
    if int(input()) == 0:
        print('YES')
        flag = False 
        break

if flag:
    print('NO')