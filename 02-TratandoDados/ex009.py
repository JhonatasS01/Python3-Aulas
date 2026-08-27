N = int(input('Digite um número inteiro: '))
cores = {'limpa' : '\033[m',
         'amarelo' : '\033[33m',
         'azul' : '\033[34m'}
print('\n{:11}\033[33m{}\033[m'.format('TABUADA DO', N))
print('='*14)
print('{}{}{}  X ''\033[33m 1\033[m'' = {}{:>3}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*1))
print('{}{}{}  X ''\033[33m 2\033[m'' = {}{:>3}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*2))
print('{}{}{}  X ''\033[33m 3\033[m'' = {}{:>3}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*3))
print('{}{}{}  X ''\033[33m 4\033[m'' = {}{:>3}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*4))
print('{}{}{}  X ''\033[33m 5\033[m'' = {}{:>3}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*5))
print('{}{}{}  X ''\033[33m 6\033[m'' = {}{:>3}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*6))
print('{}{}{}  X ''\033[33m 7\033[m'' = {}{:>3}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*7))
print('{}{}{}  X ''\033[33m 8\033[m'' = {}{:>3}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*8))
print('{}{}{}  X ''\033[33m 9\033[m'' = {}{:>3}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*9))
print('{}{}{}  X ''\033[33m10\033[m'' = {}{:>3}{}'.format(cores['amarelo'], N, cores['limpa'], cores['azul'], N*10, cores['limpa']))
print('='*14)
