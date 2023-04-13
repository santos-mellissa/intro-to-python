"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados em ordem crescente"""

valores = []

print('\n')

while True:
    num = int(input('Entre com um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Você já informou esse número.')
        break
valores.sort()
print(f'\nValores informados ordenados: {valores}\n')
