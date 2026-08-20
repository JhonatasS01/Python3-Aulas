from random import randint
njogadas = 0
print('-='*17)
print(f'{'VAMOS JOGAR PAR OU IMPAR':^33}')
print('-='*17)
while True:
    print('=' * 33)
    n = int(input('Escolha um número entre 0 e 10: '))
    while True:
        if 0 < n > 10:
            n = int(input('Tente novamente: '))
        else:
            jogada = str(input('Par ou Impar?: ')).upper().strip()
            while True:
                if jogada == 'PAR' or jogada == 'IMPAR':
                    break
                else:
                    jogada = str(input('Par ou Impar?: ')).upper().strip()
            njogadas += 1
            break
    PC = randint(0, 10)
    print(f'Computador jogou: {PC}\n')
    somador = PC + n
    resultado = somador % 2

    print('DEU PAR' if somador % 2 == 0 else 'DEU IMPAR')
    if jogada == 'PAR' and resultado == 0:
        print('\033[1;32mJogador ganhou!\033[m')
    elif jogada == 'IMPAR' and resultado == 1:
        print('\033[1;32mJogador ganhou!\033[m')
    else:
        print('\033[1;31mVocê Perdeu :(')
        print('Computador ganhou!\033[m')
        break
print('=' * 20)
print(f'Número de jogadas: {njogadas}')
