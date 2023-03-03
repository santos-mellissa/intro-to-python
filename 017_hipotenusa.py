"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa."""

from math import hypot

cat_oposto = float(input('\nInforme o comprimento do cateto oposto do triângulo retângulo: '))
cat_adjacente = float(input('Informe o comprimento do cateto adjacente do triângulo retângulo: '))

h = hypot(cat_oposto,cat_adjacente)

print(f'\nA hipotenusa é igual a {h:.1f}.\n')
