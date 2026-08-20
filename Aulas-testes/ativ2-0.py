from random import randint
print('-+'*15)
print('\033[1:34mAdivinhe um número de 1 a 10\033[m')
print('-+'*15)
jogador1 = tentativas = 0

pc = randint(1, 10)
while True:
    jogador1 = int(input('Digite o valor: '))
    tentativas += 1

    if jogador1 == pc:
        print('\n\033[1:32mVocê acertou!\033[m')
        break
    elif jogador1 > pc:
        print('\033[31mValor maior que o PC\033[m')
    elif jogador1 < pc:
        print('\033[31mValor menor que o PC\033[m')

print(f'Valor do computador: {pc}')
print(f'Tentativas: {tentativas}')
print('Fim do jogo')
