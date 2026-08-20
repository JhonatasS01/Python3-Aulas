soma = 0
cont = 0
for C in range(1, 501, 2):
    if C % 3 == 0:
        cont += 1
        soma += C
print('\nA soma de todos os números entre 1 e 500,'
      f'\nmúltiplos de 3 e ímpares é: \033[34m{soma}\033[m')
print(f'Foram encontradas \033[34m{cont}\033[m números.')
