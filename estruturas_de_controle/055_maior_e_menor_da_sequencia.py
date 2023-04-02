"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

lista = []

print('\n')

for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    lista += [peso]

print(f'\nO maior peso informado foi: {max(lista):.1f}')
print(f'O menor peso informado foi: {min(lista):.1f}\n')
