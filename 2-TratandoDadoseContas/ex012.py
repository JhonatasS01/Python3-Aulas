print('\033[33m=-\033[m'*12)
print('{}{:^24}{}'.format('\033[1;31;40m', 'SUPER OFERTA DE 5%', '\033[m'))
print('\033[33m=-\033[m'*12)
P = float(input('Digite o preço: R$'))
D = P - (P * 5 / 100)
print('O preço com desconto de {}5%{} será {}R${:.2f}{}'.format('\033[1;31m', '\033[m',
      '\033[1;32m', D, '\033[m'))
