from time import sleep
print('=+'*20)
print(f'{'BANCO JS':^40}')
print('=+'*20)
valor = int(input('Qual o valor a ser sacado: R$'))
conta = valor
print('Sacando dinheiro....')
sleep(2)
while True:
    div1 = valor // 50
    conta -= div1 * 50
    print(f'{div1} notas de R$50')
    sleep(2)
    if 0 < conta < 50 and conta > 19:
        div2 = conta // 20
        conta -= div2 * 20
        print(f'{div2} notas de R$20')
        sleep(2)
    if 0 < conta < 20 and conta > 9:
        div3 = conta // 10
        conta -= div3 * 10
        print(f'{div3} notas de R$10')
        sleep(2)
    if 0 < conta < 10:
        div4 = conta // 1
        conta -= div4 * 1
        print(f'{div4} moedas de R$1')
        sleep(2)
    break
print('-'*40)
print('Tenha um bom dia! :)')
