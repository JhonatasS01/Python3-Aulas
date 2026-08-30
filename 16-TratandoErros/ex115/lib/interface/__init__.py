def leia_int(msg):
    """
    -> Input de números inteiros com validação.
    :param msg: Entrada da mensagem do input.
    :return: Retorna o valor digitado ou erro se for string.
    """
    while True:
        try:
            n = int(input(msg))
            return n
        except (TypeError, ValueError):
            print('\033[1;31mErro! Digite um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não informar os dados.\033[m')
            return 0

def linha(tam=40):
    """
    -> Linha para separar titulos no deletar.
    :param tam: tamanho da linha para multiplicar pelo sinbolo '-'.
    :return: retorna o simbolo '-' multiplicado pelo tamanho, o padrão e 40.
    """
    return '-' * tam

def cabecalho(txt):
    """
    -> Cabeçalhos do ex115
    :param txt: Nome do cabeçalho.
    :return: Retorna o cabeçalho com o nome informado.
    """
    print(linha())
    print(txt.center(40))
    print(linha())

def menu(lista):
    """
    -> Menu do ex115
    :param lista: Lista de opções para o programa.
    :return: Retorna as opções informadas e a função leia_int para seleção.
    """
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cores("amarelo",c)} - {cores("azul", item)}')
        c += 1
    print(linha())
    opc = leia_int(f'{cores("verde", "Sua Opção: ")}')
    return opc

def cores(cor, texto):
    """
    -> Função para cores para o deletar.
    :param cor: Só tem disponivel 3 cores 'amarelo', 'azul' e 'verde' junto do 'limpar'.
    :param texto: Texto a ser colorido.
    :return: Retorna a cor definida apenas no texto informado.
    """
    coresp = {'amarelo': '\033[1;33m',
             'azul': '\033[1;34m',
              'verde': '\033[1;32m',
             'limpar': '\033[m'
             }
    new = f'{coresp[cor]}{texto}{coresp["limpar"]}'
    return new
