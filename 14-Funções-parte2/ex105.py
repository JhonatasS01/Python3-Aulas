def notas(* valor, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valor: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    if not valor:
        return {'Erro!': 'nenhum valor informado'}
    boletim = {
        'Total' : len(valor),
        'Maior' : max(valor),
        'Menor' : min(valor),
        'Média' : sum(valor) / len(valor)
    }
    if sit:
        if boletim['Média'] >= 7:
            boletim['Situação'] = 'BOA'
        elif boletim['Média'] >= 5:
            boletim['Situação'] = 'RAZOÁVEL'
        else:
            boletim['Situação'] = 'RUIM'
    return boletim

#Program primary
reps = notas(5.5, 2.5, 1.5, sit=True)
print(reps)
help(notas)
