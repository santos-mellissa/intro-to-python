"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule a preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado"""

km = float(input('\nInforme a quantidade de km percorridos: '))
dias = int(input('Informe a quantidade de dias que o carro foi alugado: '))

valor_dias = dias * 60
valor_km = km * 0.15
valor_total = valor_dias + valor_km

print(f'\nO total a pagar é de R${valor_total:.2f}.\n')
