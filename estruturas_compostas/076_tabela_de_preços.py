"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços organizando os dados de forma tabular."""

produtos = ('arroz', 20.50, 'feijão', 10.99, 'biscoito', 3.50, 'amendoim', 15.90)

print('\n')

for index, item in enumerate(produtos):
    if index % 2 == 0:
        print(item, produtos[index + 1])
print('\n')
