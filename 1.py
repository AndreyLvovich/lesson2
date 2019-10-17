while True:
    a = int(input('Введите число а '))
    b = int(input('Введите число b '))
    while True:
        znak = input('Введите: + , - , /, *, 0 ')
        if znak == '+' or znak == '-' or znak == '/' or znak == '*'  or znak == '0':
            print('Знак верен')
            break
        else:
            print('Знак не верен')
    if znak == '0':
        break
    elif znak == '+':
        print(a + b)
    elif znak == '-':
        print(a - b)
    elif znak == '*':
        print(a * b)
    elif znak == '/':
        if b == 0:
            print('Деление на 0')
        else:
            print(a / b)