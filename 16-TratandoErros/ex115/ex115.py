from time import sleep
from date import dict_to_list
from tools import *

while True:
    # ----- Impressão do menu de opções -----
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])

    #------ Validação de opções ------
    if opcao == 1:
        # Chamando a função tabela.
        tabela(
            'PESSOAS CADASTRADAS',
            'pessoas'
        )
    elif opcao == 2:
        cabecalho('NOVO CADASTRO')
        # Informando o nome dos dicionarios
        dados = dict_to_list(
            'Nome',
            'Idade',
            'pessoas'
        )
        # Criando um arquivo txt com nome pessoas.
        file_json(
            'pessoas', dados
        )
    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(3)
        break
    else:
        print(f'\033[31mErro! "{opcao}" e um valor inválido, tente novamente\033[m')
    sleep(2)
