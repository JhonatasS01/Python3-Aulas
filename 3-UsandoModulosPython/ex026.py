frase = str(input('Digite uma frase: ')).strip().upper()
print('\nA letra A aparece {} vezes'.format(frase.count('A')))
print('Aparece pela primeira vez na posição: {}'.format(frase.find('A')+1))
print('Aparece pela ultima vez na posição: {}'.format(frase.rfind('A')+1))
