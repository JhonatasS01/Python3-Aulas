from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

print(numeros)
print(f'Maior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')
