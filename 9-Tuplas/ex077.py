palavras = ('carro', 'moto', 'caminhao',
            'caderno', 'revista', 'notebook',
            'computador', 'python', 'mercado'
            )
for c in palavras:
    print(c.upper(), end=' - ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()

