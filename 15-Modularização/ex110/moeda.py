def aumentar(n = 0, fator = 0, form = False):
    """
    -> Função para aumentar em porcentagens um valor informado.
    :param form: Adicionar ou não a formatação monetária.
    :param n: Valor a ser aumentado.
    :param fator: Porcentagem do aumento.
    :return: Retorna o valor inicial calculado com o aumento.
    """
    calc = n + (n * fator/100)
    return calc if not form else moeda(calc)

def diminuir(n = 0, fator = 0, form = False):
    """
    -> Função para diminuir em porcentagens um valor informado.
    :param form: Adicionar ou não a formatação monetária.
    :param n: Valor a ser diminuido.
    :param fator: Porcentagem da diminuição.
    :return: Retorna o valor inicial calculado com a diminuição.
    """
    calc = n - (n * fator/100)
    return calc if not form else moeda(calc)

def dobro(n = 0, form = False):
    """
    -> Função para dobrar um valor informado.
    :param form: Adicionar ou não a formatação monetária.
    :param n: Valor a ser multiplicado por 2.
    :return: Retorna o valor em dobro.
    """
    calc = n * 2
    return calc if not form else moeda(calc)

def metade(n = 0, form = False):
    """
    -> Função para dividir em dois um valor informado.
    :param form: Adicionar ou não a formatação monetária.
    :param n: Valor a ser dividido por 2.
    :return: Retorna o valor dividido.
    """
    calc = n / 2
    return calc if not form else moeda(calc)

def moeda(dinheiro: float = 0, moedas = 'R$'):
    """
    -> Função para adicionar valor monetario em reais(R$).
    :param moedas: (Opcional) informar a moeda, o padrão e reais(R$).
    :param dinheiro: Valor a ser formatado.
    :return: Retorna o valor formatado em reais.
    """
    return f'{moedas}{dinheiro:>.2f}'.replace('.', ',')

def resumo(n, aumento, reducao):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aumento}% de aumento: {aumentar(n, aumento, True)!s:>12}')
    print(f'{reducao}% de redução: {diminuir(n, reducao, True)!s:>12}')
    print('-' * 30)
