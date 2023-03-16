# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('\nEntre com um número: '))

print('\nO sucessor de {} é {}.'.format(num, num+1))
print('O antecessor de {} é {}.\n'.format(num, num-1))
