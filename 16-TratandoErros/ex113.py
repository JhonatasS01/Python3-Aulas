def leia_int(msg):
    """
    -> Input de números inteiros com validação se for string.
    :param msg: Entrada do valor númerico em forma de string.
    :return: Retorna o valor digitado ou erro se for string.
    """
    ok = False
    valor = 0
    print('\n' + '-' * 30)
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro, só e permitido números\033[m')
        if ok:
            break
    return valor

#program primary
num = leia_int('Digite um valor: ')
print(f'Você acabou de digitar o número {num}')
#help(leia_int)
