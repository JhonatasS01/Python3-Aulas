from dados import dict_to_list
import tools

print('-' * 40)
print('MENU PRINCIPAL'.center(40))
print('-' * 40)
print(
      '1 - Ver pessoas cadastradas\n'
      '2 - Cadastrar nova pessoa\n'
      '3 - Sair do sistema\n'
      )
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print()

#Informando o nome dos dicionarios
dados = dict_to_list('Nome', 'Idade', 'pessoas')
#Criando um arquivo txt com nome pessoas.
tools.file_json('pessoas', dados)
# Chamando a função tabela.
tools.tabela('PESSOAS CADASTRADAS', dados)


### A estrutura de coleta de dados e adição no arquivo.txt esta concluido,
### resta montar o esqueleto de manipulação do usuário como o menu principal.