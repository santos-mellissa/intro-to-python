"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista  a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior."""

lista = list()

from random import randint

def sorteia(nom_lista):
    for cont in range(0, 5):
        num = randint(1, 10)
        nom_lista.append(num)
    print(f'\nValores sorteados: {nom_lista}')

def somaPar(nom_lista):
    soma_pares = 0
    for valor in nom_lista:
        if valor % 2 == 0:
            soma_pares += valor
    print(f'A soma dos números pares é igual a: {soma_pares}\n')

sorteia(lista)
somaPar(lista)
