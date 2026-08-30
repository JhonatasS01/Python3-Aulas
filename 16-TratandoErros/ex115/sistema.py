from time import sleep
from lib.arquivo import *
from lib.interface import *

arq = 'pessoas.txt'

if not arq_existe(arq):
    arq_create(arq)

while True:
    # ----- Impressão do menu de opções -----
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])

    #------ Validação de opções ------
    if opcao == 1:
        # Listando conteúdo de um arquivo
        arq_writer(arq)
    elif opcao == 2:
        # Cadastro de uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break
    else:
        print(f'\033[31mErro! "{opcao}" e um valor inválido, tente novamente\033[m')
    sleep(1)
