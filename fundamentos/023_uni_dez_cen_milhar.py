"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

num = input('\nEntre com um número inteiro de 0 a 9999: ').zfill(4)

print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')
