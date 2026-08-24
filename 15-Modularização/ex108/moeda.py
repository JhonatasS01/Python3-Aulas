def aumentar(n = 0, fator = 0):
    """
    -> Função para aumentar em porcentagens um valor informado.
    :param n: Valor a ser aumentado.
    :param fator: Porcentagem do aumento.
    :return: Retorna o valor inicial calculado com o aumento.
    """
    calc = n + (n * fator/100)
    return calc

def diminuir(n = 0, fator = 0):
    """
    -> Função para diminuir em porcentagens um valor informado.
    :param n: Valor a ser diminuido.
    :param fator: Porcentagem da diminuição.
    :return: Retorna o valor inicial calculado com a diminuição.
    """
    calc = n - (n * fator/100)
    return calc

def dobro(n = 0):
    """
    -> Função para dobrar um valor informado.
    :param n: Valor a ser multiplicado por 2.
    :return: Retorna o valor em dobro.
    """
    calc = n * 2
    return calc

def metade(n = 0):
    """
    -> Função para dividir em dois um valor informado.
    :param n: Valor a ser dividido por 2.
    :return: Retorna o valor dividido.
    """
    calc = n / 2
    return calc

def moeda(dinheiro = 0, moedas = 'R$'):
    """
    -> Função para adicionar valor monetario em reais(R$).
    :param moedas: (Opcional) informar a moeda, o padrão e reais(R$).
    :param dinheiro: Valor a ser formatado.
    :return: Retorna o valor formatado em reais.
    """
    return f'{moedas}{dinheiro:>.2f}'.replace('.', ',')
