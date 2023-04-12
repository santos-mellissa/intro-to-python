"""Crie um programa que vai gerar cinco números aleatórios e e colocar em uma tupla. Depois disso mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla."""

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'\nNúmeros gerados: {numeros}' )
print(f'Maior número da tupla: {max(numeros)}')
print(f'Menor número da tupla: {min(numeros)}\n')
