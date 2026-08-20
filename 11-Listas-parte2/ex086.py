matriz = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite o valor [{l}, {c}]: ')))
print('=+' * 30)
print('\033[1;34m', end='')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')
print('\033[m')
