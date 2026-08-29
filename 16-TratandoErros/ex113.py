def leia_int(msg):
    """
    -> Input de números inteiros com validação.
    :param msg: Entrada da mensagem do input.
    :return: Retorna o valor digitado ou erro se for string.
    """
    print('\n' + '-' * 30)
    while True:
        try:
            n = int(input(msg))
            return n
        except (TypeError, ValueError):
            print('\033[1;31mErro! Digite um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não informar os date.\033[m')
            return 0

def leia_float(msg):
    """
    -> Input de números reais com validação.
    :param msg: Entrada da mensagem do input.
    :return: Retorna o valor digitado ou erro se for string.
    """
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
            return n
        except (TypeError, ValueError):
            print('\033[1;31mErro! Digite um valor real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não informar os date.\033[m')
            return 0

inteiro = leia_int('Digite um valor Inteiro: ')
real = leia_float('Digite um valor Real:')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
#help(leia_int)
