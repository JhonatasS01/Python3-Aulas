def leia_dinheiro(msg):
    """
    -> Função para validar se um valor digitado e monetário ou não.
    :param msg: Ler o valor digitado pelo usuário.
    :return: Retorna apenas se o valor monetário estiver correto, se não aparece erro na tela.
    """
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[1;31mErro! "{valor}" é um preço inválido.\033[m')
        else:
            return float(valor)
