from time import sleep
import json

def dict_to_list(dic1='', dic2='', file=''):
    """
    -> Essa função pega dois date de um dicionário e coloca em uma lista, para
    facilitar a manipulação, perguntando se o usuário deseja parar ou não.

    :param dic1: Nome do primeiro item do dicionário.
    :param dic2: Nome do segundo item do dicionário.
    :param file: Nome do arquivo a ser lido.
    :return: Ele retorna os date coletados do dic1 e dic2 dentro de uma lista,
    não havendo limite de coleta.
    """
    dados = list()
    # Leitura do arquivo em json
    try:
        with open(f'{file}.txt', 'r') as arquivo:
            dados = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = list()

    # Inserindo os date.
    while True:
        try:
            itens = dict()
            itens[dic1] = str(input(f'{dic1}: '))
            itens[dic2] = int(input(f'{dic2}: '))
            dados.append(itens.copy())

            while True:
                parador = str(input('Deseja continuar [S/N]? ')).upper()
                if parador not in ['S', 'N']:
                    print('\033[31mErro! só e permitido [S/N].\033[m')
                    continue
                break
            if parador == 'N':
                return dados

        except (ValueError, IndexError):
            sleep(3)
            print(f'\033[31mErro! tivemos problemas com o tipo do valor.')
            print('Coloque novamente os date.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mO usuário decidiu não informar os date.\033[m')
            return dados
