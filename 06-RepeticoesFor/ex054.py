from datetime import date
anoatual = date.today().year
menor = 0
maior = 0

for C in range(1, 8):
    print(f'\033[34m{C}. pessoa\033[m')
    ano = int(input('Digite seu ano de nascimento: '))
    idade = anoatual - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
#avaliação das pessoas
print(f'\nPessoas maiores de idade: \033[1;32m{maior}\033[m')
print(f'Pessoas menores de idade: \033[1;31m{menor}\033[m')
