"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas dos que forem pares.
Se o valor digitado for ímpar, desconsidere-o."""

soma = 0

print('\n')

for c in range(0,6):
    num = int(input('Entre com um número inteiro: '))
    if num % 2 == 0:
        soma = soma + num
print(f'\nA soma dos números pares informados é igual a: {soma}\n')

