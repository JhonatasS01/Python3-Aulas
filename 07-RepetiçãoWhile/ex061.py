from time import sleep

print('+='*15)
print('\033[34m{:^30}\033[m'.format('10 TERMOS DE UMA PA'))
print('+='*15)
fim = 'S'

while fim == 'S':
    cont = 0
    termo = int(input('Inicio: '))
    PA = int(input('Salto: '))
    if termo == 0 and PA == 0:
        fim = 'N'
        break
    while cont < 10:
        print(termo, end=' ➜ ')
        termo += PA
        cont += 1
    print('FIM!')
    print('-'*35)
    if fim == 'S':
        fim = str(input('\033[34mQuer continuar? [S/N] \033[m')).upper()
print('Saindo...')
sleep(2)
