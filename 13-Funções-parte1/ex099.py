from time import sleep
def maior(*args):
    print('=-' * 30)
    print('Analisando os valores passados...')
    sleep(0.5)
    for c in args:
        print(f'{c} ', end='')
    print(f'- Foram informados {len(args)} valores ao todo.')
    if not args:
        print(f'O maior valor foi: 0')
    else:
        print(f'O maior valor foi: {max(args)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
