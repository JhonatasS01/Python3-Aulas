valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        valores.sort()
        print(f'\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[1;31mEste valor já existe! Tente novamente.\033[m')

    parador = input('Deseja continuar [S/N]? ').strip()
    if parador in 'Nn':
        break

print(f'Valores digitados:\n{valores}')
