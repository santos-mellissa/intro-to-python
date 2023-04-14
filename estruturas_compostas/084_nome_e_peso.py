"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas
- Uma listagem com as pessoas mais pesadas
- Uma listagem com as pessoas mais leves"""

continuar =  'a'
dados = list()
lista = list()
maior_peso = 0
menor_peso = 0
pessoas_maior_peso = list()
pessoas_menor_peso = list()

while True:
    lista.append(str(input('Entre com seu nome: ')))
    lista.append(float(input('Entre com seu peso: ')))
    dados.append(lista[:])
    lista.clear()
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? (N/S) ')).strip().upper()
    if continuar == 'N':
        break
    else:
        continuar = 'a'

for dado_maior_peso in dados:
    if maior_peso == 0 or dado_maior_peso[1] > maior_peso:
        maior_peso = dado_maior_peso[1]

for dado_menor_peso in dados:
    if menor_peso == 0 or dado_menor_peso[1] < menor_peso:
        menor_peso = dado_menor_peso[1]

for dado_maior_nome in dados:
    if dado_maior_nome[1] == maior_peso:
        pessoas_maior_peso.append(dado_maior_nome[0])

for dado_menor_nome in dados:
    if dado_menor_nome[1] == menor_peso:
        pessoas_menor_peso.append(dado_menor_nome[0])
        
print(f'\nTotal de pessoas cadastradas: {len(dados)}')
print(f'Maior peso: {maior_peso}')
print(f'Pessoa(s) com o maior peso: {pessoas_maior_peso}')
print(f'Menor peso: {menor_peso}')
print(f'Pessoa(s) com o maior peso: {pessoas_menor_peso}\n')
