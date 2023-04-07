"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é uma condição de parada. NO final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

num = 0
contagem = 0
soma = 0

print ('\n')

while num != 999:
    num = int(input('Entre com um número inteiro: '))
    if num != 999:
        contagem += 1
        soma += num
print(f'\nQuantidade de números inseridos: {contagem}')
print(f'Soma dos números inseridos: {soma}\n')

