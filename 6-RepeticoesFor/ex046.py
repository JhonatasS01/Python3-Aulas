from time import sleep
from sys import stdout

print('=-'*12)
print('{:^22}'.format('CONTAGEM DOS FOGOS'))
print('=-'*12)
for C in range(10, -1, -1):
    print('\r{:^22}'.format(C), end='')
    stdout.flush()
    sleep(1)
print('\nBOOM!!!', end='')
sleep(1)
print(' BOOM!!', end='')
sleep(1)
print(' BOOM!!! ', end='')
sleep(1)
print('POOOW!!')
