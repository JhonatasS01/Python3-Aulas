from random import randint
def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))

def soma_par(valores):
    soma = 0
    print(f'Valores informados: {valores}')
    print('Valores pares: ', end='')
    for v in valores:
        if v % 2 == 0:
            print(v, end=' ')
            soma += v
    print(f'\nSoma dos valores pares: {soma}')


numeros = list()
sorteia(numeros)
soma_par(numeros)
