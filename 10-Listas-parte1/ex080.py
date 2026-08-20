num = list()
cont = posicao = 0

for cont in range(0, 5):
    valor = (int(input('Digite um valor: ')))
    if not num or valor >= num[-1]:
        num.append(valor)
        print('Valor adicionado ao final da lista...')
    else:
        while posicao < len(num):
            if valor <= num[posicao]:
                num.insert(posicao, valor)
                print(f'Valor adicionado na posição {posicao}...')
                break
            posicao += 1
print(f'\nVocê digitou os valores: {num}')
