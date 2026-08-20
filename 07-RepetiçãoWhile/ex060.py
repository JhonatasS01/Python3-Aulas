from math import factorial

n = int(input('Digite um número: '))
f = factorial(n)
print(f'\nO fatorial de {n}! é:')
while n > 0:
    if n > 0:
        print(n, end='\033[34m x \033[m')
        n -= 1
        if n == 0:
            print(n, '\033[34m = \033[m ', end='')
print(f)
