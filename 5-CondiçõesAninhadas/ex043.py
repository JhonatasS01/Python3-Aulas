peso = float(input('Digite seu peso [KG]: '))
altura = float(input('Digite sua altura [Metros]: '))
imc = peso / (altura ** 2)
print('-'*25)
print('IMC: {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[1;31mABAIXO DO PESO\033[m')
elif 18.5 <= imc < 25:
    print('\033[1;32mPESO IDEAL\033[m')
elif 25 <= imc < 30:
    print('\033[1;33mSOBREPESO\033[m')
elif 30 <= imc < 40:
    print('\033[1;33mOBESIDADE\033[m')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA\033[m')
print('-'*25)
