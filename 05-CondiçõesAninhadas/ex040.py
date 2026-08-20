n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Média: \033[31m{:.1f}\033[m'.format(m))
    print('Situação: \033[31mREPROVADO\033[m')
elif m >= 5 and m <= 6.9:
    print('Média: \033[33m{:.1f}\033[m'.format(m))
    print('Situação: \033[33mRECUPERAÇÃO\033[m')
else:
    print('Média: \033[32m{:.1f}\033[m'.format(m))
    print('Situação: \033[32mAPROVADO\033[m')
