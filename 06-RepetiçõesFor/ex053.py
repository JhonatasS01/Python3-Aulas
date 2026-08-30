P = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
contra = P[::-1]
print(f'\033[34m\nNormal:\033[m {P}')
print(f'\033[34mContrário:\033[m {contra}')
if P == contra:
    print('\033[1;32mA frase e um palíndromo\033[m')
else:
    print('\033[1;31mA frase não e um palíndromo\033[m')
