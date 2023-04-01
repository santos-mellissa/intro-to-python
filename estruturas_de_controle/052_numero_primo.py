"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input('\nEntre com o número: '))
verificador = 0

print('\n')

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end= ' ')
        verificador += 1
    else:
        print('\033[31m', end= ' ')
    print(f'{c}', end= ' ')

print('\n')

if verificador > 2:
    print('\n\033[mO número informado não é primo.\n')
else:
    print('\n\033[mO número informado é primo.\n')