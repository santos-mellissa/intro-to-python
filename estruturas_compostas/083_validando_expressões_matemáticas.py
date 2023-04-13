"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

expressão = str(input('\nEntre com a expressão: '))
pilha = []

for parentese in expressão:
    if parentese == '(':
        pilha.append('(')
    elif parentese == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\nSua expressão está válida.\n')
else:
    print('\nSua expressão está inválida.\n')
