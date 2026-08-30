maioridade = homens = mulheridade = 0
print('-'*25)
print(f'{'CADASTRO DE PESSOAS':^25}')
print('-'*25)
while True:
    print('='*25)
    #Coletando idade
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        maioridade += 1
    #Coletando arquivo do sexo
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheridade += 1
    #Condição de parada
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while True:
        if cont not in 'SN':
            print('\033[31mOpção Invalida! Tente Novamente.\033[m')
            cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        else:
            break
    if cont == 'N':
        break
print('='*25)
print('DADOS CADASTRADOS:')
print(f'Pessoas maiores de 18 anos: {maioridade}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres menores de 20 anos: {mulheridade}')
