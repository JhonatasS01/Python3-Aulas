media = 0
maior = 0
idadeM = 0
nomeh = ''
for c in range(1, 5):
    print(f'\033[34m----- {c}ª PESSOA -----\033[m')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    print('''Escolha o sexo
[1] Homem
[2] Mulher''')
    sexo = int(input('Digite uma opção: '))
    #média de idade do grupo
    media += idade
    #nome do homem mais velho
    if sexo == 1 and idade > maior:
        maior = idade
        nomeh = nome
    #mulheres menos de 20 anos
    if sexo == 2 and idade < 20:
        idadeM = idadeM + 1
print('-'*40)
print('\033[34mA média de idade do grupo é:\033[m {:.2f} anos'.format(media/4))
if maior != 0:
    print(f'\033[34mO homem mais velho tem \033[m{maior}\033[34m anos e se chama:\033[m {nomeh}')
else:
    print('\033[34mNão há homens no grupo\033[m')
print(f'\033[34mMulheres com menos de 20 anos:\033[m {idadeM}')
