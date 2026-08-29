import json

def file_json(nome, content):
    """
    -> Função para colocar um conteúdo dentro de um arquivo txt em formato json.
    :param nome: Nome do arquivo.
    :param content: Conteúdo obrigatório para colocar no arquivo.
    :return: Retorna o contéudo dentro do arquivo e cria um arquivo local txt.
    """
    #Escrita do arquivo sem apagar.
    with open(f'{nome}.txt', 'w') as arquivo:
        json.dump(content, arquivo, indent=4)
    return arquivo

def tabela(nome, file=''):
    """
    -> Criação da tabela com nome e idade.
    :param nome: Nome da tabela.
    :param file: Nome do arquivo a ser lido para a tabela.
    :return: Retorna todos os date formatado em uma tabela.
    """
    # Leitura do arquivo em json
    try:
        with open(f'{file}.txt', 'r') as arquivo:
            dados = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = list()
    # Criação da tabela
    cabecalho(nome)
    for valor in dados:
        print(f'{valor["Nome"]:<20}{valor["Idade"]:>10} anos')

def leia_int(msg):
    """
    -> Input de números inteiros com validação.
    :param msg: Entrada da mensagem do input.
    :return: Retorna o valor digitado ou erro se for string.
    """
    while True:
        try:
            n = int(input(msg))
            return n
        except (TypeError, ValueError):
            print('\033[1;31mErro! Digite um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não informar os dados.\033[m')
            return 0

def linha(tam=40):
    """
    -> Linha para separar titulos no ex115.
    :param tam: tamanho da linha para multiplicar pelo sinbolo '-'.
    :return: retorna o simbolo '-' multiplicado pelo tamanho, o padrão e 40.
    """
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leia_int('\033[33mSua Opção:\033[m ')
    return opc

'''def cores(cor, texto):
    """
    -> Função para cores para o ex115.
    :param cor: Só tem disponivel 2 cores 'amarelo' e 'azul' junto do 'limpar'.
    :param texto: Texto a ser colorido.
    :return: Retorna a cor definida apenas no texto informado.
    """
    coresp = {'amarelo': '\033[1;33m',
             'azul': '\033[1;34m',
             'limpar': '\033[m'
             }
    new = f'{coresp[cor]}{texto}{coresp["limpar"]}'
    return new'''
