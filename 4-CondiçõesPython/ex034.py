salario = float(input('Digite seu salário: R$'))
if salario > 1250.00:
    perc = 10
    aument = salario + (salario * perc / 100)
else:
    perc = 15
    aument = salario + (salario * perc / 100)
print('O aumento foi {}%\nNovo salário: R${:.2f}'.format(perc, aument))
