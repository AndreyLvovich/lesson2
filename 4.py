

n = int(input('Введите число элементов n '))

summ = 0
a = 1

for i in range(n):
    summ = summ + a
    a = a / ( -2 )

print('Сумма элементов числа = ', summ)