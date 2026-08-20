print('\033[33m=+\033[m'*14)
print('\033[1;34m{:^28}\033[m'.format('CONSULTE SEU FINANCIAMENTO'))
print('\033[33m=+\033[m'*14)
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos quer pagar? '))
percentual = 30 * salario / 100
S = casa / (anos * 12)
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}
if S > percentual:
    print('\nRESUMO DO EMPRÉSTIMO')
    print('\033[34mValor mensal:\033[m R${:.2f} (\033[31mmaior que 30% do salario\033[m)'.format(S))
    print('\033[34mSituação:\033[m \033[31mNEGADO\033[m')
else:
    print('\nRESUMO DO EMPRÉSTIMO')
    print('{}Situação:{} {}APROVADO{}'.format(cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))
    print('\033[34mValor mensal:\033[m R${:.2f}'.format(S))
    print('\033[34mParcelas:\033[m {}x'.format(anos * 12))
