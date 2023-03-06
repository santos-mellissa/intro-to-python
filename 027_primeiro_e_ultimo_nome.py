"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último
nome separadamente."""

nome = str(input('\nEntre com o seu nome completo: ')).strip()

nome_2 = nome.split(' ')

prim_nome = nome_2[0].title()
sobrenome = nome_2[-1].title()

print(f'Seu nome e último nome: {prim_nome} {sobrenome}\n')

