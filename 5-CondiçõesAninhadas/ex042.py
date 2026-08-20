print('\033[33m-=\033[m'*13)
print('\033[34m{:^26}\033[m'.format('Analisador de Triângulos'))
print('\033[33m-=\033[m'*13)
a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))
maior = max(a, b, c)
menores = (a + b + c) - maior
print('\nO lado A = {:.1f} + B = {:.1f} + C = {:.1f}'.format(a, b, c))
if maior < menores:
    print('\033[32mE um triângulo!\033[m')
    if a == b == c:
        print('Tipo: \033[34mEQUILÁTERO\033[m')
    elif a != b != c != a:
        print('Tipo: \033[34mESCALENO\033[m')
    else:
        print('Tipo: \033[34mISÓSCELES\033[m')
else:
    print('\033[31mNão e triângulo!\033[m')
