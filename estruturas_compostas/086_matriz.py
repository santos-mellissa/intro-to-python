"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print('\n')

for pos1 in range(0,3):
    for pos2 in range(0,3):
        matriz[pos1][pos2] = int(input(f'Entre com um valor para {pos1}, {pos2}: '))

for pos1 in range(0,3):
    for pos2 in range(0,3):
        print(f'[{matriz[pos1][pos2]:^5}]', end='')
    print()

print('\n')
