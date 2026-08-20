cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'verde' : '\033[32m',
         'vermelho' : '\033[31m'}

print('\033[33m=+\033[m'*13)
print('{}{:^27}{}'.format(cores['azul'], 'CALCULADORA DE PINTURA', cores['limpa']))
print('\033[33m=+\033[m'*13)
print('')
L = float(input('Digite a largura (M): '))
C = float(input('Digite a altura (M): '))
A = C * L
T = A / 2
print('-'*40)
print('{}Dimensão da parede em metros: {}{} x {}'
      '\n{}Área: {}{}m²\n{}Será necessário {}{}l {}de tinta!{}'.format(cores['azul'],
      cores['limpa'], L, C, cores['azul'], cores['limpa'], A, cores['azul'], cores['limpa'],
      T, cores['azul'], cores['limpa']))
print('-'*40)
