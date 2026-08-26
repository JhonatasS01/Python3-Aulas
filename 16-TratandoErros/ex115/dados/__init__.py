def dict_to_list(dic1='', dic2=''):
    from time import sleep
    """
    -> Essa função pega dois dados de um dicionário e coloca em uma lista, para
    facilitar a manipulação, perguntando se o usuário deseja parar ou não.

    :param dic1: Nome do primeiro item do dicionário.
    :param dic2: Nome do segundo item do dicionário.
    :return: Ele retorna os dados coletados do dic1 e dic2 dentro de uma lista,
    não havendo limite de coleta.
    """
    itens = dict()
    dados = list()

    while True:
        try:
            itens[dic1] = str(input(f'{dic1}: '))
            itens[dic2] = int(input(f'{dic2}: '))
            dados.append(itens.copy())

            parador = str(input('Deseja continuar [S/N]? ')).strip().upper()
            if parador in 'N':
                return dados
        except (ValueError, IndexError):
            sleep(3)
            print(f'\033[31mErro! tivemos problemas com o tipo do valor.')
            print('Coloque novamente os dados.\033[m')
        except KeyboardInterrupt:
            print(f'O usuário decidiu não informar os dados.')

