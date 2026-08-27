n1 = int(input('1.número: '))
n2 = int(input('2.número: '))
if n1 > n2:
    print('\033[34mO primeiro valor e maior\033[m')
elif n2 > n1:
    print('\033[34mO segundo valor e maior\033[m')
else:
    print('\033[31mNão existe valor maior, os dois são iguais!\033[m')
