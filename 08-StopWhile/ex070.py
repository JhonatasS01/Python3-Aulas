total = pmaior = menor = 0
nmenor = ''
print(f'{'Mercado do João':-^30}')
while True:
    print('='*30)
    #Coleta de date
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço: R$'))
    #Valor total
    total += preco
    #Maior que R$1000
    if preco > 1000:
        pmaior += 1
    #Produto mais barato
    if menor == 0 or preco < menor:
        menor = preco
        nmenor = nome
    #Condição de parada
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while True:
        if cont not in ('S', 'N'):
            print('\033[31mOpção invalida! Tente novamente.\033[m')
            cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        else:
            break
    if cont == 'N':
        break
print('='*30)
print('DADOS DA COMPRA:')
print(f'Total da compra: R${total:.2f}')
print(f'Produtos maior que R$1000: {pmaior}')
print(f'O produto mais barato foi: {nmenor} no valor de R${menor:.2f}')
