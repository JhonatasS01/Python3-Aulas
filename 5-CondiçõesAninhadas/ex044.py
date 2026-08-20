from time import sleep

print('{:=^40}'.format('LOJAS BEMOL'))
preco = float(input('\nDigite o preço das compras: R$'))
print('\033[1;33mEscolha a forma de pagamento\033[m \n1- Á vista (\033[34mPIX\033[m)\n2- Parcelado')
E = int(input('Digite uma opção: '))
print('-' * 30)
if E == 1:
    D = 10 * preco / 100
    print('\033[32mDesconto de 10% aplicado!\033[m')
    print('Valor do produto: \033[1;32mR${:.2f}\033[m'.format(preco-D))
elif E == 2:
    avista = 5 * preco / 100
    juros = 20 * preco / 100
    print('\033[1;33mEscolha as parcelas\033[m \n1x {:.2f} \033[1;32;40m(Desconto de 5%)\033[m\n2x {:.2f} \n3x ou mais'.format(preco-avista, preco/2))
    E = int(input('Digite uma opção: '))
    print('-' * 30)
    if E == 1:
        sleep(2)
        print('\033[32mDesconto de 5% aplicado!\033[m')
        print('Valor do produto: \033[1;32mR${:.2f}\033[m'.format(preco-avista))
    elif E == 2:
        sleep(2)
        print('2x {} sem juros'.format(preco/2))
        print('Valor do produto: \033[1;32mR${:.2f}\033[m'.format(preco))
    elif E == 3:
        sleep(2)
        parcelas = int(input('Quantas parcelas (limitado a 12x)? '))
        if 3 <= parcelas <= 12:
            sleep(2)
            print('{}x {:.2f} com juros'.format(parcelas, (preco + juros)/parcelas))
            print('Valor do produto: \033[1;32mR${:.2f}\033[m'.format(preco + juros))
        else:
            print('\033[31mSó e permitido parcelar até 12x! \ntente novamente.\033[m')
    else:
        sleep(3)
        print('\033[31mOpção invalida! tente novamente.\033[m')
else:
    print('\033[31mOpção invalida! tente novamente.\033[m')
print('-' * 30)
