cont = soma = tot = 0
while cont != 999:
    N = int(input('Digite o número [999 para parar]: '))
    soma += N

    if N == 999:
        cont = 999
        soma -= 999
    else:
        cont += 1
        tot += 1
print('-'*30)
print(f'Foi digitado {tot} números')
print(f'A soma dos números foi: {soma}')
print('-'*30)
