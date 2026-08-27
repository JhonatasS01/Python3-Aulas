from dados import dict_to_list
import tools

dados = dict_to_list('Nome', 'Idade', 'pessoas')
conteudo = tools.file('pessoas', dados)

tools.tabela('PESSOAS CADASTRADAS', dados)
