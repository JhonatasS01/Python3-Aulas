from time import sleep

def logo(txt):
    """
    -> Adiciona bordas para usar em títulos.
    :param txt: Título do programa.
    :return: Retorna o título com as bordas personalizada.
    """
    print('~' * (len(txt) + 6))
    print(f'   {txt}')
    print('~' * (len(txt) + 6))

def color(txt, fundo):
    """
    -> Cores de fundo para os títulos do programa.
    :param txt: Texto do título ou '' para adicionar por cima se o texto não estiver disponivel.
    :param fundo: O nome da cor use:
    'branco', 'vermelho', 'verde', 'amarelo', 'azul', 'roxo', 'azul claro', 'cinza', 'limpar'.
    :return: Retorna as cores no texto informado.
    """
    coresf = {
        'branco' : '\033[40m',
        'vermelho' : '\033[41m',
        'verde' : '\033[42m',
        'amarelo' : '\033[43m',
        'azul' : '\033[44m',
        'roxo' : '\033[45m',
        'azul claro' : '\033[46m',
        'cinza' : '\033[47m',
        'limpar' : '\033[0m'
    }
    c_inicio = coresf.get(fundo.lower(), '\033[0m')

    return f"{c_inicio}{txt}"

def pyhelp(active=True):
    """
    -> Ajuda interativa com base no interactive help do python.
    :param active: Ele ja inicia automaticamente, basta colocar 'pyhelp()' no terminal.
    :return: Ele retorna um painel interativo do 'help()', basta escrever 'fim' que o programa e finalizado.
    """
    while active:
        print(color('', 'verde'), end='')
        logo('Sistema de Ajuda PyHelp')

        valor = str(input('\033[mFunção ou Biblioteca > '))
        if valor == 'fim':
            print(color('', 'vermelho'), end='')
            logo('Ate Logo!')
            print('\033[0m', end='')
            break

        print(color('', 'azul'), end='')
        logo(f'Acessando o manual do comando: {valor}')
        sleep(1)
        print(color('', 'cinza'), end='')
        help(valor)


pyhelp()
