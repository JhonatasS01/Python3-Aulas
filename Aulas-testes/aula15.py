#interrompendo while com break
'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale \033[34m{s}\033[m')'''

#f-strings
nome = ('José')
idade = 24
salário = 1567.785
print(f'O {nome:-^20} tem {idade} anos e ganha {salário:.2f}')
