numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
print('-'*30)
print('Números por extenso de 0 a 20')
print('-'*30)
while True:
    n = int(input('Digite um número: '))
    if 0 <= n <= 20:
        print(f'Por extenso: {numeros[n]}')
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if cont == 'N':
            break
    else:
        print('Tente novamente.', end=' ')
print('\nFim do programa')