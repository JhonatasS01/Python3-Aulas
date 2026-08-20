from math import radians, sin, cos, tan
An = float(input('Digite o ângulo: '))
Radi = radians(An)
print('\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(Radi), cos(Radi), tan(Radi)))
