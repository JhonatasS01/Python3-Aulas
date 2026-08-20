numero = list()
pares = list()
impar = list()

while True:
    numero.append(int(input('Digite um valor: ')))
    parador = input('Deseja continuar [S/N]? ')
    if parador in 'Nn':
        break
for c, v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 ==1:
        impar.append(v)
print('-_' * 30)
print(f'Valores digitados: \033[1:32m{numero}\033[m')
print(f'Valores pares: \033[1:32m{pares}\033[m')
print(f'Valores ímpares: \033[1:32m{impar}\033[m')
