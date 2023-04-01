"""Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram
no intervalo de 1 até 500. """

soma = 0

for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c # ou s += c
print(f'\nA soma dos números ímpares, múltiplos de 3 e que se encontram no intervalo de 1 até 500 é igual a: {soma:.0f}\n')
