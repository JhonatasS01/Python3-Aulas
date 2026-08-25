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
            print('\033[1;31mErro! Tivemos problemas com o tipo do valor digitado.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não informar os dados.\033[m')

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
            print('\033[1;31mErro! Tivemos problemas com o tipo do valor digitado.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário preferiu não informar os dados.\033[m')

#Primary program
inteiro = leia_int('Digite um valor Inteiro: ')
real = leia_float('Digite um valor Real:')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
#help(leia_int)
