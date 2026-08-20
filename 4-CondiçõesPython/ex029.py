V = float(input('Digite a velocidade (Km/h): '))
if V > 80:
    print('Você foi multado!')
    S = (V - 80) * 7
    print('A multa e R${:.2f}'.format(S))
else:
    print('Você esta no limite\nSem Multas!')
