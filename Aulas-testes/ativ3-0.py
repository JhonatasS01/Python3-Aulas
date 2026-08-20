numeros = list()
valor = 0

while True:
    valor = (int(input('Digite um número: ')))
    if valor not in numeros:
        numeros.append(valor)
        numeros.sort()
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado não pode ser adicionado!\033[m')

    parador = str(input('Deseja continuar? [S/N] ')).strip()
    if parador in 'Nn':
        break
print(f'\nVocê digitou os valores: {numeros}')
