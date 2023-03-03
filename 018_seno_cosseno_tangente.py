# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('\nEntre com o valor do ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'\nO ângulo de {angulo:.1f} tem o seno igual: {seno:.1f}.')
print(f'O ângulo de {angulo:.1f} tem o cosseno igual: {cosseno:.1f}.')
print(f'O ângulo de {angulo:.1f} tem o tangente igual: {tangente:.1f}.\n')