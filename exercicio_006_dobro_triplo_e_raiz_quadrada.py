# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

num = int(input('\nEntre com um número: '))

print('\nO dobro de {} é {}.'.format(num, num*2))
print('O triplo de {} é {}.'.format(num, num*3))
print('A raiz quadrada de {} é {:.1f}.\n'.format(num, sqrt(num)))