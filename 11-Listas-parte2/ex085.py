numeros = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}.valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 == 1:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('=+' * 30)
print(f'Os valores pares são: {numeros[0]}')
print(f'Os valores ímpares são: {numeros[1]}')
