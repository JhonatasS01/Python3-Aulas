from time import sleep
from dados import dict_to_list
from tools import linha, cores, tabela, file_json

while True:
    # ----- Impressão do menu de opções -----
    opcao = 0
    linha(40)
    print('MENU PRINCIPAL'.center(40))
    linha(40)
    print(
          f'{cores("amarelo", "1")} - {cores("azul", "Ver pessoas cadastradas")}\n'
          f'{cores("amarelo", "2")} - {cores("azul", "Cadastrar nova pessoa")}\n'
          f'{cores("amarelo", "3")} - {cores("azul", "Sair do sistema")}'
          )
    linha(40)

    #------ Laço para caso de opção errada ------
    while True:
        try:
            # O programa vai perguntar qual opção:
            entrada = input(f'{cores("amarelo", "Sua Opção:")} ').strip()

            if not entrada.isdigit():
                raise ValueError("Por favor! digite um número inteiro válido.")

            opcao = int(entrada)
            #------ Validação de opções ------
            if opcao == 1:
                # Chamando a função tabela.
                tabela(
                    'PESSOAS CADASTRADAS',
                    'pessoas'
                )
                break
            elif opcao == 2:
                linha(40)
                print('NOVO CADASTRO'.center(40))
                linha(40)
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
                break
            elif opcao == 3:
                linha(40)
                print('Saindo do sistema... Até logo!'.center(40))
                linha(40)
                sleep(3)
                break
            else:
                raise ValueError(f'"{opcao}" e um valor inválido, tente novamente')
        #----- Logs de erros -----
        except ValueError as erro:
            print(f'\033[31mErro! {erro}\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mErro! o usuário decidiu não informar uma opção\033[m')
            opcao = 3
            break

    if opcao == 3:
        break
