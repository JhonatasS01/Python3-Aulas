N = int(input('Digite o número da tabuada: '))
print(f'\nTabuada do \033[33m{N}\033[m')
print('='*13)
for C in range(1, 10):
    print(f'\033[33m{N}\033[m  X  \033[33m{C}\033[m  = \033[34m{N*C}\033[m')
print(f'\033[33m{N}\033[m  X  \033[33m{10}\033[m = \033[34m{N*10}\033[m')
print('='*13)
