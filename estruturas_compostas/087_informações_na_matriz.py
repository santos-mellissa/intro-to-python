"""Aprimore o desafio 086, mostrando no final:
- A soma de todos os valores pares digitados
- A soma dos valores da terceira coluna
- O maior valor da segunda linha"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_col_3 = 0
maior_val_linha_2 = 0

print('\n')

for pos1 in range(0,3):
    for pos2 in range(0,3):
        matriz[pos1][pos2] = int(input(f'Entre com um valor para {pos1}, {pos2}: '))
        if matriz[pos1][pos2] % 2 == 0:
            soma_pares += matriz[pos1][pos2]
        if pos2 == 2:
            soma_col_3 += matriz[pos1][pos2]
for pos1 in range(0,3):
    for pos2 in range(0,3):
        print(f'[{matriz[pos1][pos2]:^5}]', end='')
    print()

print(f'\nSoma dos valores pares digitados: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_col_3}')
print(f'Maior valor da segunda linha: {max(matriz[1])}\n')
