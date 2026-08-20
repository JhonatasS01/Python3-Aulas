from random import randint
from time import sleep

# Faz o computador sortear o número entre 0 e 10
N = randint(0, 10)
print('='*25)
print('\033[1;34mADVINHE O NÚMERO SORTEADO\033[m')
print('='*25)

acertou = False
palpites = 0
# Jogador tenta adivinhar
while not acertou:
    R = int(input('\033[34mEscolha entre\033[m 0 \033[34me\033[m 10\033[34m:\033[m '))
    palpites += 1
    print('PROCESSANDO...')
    sleep(1)
    if R == N:
        print('\033[1;32mVocê acertou! PARABÉNS!\033[m')
        acertou = True
    else:
        if R > N:
            print('\033[1;31mMenos... Tente novamente!\033[m')
        elif R < N:
            print('\033[1;31mMais... Tente novamente!\033[m')
# Resultado
print('-'*24)
print(f'\033[34mNúmero sorteado:\033[m {N}')
print(f'\033[34mTentativas:\033[m {palpites}')
print('-'*24)
