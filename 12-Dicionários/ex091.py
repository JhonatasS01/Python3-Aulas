from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
ranking = list()

for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou: {v}')
    sleep(1)

print('-=' * 40)
print('  == Ranking dos jogadores ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking, start=1):
    print(f'    {i}.lugar: {v[0]} com {v[1]}')
    sleep(1)
