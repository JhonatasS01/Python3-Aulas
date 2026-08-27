print('-+'*6)
print('\033[34mNUMBER INFO\033[m')
print('-+'*6)
N = int(input('Digite um número inteiro: '))
print('\n\033[34mNúmero {} info: \033[m\n\033[32mDobro: \033[m{} \n\033[32m'
      'Triplo: \033[m{} \n\033[32mRaiz quadrada: \033[m{:.2f}'.format(N, N*2, N*3, N**(1/2)))
