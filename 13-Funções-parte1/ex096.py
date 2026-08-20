def area(larg, comp):
    a = larg * comp
    print('-' * 30)
    print(f'Base: {larg}m\nAltura: {comp}m')
    print(f'Área e igual: {a}m²')

print('CONTROLE DE TERRENOS')
print('-' * 20)
l = float(input('Digite a largura [metros]: '))
c = float(input('Digite a comprimento [metros]: '))
area(l, c)
