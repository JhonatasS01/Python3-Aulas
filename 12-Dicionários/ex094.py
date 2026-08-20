pessoas = dict()
dados = list()
media = 0

while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas["sexo"] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoas["sexo"] not in 'MF':
            print('Erro! caractere diferente de [M/F]')
        else:
            break
    pessoas['idade'] = int(input('Idade: '))
    media += pessoas['idade']
    dados.append(pessoas.copy())
    pessoas.clear()

    while True:
        parador = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if parador not in 'SN':
            print('Erro! caractere diferente de [S/N]')
        else:
            break
    if parador in 'N':
        break
print('+=' * 30)
print(f'- O grupo tem {len(dados)} pessoas.')
print(f'- A média de idade e {media/len(dados):.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'[{p["nome"]}]', end=' ')
print('\n- Lista das pessoas acima da média:')
for p in dados:
    if p["idade"] >= media/len(dados):
        for chave, valor in p.items():
            print(f'{chave}: {valor}; ', end='')
        print()
print('<< ENCERRADO >>')
