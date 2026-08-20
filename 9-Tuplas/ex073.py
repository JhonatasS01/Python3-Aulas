brasileirão = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol',
               'Fluminense', 'Bahia', 'Botafogo', 'São Paulo',
               'Bragantino', 'Corinthians', 'Grêmio', 'Vasco da Gama',
               'Atlético-MG', 'Santos', 'Ceará SC', 'Fortaleza',
               'EC Vitória', 'Internacional', 'Juventude', 'Sport Recife')

print('-=' * 15)
print(f'\033[34mLista brasileirão:\033[m {brasileirão}')
print('-=' * 15)
print(f'\033[34mOs 5 primeiros colocados:\033[m {brasileirão[0:5]}')
print('-=' * 15)
print(f'\033[34mOs 4 ultimos colocados:\033[m {brasileirão[-4:]}')
print('-=' * 15)
print(f'\033[34mOrdem alfabética:\033[m {sorted(brasileirão)}')
print('-=' * 15)
print(f'O corinthians está na \033[34m{brasileirão.index('Corinthians')+1}ª\033[m posição')
