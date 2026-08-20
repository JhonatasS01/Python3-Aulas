numeros = list()
contador = 0

while True:
    numeros.append(int(input('Digite um valor: ')))
    contador += 1
    numeros.sort(reverse=True)

    parador = input('Deseja continuar [S/N]? ')
    if parador in 'Nn':
        break
print('-+' * 30)
print(f'Foram digitados {contador} números...')
print(numeros)
if 5 in numeros:
    print('\033[1:32mO número 5 esta presente na lista!\033[m')
else:
    print('\033[1:31mO número 5 não esta presente na lista!\033[m')
