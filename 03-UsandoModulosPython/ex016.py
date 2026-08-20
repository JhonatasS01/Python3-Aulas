'''from math import trunc
Num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}!'.format(Num, trunc(Num)))'''
print('\033[33m=-\033[m'*14)
print('\033[34m{:^28}\033[m'.format('NÚMERO REAL > INTEIRO'))
print('\033[33m=-\033[m'*14)
Num = float(input('Digite um número real: '))
print('O número \033[1;36m{}\033[m tem a parte inteira \033[1;32m{}\033[m!'.format(Num, int(Num)))