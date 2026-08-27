def file(nome, content):
    """
    -> Função para colocar um contéudo dentro de um arquivo txt.
    :param nome: Nome do arquivo
    :param content: Contéudo a ser colocado dentro do arquivo.
    :return: Retorna o contéudo dentro do arquivo e cria um arquivo local txt.
    """
    #Escrita do arquivo sem apagar
    #Escrita temporaria: w
    with open(f'{nome}.txt', 'a') as arquivo:
        arquivo.write(str(content))
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
    for indice, valor in enumerate(content):
        print(f'{content[indice]["Nome"]:<20}{content[indice]["Idade"]:>10} anos')
