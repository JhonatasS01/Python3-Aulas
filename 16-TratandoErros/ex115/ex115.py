from dados import dict_to_list
from tools import file

dados = dict_to_list('Nome', 'Idade')
conteudo = file('pessoas', dados)

print(conteudo)
