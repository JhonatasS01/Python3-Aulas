N = int(input('Digite um número: '))
print('\nUnidade: {}\nDezena: {}'.format(N % 10, (N // 10) % 10), end=' ')
print('\nCentena: {}\nMilhar: {}'.format((N // 100) % 10, (N // 1000) % 10))
