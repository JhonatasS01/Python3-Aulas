print('\033[34mPRIMEIRO NOME EM MAIUSCULAS\033[m')
print('\033[33m-+\033[m'*14)

nome = str(input('Qual e o seu nome? ')).strip().upper().split()
idade = int(input('Qual a sua idade? '))
print(f'Olá {nome[0]}, ', end='')
if idade < 18:
    print('Você e de menor')
elif idade < 60:
    print('Você e de maior')
else:
    print('Você esta na categoria de idoso')
print(f'Idade: {idade}')
