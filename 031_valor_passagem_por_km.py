"""Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule
o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
para viagens mais longas."""

kms = float(input('\nInforme a distância da viagem em quilômetros: '))

if kms <= 200:
    print('\nO valor da passagem é de R${:.2f}.\n'.format(kms * 0.45))
else:
    print('\nO valor da passagem é de R${:.2f}.\n'.format(kms * 0.50))