from random import randint
from time import sleep

print('\033[33m=+\033[m'*12)
print('\033[34m{:^23}\033[m'.format('JOKENPÔ'))
print('\033[33m=+\033[m'*12)
itens = ['Pedra', 'Papel', 'Tesoura']
print('''Escolha uma jogada
[0] \033[34mPedra\033[m
[1] \033[34mPapel\033[m
[2] \033[34mTesoura\033[m''')
#jogada do player
J = int(input('Digite uma opção: '))
# jogada do computador
PC = randint(0, 2)
if J > 2:
    print('\n\033[1;31mJogada Invalida! Tente Novamente.\033[m')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-=' * 12)
    print('\033[36mJogador:\033[m {}'.format(itens[J]))
    print('\033[35mComputador:\033[m {}'.format(itens[PC]))
    print('-=' * 12)
    # analise do vencedor
    sleep(1)
    if J == 0 and PC == 1:
        print('\n\033[1;31mComputador Ganhou!\033[m')
    elif J == 1 and PC == 2:
        print('\n\033[1;31mComputador Ganhou!\033[m')
    elif J == 2 and PC == 0:
        print('\n\033[1;31mComputador Ganhou!\033[m')
    elif J == PC:
        print('\n\033[1;33mEmpate!\033[m')
    else:
        print('\n\033[1;32mJogador ganhou!\033[m')
    sleep(2)
    print('FIM DE JOGO...')
