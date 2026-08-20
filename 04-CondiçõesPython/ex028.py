from random import randint
from time import sleep
N = randint(1, 5) # Faz o computador sortear o número entre 0 e 5
print('='*25)
print('ADVINHE O NÚMERO SORTEADO')
print('='*25)
R = int(input('Escolha entre 1 e 5: ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if R == N:
    print('Você acertou!\nPARABÉNS!')
else:
    print('Você errou!\nQUE PENA :(')
print('-'*20)
print('Número sorteado: {}'.format(N))
print('-'*20)
