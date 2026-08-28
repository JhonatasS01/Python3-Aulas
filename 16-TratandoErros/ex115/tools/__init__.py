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
    :return: Retorna todos os dados formatado em uma tabela.
    """
    # Leitura do arquivo em json
    try:
        with open(f'{file}.txt', 'r') as arquivo:
            dados = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = list()
    # Criação da tabela
    print('-' * 40)
    print(nome.center(40))
    print('-' * 40)
    for valor in dados:
        print(f'{valor["Nome"]:<20}{valor["Idade"]:>10} anos')

def linha(tamanho=0):
    """
    -> Linha para separar titulos no ex115.
    :param tamanho: tamanho da linha para multiplicar pelo sinbolo '-'.
    :return: retorna o simbolo '-' multiplicado pelo tamanho informado.
    """
    print('-' * tamanho)

def cores(cor, texto):
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
    return new
