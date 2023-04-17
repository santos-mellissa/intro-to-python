"""Faça um programa qu tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

números = []

def maior(* lista):
    print(f'\nO maior número informado foi o: {max(lista)}\n')

while True:
    num = int(input('\nEntre com um número: '))
    números.append(num)
    cond = str(input('\nQuer continuar? [S/N]: ')).strip().upper()[0]
    while cond not in 'SN':
        cond = str(input('\nQuer continuar? [S/N]: ')).strip().upper()[0]
    if cond == 'N':
        break
maior(* números)
