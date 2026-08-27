from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print('Idade: {}'.format(idade))
if idade >= 1 and idade <= 9:
    print('Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Categoria: SÊNIOR')
elif idade > 25 and idade <= 100:
    print('Categoria: MASTER')
else:
    print('\033[31mIdade Invalida! Tente novamente.\033[m')
