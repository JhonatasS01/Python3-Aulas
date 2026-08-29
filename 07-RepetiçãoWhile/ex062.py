from time import sleep

print('+='*15)
print('\033[34m{:^30}\033[m'.format('GERADOR DE PA'))
print('+='*15)
fim = 1
N = 10
cont = 0
#pegando os date
termo = int(input('Inicio: '))
PA = int(input('Salto: '))

while fim == 1:
    #proteção contra erros
    if termo == 0 and PA == 0:
        fim = 0
        print('Nenhum valor!')
        break
    #impressão da progressão
    while cont < N:
        print(termo, end=' ➜ ')
        termo += PA
        cont += 1
    print('...')
    print('-'*35)
    #continuar?
    if fim == 1:
        C = int(input('\033[34mQuer mostrar mais? [0 para não]: \033[m'))
        if C == 0:
            fim = 0
        elif C > 0:
            cont = 0
            N = C
print('Saindo...')
sleep(2)
