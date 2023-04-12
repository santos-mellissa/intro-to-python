"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
- Quantas vezes apareceu o valor 9
- Em que posição foi digitado o primeiro valor 3
- Quais foram os valores pares"""

num_a = int(input('\nEntre com o primeiro número: '))
num_b = int(input('Entre com o segundo número: '))
num_c = int(input('Entre com o terceiro número: '))
num_d = int(input('Entre com o quarto número: '))
numeros = (num_a, num_b, num_c, num_d)

print(f'\nO número 9 apareceu {numeros.count(9)} vez(es).')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3) + 1}ª posição.')
else:
    print(f'O número 3 não foi digitado em nenhuma posição.')
print('Números pares digitados:', end= ' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end= ' ')
print('\n')