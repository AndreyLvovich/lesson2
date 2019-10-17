

chislo = int(input('Введите натуральное число '))

chet = 0
nechet = 0

while chislo > 0:
    if chislo % 2 == 0:
        chet = chet + 1
    else:
        nechet = nechet + 1
    chislo = chislo // 10

print('четных цифр - ', chet)
print('четных цифр - ', nechet)
