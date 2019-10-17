ascii1 = 32
ascii2 = 127
shag = 0

for i in range( ascii1, ascii2 + 1 ):
    print(i,'-',chr(i),' ',end='')
    shag = shag + 1
    if shag == 10:
        print()
        shag = 0
