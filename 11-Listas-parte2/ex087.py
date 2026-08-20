matriz = [[], [], []]
pares = soma3 = maxl2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite o valor [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][2]
        if l == 1:
            maxl2 = max(matriz[1])
print('=+' * 30)
print('\033[1;34m', end='')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l][c]:^5}]', end='')
    print()
print('\033[m', end='')
print('=+' * 30)
print(f'A soma dos valores pares foi: {pares}\n'
      f'A soma dos valores da terceira coluna: {soma3}\n'
      f'O maior valor da segunda linha foi: {maxl2}')
