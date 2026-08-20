f = 'S'
soma = cont = maior = menor = 0
while f == 'S':
    n = int(input('\033[34mDigite o número: \033[m'))
    f = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    soma += n
    cont += 1
    if maior == 0:
        maior = n
    elif maior < n:
        maior = n

    if menor == 0:
        menor = n
    elif menor > n:
        menor = n
media = soma / cont
print('-'*40)
print(f'Números digitados: \033[34m{cont}\033[m')
print(f'O maior valor foi \033[32m{maior}\033[m e o menor foi \033[31m{menor}\033[m')
print('A média dos valores é: \033[33m{:.2f}\033[m'.format(media))
print('-'*40)
