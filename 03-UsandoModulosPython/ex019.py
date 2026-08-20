from random import choice
n1 = str(input('1.aluno: '))
n2 = str(input('2.aluno: '))
n3 = str(input('3.aluno: '))
n4 = str(input('4.aluno: '))
Nomes = [n1, n2, n3, n4]
Escolhido = choice(Nomes)
print('\nO escolhido foi: {}'.format(Escolhido))
