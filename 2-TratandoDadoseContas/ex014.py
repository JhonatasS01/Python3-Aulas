print('\033[33m=+\033[m'*16)
print('\033[34m{:^33}\033[m'.format('CONVERSOR DE TEMPERATURA'))
print('\033[33m=+\033[m'*16)
C = float(input('Digite a temperatura (Celsius): '))
F = ((9 * C) / 5) + 32
print('\n\033[34mCelsius:\033[m {}°C\n\033[34mFahrenheit:\033[m {}°F'.format(C, F))
