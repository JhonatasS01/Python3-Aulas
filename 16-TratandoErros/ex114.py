import requests
from time import sleep
from urllib.parse import urlparse

print('Fazendo a requisição...')
try:
    #Fazendo a requisição
    url = 'https://pudim.com.br/'
    resposta = requests.get(url)
    sleep(3)

    #Log de sucesso
    name = urlparse(url).netloc.replace('www.', '')
    print(f'\033[1;32mO site "{name}" está funcionando normalmente.\033[m')
except requests.exceptions.RequestException:
    #Log de erro
    print('\033[1;31mO site não está acessível ou esta fora do ar.\033[m')
