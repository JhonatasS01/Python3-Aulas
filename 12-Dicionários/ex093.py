jogo = dict()
gols = list()

jogo['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {jogo['nome']} jogou?: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}?: ')))
jogo['gols'] = gols[:]
jogo['total'] = sum(gols)

print('+=' * 30)
print(jogo)
print('+=' * 30)
for chave, valor in jogo.items():
    print(f'{chave}: {valor}')
print('+=' * 30)
print(f'O jogador {jogo["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogo['gols']):
    print(f'  ==> Na partida {i+1}, fez {v} gols.')
print(f'Fez um total de {jogo["total"]} gols.')
