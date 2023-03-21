"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
um triângulo."""

reta_a = float(input('\nEntre com o comprimento da primeira reta: '))
reta_b = float(input('\nEntre com o comprimento da segunda reta: '))
reta_c = float(input('\nEntre com o comprimento da teraceir reta: '))

if reta_a < reta_b + reta_c and reta_b < reta_a + reta_c and reta_c < reta_a + reta_b:
    print('\nAs retas podem formar um triângulo.\n')
else:
    print('\nAs retas não podem formar um triângulo.\n')