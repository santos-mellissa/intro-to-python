"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais."""

palavras = ('amendoim', 'gato', 'gel', 'computador', 'borracha')
vogais = ('a', 'e', 'i', 'o', 'u')

print('\n')

for palavra in palavras:
    print(palavra, end= ': ')
    for vogal in vogais:
        if vogal in palavra:
            print(vogal, end=' ')
    print()

print('\n')
