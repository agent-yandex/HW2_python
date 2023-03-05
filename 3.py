x = int(input())
summ, count = x, 0

# пока x != 0 прибавляем его к общей сумме summ и к количеству чисел count + 1
while x != 0:
    x = int(input())
    summ += x
    count += 1

# если count = 0, то пишем просто 0 во избежании деления на 0
if count != 0:
    print(summ / count)
else:
    print(0)