print('=+'*10)
print('\033[34m{:23}\033[m'.format('CONVERSOR DE DOLÁRES'))
print('=+'*10)
D = float(input('\nDigite o seu saldo: R$'))
print('-'*30)
print('Você podera comprar US${}{:.2f}{}'
      '\nVocê podera comprar €{}{:.2f}{}'.format('\033[32m', D/5.46, '\033[m',
      '\033[32m', D/6.36, '\033[m'))
print('-'*30)
