prev_num = int(input()) # первое число

if prev_num != 0: # проверяем, не нулевая ли у нас последовательность
    num = int(input()) # второе число

    # текущая длина монотонной последовательности и максимальная длина
    current_len, max_len = 1, 0

    # флаг False - когда последовательность убывающая
    # флаг True - когда последовательность возрастающая
    flag = None
    if prev_num > num:
        flag = False
    elif prev_num < num:
        flag = True

    # цикл, пока введенное число != 0
    while num != 0:
        # если 2 числа совпадают по условию с флагом, то 
        # прибавляем к текущей последовательности 1
        if prev_num > num and flag is False:
            current_len += 1
        elif prev_num < num and flag is True:
            current_len += 1
        else:
            # если последовательноть не верная и текущая длина больше
            # максимальной, то она становится максимальной
            if max_len < current_len:
                max_len = current_len

            # проверяем не равны ли у нас числа, чтобы не сделать
            # текущую последовательность больше чем нужно
            if prev_num != num:
                current_len = 2
            else:
                current_len = 1

            # расставляем флаги заново
            flag = None
            if prev_num > num:
                flag = False
            elif prev_num < num:
                flag = True

        prev_num, num = num, int(input())

    # поскольку цикл может завершиться раньше, чем последовательность
    # оборвется, то делаем конечное сравнение текущей и максимальной посл.
    if max_len < current_len:
        print(current_len)
    else:
        print(max_len)
else:
    print(0)
