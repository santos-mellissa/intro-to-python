""" Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece uma substring.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez. """

frase = str(input('\nEntre com a frase: ')).lower().strip()
substring = str(input('Entre com a expressão para análise: '))

if substring not in frase:
    print(f'\n"{substring}" não esta presente na frase.\n')
else:
    print(f'\nQuantas vezes "{substring}" aparece: {frase.count(substring)}')
    print(f'Posição em que "{substring}" aparece a primeira vez: {frase.find(substring)+1}')
    print(f'Posição em que "{substring}" aparece a última vez: {frase.rfind(substring)+1}\n')
