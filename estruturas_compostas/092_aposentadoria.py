"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import datetime

dados_trabalhador = dict()

dados_trabalhador['Nome'] = str(input('\nEntre com o nome: '))
dados_trabalhador['Ano de Nascimento'] = int(input('Entre com o ano de nascimento: '))
ano_atual = datetime.now().year
dados_trabalhador['Idade'] = ano_atual - dados_trabalhador['Ano de Nascimento']
dados_trabalhador['CTPS'] = int(input('Entre com a CTPS (digite 0 cado não se aplique): '))

if dados_trabalhador['CTPS'] != 0:
    dados_trabalhador['Contratação'] = int(input('Entre com o ano de contratação: '))
    dados_trabalhador['Salário'] = float(input('Entre com o salário: '))
    dados_trabalhador['Aposentadoria'] = dados_trabalhador['Idade'] + ((dados_trabalhador['Contratação'] + 35) - datetime.now().year)

for k, v in dados_trabalhador.items():
    print(f'{k}: {v}')
