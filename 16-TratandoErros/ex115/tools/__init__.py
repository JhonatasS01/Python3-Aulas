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

def tabela(nome, content):
    """
    -> Criação da tabela com nome e idade.
    :param nome: Nome da tabela.
    :param content: Dados como nome e idade para a tabela.
    :return: Retorna todos os dados formatado em uma tabela.
    """
    print('-' * 40)
    print(nome.center(40))
    print('-' * 40)
    for valor in content:
        print(f'{valor["Nome"]:<20}{valor["Idade"]:>10} anos')
