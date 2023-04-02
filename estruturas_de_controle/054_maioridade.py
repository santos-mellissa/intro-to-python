"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores."""

from datetime import date

atual = date.today().year
maiores = 0
menores = 0

print('\n')

for c in range(0,7):
    ano_nasc = int(input('Informe o ano de nascimento: '))
    idade = atual - ano_nasc
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1

print(f'\nDas 7 pessoas, {maiores} atingiram a maioridade e {menores} não atingiram.\n')
