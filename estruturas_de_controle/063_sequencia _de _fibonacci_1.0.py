"""Escreve um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
uma sequência de Fibonacci."""

num = int(input('\nEntre com a quantidade de elementos: '))
c = 3
primeiro_elemento = 0
segundo_elemento = 1

print(f'\n{primeiro_elemento} - {segundo_elemento}', end= '')

while c <= num:
    terceiro_elemento = primeiro_elemento + segundo_elemento
    print(f' - {terceiro_elemento}', end= '')
    c = c + 1
    primeiro_elemento = segundo_elemento
    segundo_elemento = terceiro_elemento
print('\n')
