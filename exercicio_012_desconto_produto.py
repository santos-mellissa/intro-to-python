# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('\nInsira o preço do produto: R$'))

preco_atual = preco-(preco*0.05)

print(f'\nO valor do produto foi atualizado de R${preco:.2f} para R${preco_atual:.2f} com os 5% de desconto.\n')
