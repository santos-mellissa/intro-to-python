"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário, ou 
então o empréstimo será negado."""

valor_casa = float(input('\nInforme o valor da casa: '))
salario = float(input('Informe seu salário: '))
anos = int(input('Informe em quantos anos você pretende pagar a casa: '))

pretacao_mensal = valor_casa / (anos * 12)

if pretacao_mensal <= (salario * 0.30):
    print('\nSeu empréstimo foi aprovado!\n')
else:
    print('\nSeu empréstimo não foi aprovado.\n')
