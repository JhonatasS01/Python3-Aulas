import requests
from time import sleep
#from urllib.parse import urlparse

print('Fazendo a requisição...')
sleep(3)
try:
    url = 'https://pudim.com/'
    resposta = requests.get(url)

    #name = urlparse(url).netloc.replace('www.', '')
    name = url.replace('https://', '').replace('http://', '').replace('/', '').replace('www.', '')

    print(f'\033[1;32mO site "{name}" esta funcionando normalmente.\033[m')
except requests.exceptions.RequestException:
    print('\033[1;31mO site não esta funcionando ou esta fora do ar.\033[m')
