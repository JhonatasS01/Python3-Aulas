#Interactive Help e Docstrings
"""def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = 1
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

print(contador.__doc__)
help(contador)
#Argumentos opcionais
def somar(a, b, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 3)
#escopo de variáveis
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()"""
#Retorno de resultados
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')
