print('\033[0;34;40mOlá, Mundo!\033[m')
####
a = 5
b = 6
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
####
nome = 'Jhonatas'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá, prazer em te conhecer {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))
####
