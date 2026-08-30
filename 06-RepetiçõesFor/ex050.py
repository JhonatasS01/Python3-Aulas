S = 0
cont = 0
for C in range(1, 7):
    N = int(input(f'{C}. número: '))
    if N % 2 == 0:
        S += N
        cont += 1
print(f'A soma dos números pares é: \033[34m{S}\033[m')
print(f'Números pares: \033[34m{cont}\033[m')
