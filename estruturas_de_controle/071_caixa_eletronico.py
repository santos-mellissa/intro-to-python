"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Considere que o caixa possui cédulas de 50, 20, 10 e 1"""

cedulas_disponiveis = [50, 20, 10, 1]

valor_saque = int(input('\nInforme o valor do saque: '))

qtd_cedulas_50 = 0
qtd_cedulas_20 = 0
qtd_cedulas_10 = 0
qtd_cedulas_1 = 0

while True:
    if valor_saque >= 50:
        qtd_cedulas_50 += 1
        valor_saque -= 50
    elif valor_saque >= 20:
        qtd_cedulas_20 += 1
        valor_saque -= 20
    elif valor_saque >= 10:
        qtd_cedulas_10 += 1
        valor_saque -= 10
    elif valor_saque >= 1:
        qtd_cedulas_1 += 1
        valor_saque -= 1
    else:
        break

print('\nQuantidade de cédulas de cada valor:')
print(f'Cédula(s) de R$50,00: {qtd_cedulas_50}')
print(f'Cédula(s) de R$20,00: {qtd_cedulas_20}')
print(f'Cédula(s) de R$10,00: {qtd_cedulas_10}')
print(f'Cédula(s) de R$1,0: {qtd_cedulas_1}\n')