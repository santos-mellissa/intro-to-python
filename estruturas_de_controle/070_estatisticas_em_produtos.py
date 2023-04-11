"""Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
- Qual é o total gasto na compra;
- Quantos produtos custam mais de R$1000
- Qual é o nome do produto mais barato"""

lista_produtos = []
lista_valores = []
qtd_maior_mil = 0

print('\n')

while True:
    produto = str(input('Entre com o nome do produto: '))
    valor = float(input('Entre com o valor do produto: '))
    lista_produtos.append(produto)
    lista_valores.append(valor)
    if valor > 1000:
        qtd_maior_mil += 1
    continuar = str(input(f'Deseja continuar? (N/S) ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\nO total gasto na compra: R${sum(lista_valores):.2f}'.replace('.', ','))
print(f'Total de produtos que custam mais de R$1000,00: {qtd_maior_mil}')
print(f'Produto mais barato: {lista_produtos[lista_valores.index(min(lista_valores))]}')
print(f'Valor do produto mais barato: R${min(lista_valores):.2f}\n'.replace('.', ','))
