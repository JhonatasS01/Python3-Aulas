prox = 0
ante = 0
cont = 0
print('_'*30)
print('Sequência de Fibonacci ')
print('_'*30)

n = int(input('Digite o tamanho da sequência de fibonacci: '))
print('~'*50)
while cont < n:
    print(prox, end=' - ')
    prox += ante
    ante = prox - ante

    if prox == 0:
        prox += 1
    cont += 1
print('FIM')
print('~'*50)
