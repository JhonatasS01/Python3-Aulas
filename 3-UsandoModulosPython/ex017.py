from math import hypot
A = float(input('Digite o cateto oposto: '))
B = float(input('Digite o cateto adjacente: '))
#a² + b² = c²
#C = sqrt(pow(A, 2) + pow(B, 2))
C = hypot(A, B)
print('A hipotenusa vai ser {:.2f}'.format(C))
