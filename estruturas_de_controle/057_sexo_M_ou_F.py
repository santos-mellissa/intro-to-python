"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('\nEntre com o seu sexo (M/F): ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('\nEntrada inválida.')

print(f'\nO sexo informado foi: {sexo}\n')
