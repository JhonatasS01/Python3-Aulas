from random import randint
from time import sleep
print('-' * 30)
print(f"{" JOGA NA MEGA SENA ":^30}")
print('-' * 30)

sorteio = list()
numeros = list()

jogos = int(input('Quantos jogos você que sortear? '))
for c in range(0, jogos):
    while len(numeros) < 6:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
    numeros.sort()
    sorteio.append(numeros[:])
    numeros.clear()

print(f"{" SORTEANDO " + str(jogos) + " JOGOS ":=^30}")
sleep(1)
for c in range(0, jogos):
    print(f'Jogo {c + 1}: {sorteio[c]}')
    sleep(1)
print(f"{" BOA SORTE! ":=^30}")
