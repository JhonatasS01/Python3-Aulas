temp = list()
dados = list()
pesomax = pesomin = 0

while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    if len(dados) == 0:
        pesomax = pesomin = temp[1]
    else:
        if temp[1] > pesomax:
            pesomax = temp[1]
        if temp[1] < pesomin:
            pesomin = temp[1]
    dados.append(temp[:])
    temp.clear()

    parador = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if parador == 'N':
        break
'''pesomax = max(date, key=lambda x: x[1])
pesomin = min(date, key=lambda x: x[1])'''
print('=+' * 30)
print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'A pessoa mais pesada foi {pesomax}Kg de ', end='')
for p in dados:
    if p[1] == pesomax:
        print(f'[{p[0]}] ', end='')
print()
print(f'A pessoa mais leve foi {pesomin}Kg de ', end='')
for p in dados:
    if p[1] == pesomin:
        print(f'[{p[0]}] ', end='')
print()
