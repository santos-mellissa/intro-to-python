"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal"""

num = int(input('\nEntre com um número inteiro:\n-> '))
tipo_conversao = int(input('\nEscolha a base de conversão:\n1- Binário\n2- Octal\n3- Hexadecimal\n-> '))

if tipo_conversao == 1:
    print(f'\nO número {num} convertido para binário é {bin(num)}.')
elif tipo_conversao == 2:
    print(f'\nO número {num} convertido para octal é {oct(num)}.')
elif tipo_conversao == 3:
    print(f'\nO número {num} convertido para hexadecimal é {hex(num)}.')
else:
    print('\nEntrada inválida.')