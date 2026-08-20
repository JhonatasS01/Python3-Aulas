from math import sqrt, floor
#ctrl + espaço abri as opções do from import
#import math
num = int(input('Digite um número: '))
raiz = sqrt(num)
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {} aredondando para cima!'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {:.2f} aredondando para baixo!'.format(num, floor(raiz)))
#print('A raiz de {} é igual a {:.2f} formatado!'.format(num, raiz))
