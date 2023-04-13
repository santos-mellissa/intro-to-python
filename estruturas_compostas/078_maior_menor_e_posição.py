"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas posições na lista."""

c = 0
lista = []
posições_maior = []
posições_menor = []

print('\n')

for c in range(0,5):
    lista.append(int(input('Entre com um número: ')))

maior = max(lista)
menor = min(lista)

for pos, valor in enumerate(lista):
    if valor == maior:
       posições_maior.append(pos)

for pos, valor in enumerate(lista):
    if valor == menor:
       posições_menor.append(pos)

print(f'\nO maior número informado foi o {maior}, que aparece na(s) posição(ões): {posições_maior}')
print(f'O menor número informado foi o {menor}, que aparece na(s) posição(ões): {posições_menor}\n')
