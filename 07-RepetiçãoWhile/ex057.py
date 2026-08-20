'''n = 1
while n != 0:
    r = str(input('Digite seu sexo [M/F] ')).upper()[0].strip()
    if r == 'M' or r == 'F':
        n = 0
    else:
        print('Opção invalida! tente novamente.')
        n += 1
print(f'Sexo {r} registrado com sucesso!')'''

sexo = str(input('Digite seu sexo [M/F] ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')