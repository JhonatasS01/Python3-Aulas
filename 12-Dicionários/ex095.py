jogo = dict()
gols = list()
jogadores = list()

while True:
    #Coleta de dados
    jogo.clear()
    jogo['nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {jogo['nome']} jogou?: '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'  Quantos gols na partida {c+1}?: ')))
    jogo['gols'] = gols[:]
    jogo['total'] = sum(gols)
    jogadores.append(jogo.copy())
    while True:
        parador = str(input('Deseja continuar [S/N]?: ')).strip().upper()[0]
        if parador not in 'SN':
            print('Erro! caractere diferente de [S/N]')
        else:
            break
    if parador in 'N':
        break
#Tabela de dados
print()
print('-' * 40)
#Cabeçalho
print('Cod ', end='')
for i in jogo.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
#Tabela
for i, valor in enumerate(jogadores):
    print(f'{i:>3} ', end='')
    for dados in valor.values():
        print(f'{str(dados):<15}', end='')
    print()
#Levantamento de dados
while True:
    print('-' * 40)
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar == 999:
        break
    if mostrar >= len(jogadores):
        print(f'Erro! não existe jogador {mostrar}, tente novamente!')
    else:
        print(f'-- Levantamento do jogador {jogadores[mostrar]["nome"]}:')
        for i, valor in enumerate(jogadores[mostrar]['gols']):
            print(f'   No jogo {i+1} fez {valor} gols.')
print('<<  VOLTE SEMPRE  >>')
