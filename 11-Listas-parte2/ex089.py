from time import sleep
dados = list()
media = soma = valor = 0

while True:
    nome = list()
    nome.append(str(input('Nome: ')))
    notas = list()
    for c in range(1, 3):
        notas.append(float(input(f'Nota {c}: ')))
    nome.append(notas[:])
    notas.clear()
    dados.append(nome[:])
    nome.clear()
    parador = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if parador == 'N':
        break
print('=+' * 30)
print(f'{"No.":<4}{"NOME":<13}{"MÉDIA":>2}')
print('-' * 30)
for c in range(0, len(dados)):
    soma = dados[c] [1]
    media = (soma[0] + soma[1]) / 2
    print(f"{c:<4}{dados[c][0]:<13}{float(media):>2.1f}")
print('-' * 30)
while True:
    valor = int(input('Mostrar nota de qual aluno? (999 finaliza!): '))
    if valor != 999:
        print(f'Notas de {dados[valor][0]} são {dados[valor][1]}')
        print('-' * 30)
    elif valor == 999:
        break
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')
