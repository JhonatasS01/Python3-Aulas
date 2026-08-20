from time import sleep
def contador(i, f, p):
    # Ajuste de erro se o passo for igual a 0
    if p == 0:
        p = 1
    # Adicionando negativo se o inicio for maior que o final
    if i > f and p > 0:
        p = -p
    elif i < f and p < 0:
        p = -p
    print('=-' * 20)
    print(f'Contando de {i} até {f} de {p} em {p}')
    #Ajuste do valor final faltando no passo positivo e negativo
    if p > 0:
        fimajuste = f + 1
    else:
        fimajuste = f - 1
    #Imprimindo na tela
    for c in range(i, fimajuste, p):
        print(f'{c} ', end='')
        sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 20)
print('Agora e sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
contador(inicio, final, passo)
