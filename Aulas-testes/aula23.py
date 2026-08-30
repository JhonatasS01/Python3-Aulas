try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (TypeError, ValueError):
    print('Tivemos um problema com os tipos de arquivo que você digitou!')
except ZeroDivisionError:
    print('Não e possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os arquivo!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado e {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
