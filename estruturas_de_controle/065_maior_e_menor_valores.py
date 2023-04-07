"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores."""

num = 0
lista_num = []
continuar = 'S'

print('\n')

while continuar == 'S':
    num = int(input('Entre com um número: '))
    continuar = str(input('Deseja continuar (S/N)? ')).strip().upper()
    lista_num.append(num)
print(f'\nA média dos números informados é igual a {sum(lista_num) / len(lista_num):.1f}.')
print(f'O maior número inserido foi: {max(lista_num)}')
print(f'O menor número inserido foi: {min(lista_num)}\n')
