'''num = [2, 5, 9, 1]
num[2] = 8
num.append(7)
num.sort(reverse=True)
num.insert(3, 10)
#removendo com pop()
#num.pop(4)
#removendo por elementos com .remove()
if 11 in num:
    num.remove(11)
else:
    print('Não achei o número 11')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''
from time import sleep

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

#valores.append(5)
#valores.append(8)
#valores.append(10)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
    sleep(2)
print('Cheguei ao final da lista.')

'''a = [2, 4, 8, 7]
b = a[:]
b[2] = 10
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
