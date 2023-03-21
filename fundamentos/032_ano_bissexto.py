# Faça um programa que leia o ana qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('\nInforme o ano que quer analisar: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\nO ano {ano} é bissexto.\n')
else:
    print(f'\nO ano {ano} não é bissexto.\n')
