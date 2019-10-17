

import random

chislo = random.randint(0, 100)

b = False

for i in range(0, 10):
    a = int(input('Введите угадываемое число: '))
    if a > chislo:
        print('Число больше')
    elif a < chislo:
        print('Число меньше')
    else:
        print('Вы угадали')
        b = True
        break
if b == False:
    print('Вы проиграли')
