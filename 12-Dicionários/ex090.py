alunos = dict()

alunos['Nome'] = str(input('Nome: '))
alunos['Media'] = float(input('Média: '))
if alunos['Media'] >= 7:
    alunos['Situacao'] = 'Aprovado'
elif alunos['Media'] >= 5:
    alunos['Situacao'] = 'Recuperação'
else:
    alunos['Situacao'] = 'Reprovado'

print('-=' * 30)
for k, v in alunos.items():
    print(f'{k}: {v}')
