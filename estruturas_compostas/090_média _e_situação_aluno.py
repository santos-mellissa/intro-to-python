"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

dados_aluno = dict()

dados_aluno['Nome'] = str(input('\nEntre com o nome do aluno: ')).title()
dados_aluno['Média'] = float(input('Entre com a média do aluno: '))

if dados_aluno['Média'] < 5:
    dados_aluno['Situação'] = 'Reprovado'
elif dados_aluno['Média'] >= 5 and dados_aluno['Média'] < 7:
    dados_aluno['Situação'] = 'Recuperação'
else:
    dados_aluno['Situação'] = 'Aprovado'

for k, v in dados_aluno.items():
    print(f'{k}: {v} ')
