print('-='*13)
print('Analisador de Triângulos')
print('-='*13)
A = float(input('Lado a: '))
B = float(input('Lado b: '))
C = float(input('Lado c: '))
maior = max(A, B, C)
menores = (A + B + C) - maior
if maior < menores:
    print('O lado A:{:.1f} + B:{:.1f} + C:{:.1f}\nE um triângulo!'.format(A, B, C))
else:
    print('O lado A:{:.1f} + B:{:.1f} + C:{:.1f}\nNão e um triângulo!'.format(A, B, C))
