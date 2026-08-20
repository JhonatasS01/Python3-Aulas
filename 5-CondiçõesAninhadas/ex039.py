import datetime
print('\033[33m=+\033[m'*18)
print('\033[1;32;40m{:^34}\033[m'.format('ALISTAMENTO MILITAR'))
print('\033[33m=+\033[m'*18)
ano = int(input('\nQual seu ano de nascimento? '))
anoatual = datetime.datetime.now()
idade = anoatual.year - ano
print('-'*35)
if idade == 18:
    print('\033[1;32mVocê já pode se alistar!\033[m')
    print('Idade atual: {}'.format(idade))
elif idade < 18:
    falta = 18 - idade
    print('\033[1;34mVocê ainda não pode se alistar!\033[m')
    print('Você tem {} anos, falta {} anos!'.format(idade, falta))
    print('Seu alistamento será em {}'.format(anoatual.year + falta))
else:
    print('\033[1;31mJá passou da idade de se alistar!\033[m')
    print('Você tem {} anos, e passou {} anos!'.format(idade, idade-18))
    print('''\n\033[33mPor isso devera pagar uma multa, 
consulte o site para mais informações,\033[m
\033[1;33mOu desconsidere caso já tenha se
apresentado.\033[m''')
print('-'*35)
