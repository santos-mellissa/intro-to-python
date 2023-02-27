# Faça um programa que leia um número inteiro e realize diversas operações aritméticas.

from math import sqrt

num = int(input('Entre com um número: '))
tabuada = 'Tabuada'

# Exercício 5: Antecessor e sucessor
print('\nO sucessor de {} é {}.'.format(num, num+1))
print('O antecessor de {} é {}.'.format(num, num-1))
# Exercício 6: Dobro, triplo e raiz quadrada
print('\nO dobro de {} é {}.'.format(num, num*2))
print('O triplo de {} é {}.'.format(num, num*3))
print('A raiz quadrada de {} é {:.1f}.\n'.format(num, sqrt(num)))
# Exercício 9: Tabuada
print('\n{:-^30}'.format(tabuada.upper()))
print(f'{num} x 01 = {num*1}')
print(f'{num} x 02 = {num*2}')
print(f'{num} x 03 = {num*3}')
print(f'{num} x 04 = {num*4}')
print(f'{num} x 05 = {num*5}')
print(f'{num} x 06 = {num*6}')
print(f'{num} x 07 = {num*7}')
print(f'{num} x 08 = {num*8}')
print(f'{num} x 09 = {num*9}')
print(f'{num} x 10 = {num*10}')
print('-'*30)
