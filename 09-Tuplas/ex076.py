print('-'*36)
print(f'{'LISTAGEM DE PREÇOS':^36}')
print('-'*36)
produtos = ('Caderno', 29.90, 'Lápis', 2.99, 'Celular', 1950.99,
            'Teclado Mecânico', 195.98, 'Mochila', 79.00, 'Livro', 19.90,
            'Borracha', 1.99, 'Apostila', 129.99, 'Mouse', 109.98
            )
for c in range(0, len(produtos), 2):
    nome = produtos[c]
    preco = produtos[c+1]
    print(f'{nome:.<25} R$ {preco:>7.2f}')
print('-'*36)
