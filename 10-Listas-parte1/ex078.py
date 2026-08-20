num = []
mai = men = 0
for C in range(0, 5):
    num.append(int(input(f'Digite um valor na posição {C}: ')))
    if C == 0:
        mai = men = num[C]
    else:
        if num[C] > mai:
            mai = num[C]
        if num[C] < men:
            men = num[C]
print('-' * 30)
print(f'Valores digitados:\n{num}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}... ', end='')
print()
