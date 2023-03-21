# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num_a = float(input('\nEntre com o primeiro número: '))
num_b = float(input('Entre com o segundo número: '))
num_c = float(input('Entre com o terceiro número: '))
lista = [num_a,num_b,num_c]

print('\n{:.1f} é o maior número.'.format(max(lista)))
print('{:.1f} é o menor número.\n'.format(min(lista)))