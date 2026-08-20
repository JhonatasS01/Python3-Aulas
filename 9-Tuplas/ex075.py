nove = valor = 0
num = (int(input('Digite o 1. Valor: ')),
       int(input('Digite o 2. Valor: ')),
       int(input('Digite o 3. Valor: ')),
       int(input('Digite o 4. Valor: ')))
print('-'*30)
print(f'Valores digitados:\n{num}')
print('-'*30)
print(f'Nove apareceu {num.count(9)} vezes.')
for c in num:
    if c == 3:
        valor += 1
if 3 in num:
    print(f'O valor 3 está na: {num.index(3) + 1}ª posição')
else:
    print('Nenhum valor igual a 3')
print('Números pares:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print('')
