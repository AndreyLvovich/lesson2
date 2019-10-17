

chislo = int(input('Введите натуральное число '))

chislo2 = 0

while chislo > 0:
    chislo2 = chislo2 * 10 + chislo % 10
    chislo = chislo // 10

print(chislo2)

