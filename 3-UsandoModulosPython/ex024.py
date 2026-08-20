city = str(input('Digite o nome da cidade: ')).strip()
print('\nA cidade começa com Santo?:', end=' ')
print(city[:5].title() == 'Santo')
