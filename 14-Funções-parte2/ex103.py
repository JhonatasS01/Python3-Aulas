def ficha(jog='<desconhecido>', gol=0):
    """
    ->Mostra os date de um jogador organizado.
    :param jog: Nome do jogador.
    :param gol: Quantos gols ele fez.
    :return: Retorna os valores informados.
    """
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
#help(ficha)
