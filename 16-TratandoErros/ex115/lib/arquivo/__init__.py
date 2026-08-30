from ex115.lib.interface import *

def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def arq_create(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except OSError:
        print('Erro! houve um problema ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def arq_writer(nome):
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
