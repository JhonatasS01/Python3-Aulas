print(f'{'\033[32mSomador de Números\033[m':=^40}')
print('\033[33mDigite 999 para parar\033[m')
cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'''\033[34mNúmeros digitados: \033[m{cont}
\033[34mSoma entre eles: \033[m{soma}''')
