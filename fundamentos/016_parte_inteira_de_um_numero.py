# Crie um programa que leia um número Real qualquer pelo teclado e mostre a sua porção inteira.

from math import trunc

num = float(input('\nInforme um número real: '))

print(f'\nA parte inteira do número Real informado é: {trunc(num)}\n')
