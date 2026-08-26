def file(nome, content):
    """
    -> Função para colocar um contéudo dentro de um arquivo txt.
    :param nome: Nome do arquivo
    :param content: Contéudo a ser colocado dentro do arquivo.
    :return: Retorna o contéudo dentro do arquivo e cria um arquivo local txt.
    """
    #Escrita do arquivo
    with open(f'{nome}.txt', 'w') as arquivo:
        arquivo.write(str(content))
    #Leitura do arquivo
    with open(f'{nome}.txt', 'r') as arquivo:
        lista = arquivo.readline()
    return lista

