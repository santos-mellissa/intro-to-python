"""Faça um programa que leia um número qualquer e mostre o seu fatorial."""

num = int(input('\nEntre com o número: '))
c = num
fatorial = 1

print(f'\n{num}! = ', end= '')

while c > 0:
    print(f'{c}', end= '')
    print(' x ' if c > 1 else ' = ', end= '')
    fatorial *= c
    c -= 1
print(f'{fatorial}\n')