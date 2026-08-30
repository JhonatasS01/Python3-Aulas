from ex115.lib.interface import *

def arq_existe(nome):
    """
    -> Função para verificar se o arquivo do ex115 existe ou não.
    :param nome: Nome do arquivo.
    :return: Retorna False ou True.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def arq_create(nome):
    """
    -> Função para criar o arquivo do ex115.
    :param nome: Nome do arquivo a ser criado.
    :return: Retorna o arquivo.txt na raiz do projeto.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except OSError:
        print('Erro! houve um problema ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def arq_writer(nome):
    """
    -> Função para ler o arquivo do ex115.
    :param nome: Nome do arquivo a ser lido.
    :return: Retorna os dados do arquivo com o cabeçalho formatado.
    """
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('Erro! falha ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linhas in a:
            dado = linhas.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

def cadastrar(arq, nome='desconhecido', idade=0):
    """
    -> Função para cadastrar as pessoas no arquivo do ex115.
    :param arq: Arquivo para ser feito o cadastro.
    :param nome: Nome da pessoa.
    :param idade: Idade da pessoa.
    :return: Retorna uma mensagem da situação do cadastro.
    """
    try:
        a = open(arq, 'at')
    except FileNotFoundError:
        print('Erro! houve um problema na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except FileNotFoundError:
            print('Erro! houve um problema ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
