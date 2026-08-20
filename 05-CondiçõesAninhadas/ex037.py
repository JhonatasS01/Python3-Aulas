print('\033[33m=+\033[m'*15)
print('\033[34m{:^30}\033[m'.format('CONVERSOR PARA PROGRAMADORES'))
print('\033[33m=+\033[m'*15)
N = int(input('Digite um número inteiro: '))
print('-'*22)
print('''Escolha a conversão
1-\033[34mBinário\033[m
2-\033[34mOctal\033[m
3-\033[34mHexadecimal\033[m''')
print('-'*22)
E = int(input('Digite uma opção: '))
print('-'*22)
if E == 1:
    print('\033[1;32mBINÁRIO\033[m')
    print('{} = {}'.format(N, bin(N)[2:]))
elif E == 2:
    print('\033[1;32mOCTAL\033[m')
    print('{} = {}'.format(N, oct(N)[2:]))
elif E == 3:
    print('\033[1;32mHEXADECIMAL\033[m')
    print('{} = {}'.format(N, hex(N)[2:]))
else:
    print('\033[1;31mOpcão inexistente, \ntente novamente!\033[m')
print('-'*22)
