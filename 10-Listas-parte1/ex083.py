expre = str(input('Digite a expressão: '))
pilha = list()
correta = True
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            correta = False
            break
if correta and len(pilha) == 0:
    print('\033[1:32mSua expressão esta correta!\033[m')
else:
    print('\033[1:31mSua expressão esta errada!\033[m')
print(pilha)
