D = float(input('Digite a distância da viagem (Km): '))
'''if D <= 200: #forma composta
    S = D * 0.50
    print('Viagens de ate 200Km\nO preço da viagem e R${:.2f}'.format(S))
else:
    S = D * 0.45
    print('Viagens longas com desconto!\nO preço da viagem e R${:.2f}'.format(S))'''
S = D * 0.50 if D <= 200 else D * 0.45 #forma simplificada
print('O preço da viagem e: R${}'.format(S))
