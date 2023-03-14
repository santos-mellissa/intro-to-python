# Crie um programa que leia um número inteiro e mostre na tela se ele pe PAR ou ÍMPAR.

num = int(input('\nEntre com um número inteiro: '))

resto =  num % 2

if resto == 0:
    print(f'\nO número {num} é par.\n')
else:
    print(f'\nO número {num} é ímpar.\n')