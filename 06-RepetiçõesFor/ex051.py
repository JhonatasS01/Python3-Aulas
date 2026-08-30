print('+='*15)
print('\033[34m{:^30}\033[m'.format('10 TERMOS DE UMA PA'))
print('+='*15)
cont = int(input('Inicio: '))
PA = int(input('Salto: '))

for C in range(0, 10):
    print(cont, end=' ➜ ')
    cont += PA
print('ACABOU')
