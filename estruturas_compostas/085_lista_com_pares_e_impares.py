"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separado os valores pares e ímpares. No final, mostre-os valores pares e ímpares em ordem crescente."""

num = [[],[]]
valor = 0
for numeros in range(0,7):
    valor = int(input('Entre com um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print(f'\nValores pares: {sorted(num[0])}')
print(f'Valores ímpares: {sorted(num[1])}\n')
