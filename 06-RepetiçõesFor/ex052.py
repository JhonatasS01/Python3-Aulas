print('\033[33m=+\033[m'*14)
print('\033[34m{:^26}\033[m'.format('E PRIMO?'))
print('\033[33m=+\033[m'*14)
N = int(input('Digite um número inteiro: '))
V = 0
print(' ')
for C in range(1, N + 1):
    if N % C == 0:
        #contador amarelo
        print('\033[1;33m', end='')
        V += 1
    else:
        #contador vermelho
        print(f'\033[1;31m', end='')
    print(f'{C}', end=' ')
if V == 2:
   print('\033[1;32m\nO número e primo\033[m')
else:
   print('\033[1;31m\nO número não e primo\033[m')
print(f'O número e divisível \033[1;33m{V}\033[m vezes')
