"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculos.
- O nome com todas minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

nome = input('\nEntre com o seu nome completo: ')

print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
print(f'Seu nome em letras minúsculas é: {nome.lower()}')
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))

lista = nome.split()

print(f'Seu primeiro nome tem {len(lista[0])} letras.\n')
