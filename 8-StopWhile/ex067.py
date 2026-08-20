c = 0
print(f'{'\033[1;33mGerador de Tabuadas\033[m':=^60}\n')
while True:
    print('-'*30)
    print('Para finalizar, digite um número negativo.')
    n = int(input('\033[34mEscolha a tabuada: \033[m'))
    print('-'* 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n}\033[1;34m X \033[m{c}\033[1;34m = \033[m{n * c}')
print('Gerador de tabuada finalizado...')
