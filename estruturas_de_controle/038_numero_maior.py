"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

num_a = int(input('\nEntre com o primeiro número: '))
num_b = int(input('Entre com o segundo número: '))

if num_a > num_b:
    print(f'\nO primeiro valor ({num_a}) é maior.\n')
elif num_b > num_a:
    print(f'\nO segundo valor ({num_b}) é maior.\n')
else:
    print('\nNão existe valor maior, os dois são iguais.\n')