def aumentar(n, fator):
    """
    -> Função para aumentar em porcentagens um valor informado.
    :param n: Valor a ser aumentado.
    :param fator: Porcentagem do aumento.
    :return: Retorna o valor inicial calculado com o aumento.
    """
    calc = n + (n * fator/100)
    return calc

def diminuir(n, fator):
    """
    -> Função para diminuir em porcentagens um valor informado.
    :param n: Valor a ser diminuido.
    :param fator: Porcentagem da diminuição.
    :return: Retorna o valor inicial calculado com a diminuição.
    """
    calc = n - (n * fator/100)
    return calc

def dobro(n):
    """
    -> Função para dobrar um valor informado.
    :param n: Valor a ser multiplicado por 2.
    :return: Retorna o valor em dobro.
    """
    calc = n * 2
    return calc

def metade(n):
    """
    -> Função para dividir em dois um valor informado.
    :param n: Valor a ser dividido por 2.
    :return: Retorna o valor dividido.
    """
    calc = n / 2
    return calc
