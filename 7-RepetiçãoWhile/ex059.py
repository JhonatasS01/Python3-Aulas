from time import sleep

n1 = int(input('\033[34m\nPrimeiro valor: \033[m'))
n2 = int(input('\033[34mSegundo valor: \033[m'))
sair = False
while not sair:
    print('''[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa''')
    opcao = int(input('\033[34mEscolha uma opção: \033[m'))
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} = {n1+n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} x {n2} = {n1*n2}')
    elif opcao == 3:
        maior = max(n1, n2)
        print(f'O maior valor e: {maior}')
    elif opcao == 4:
        n1 = int(input('\033[34m\nPrimeiro valor: \033[m'))
        n2 = int(input('\033[34mSegundo valor: \033[m'))
    elif opcao == 5:
        print('\nSaindo...')
        sleep(2)
        sair = True
    else:
        print('\n\033[1;31mOpção invalida! tente novamente.\033[m\n')
