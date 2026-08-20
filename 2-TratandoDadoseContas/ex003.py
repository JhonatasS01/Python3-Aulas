from time import sleep

print('\033[33m=+\033[m'*12)
print('\033[36;40mCALCULADORA DE ADIÇÃO\033[m')
print('\033[33m=+\033[m'*12)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
print('Calculando...')
sleep(3)
print('A soma entre \033[34m{}\033[m e \033[32m{}\033[m é igual a \033[31m{}\033[m!'.format(n1, n2, s))
