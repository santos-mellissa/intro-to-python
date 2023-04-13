"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas."""

lista_todos = []
lista_pares = []
lista_ímpares = []

continuar = 'a'


print('\n')

while True:
    num = int(input('Entre com um valor: '))
    lista_todos.append(num)

    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? (N/S) ')).strip().upper()
    if continuar == 'N':
        break
    else:
        continuar = 'a'

    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_ímpares.append(num)
print(f'\nLista completa: {lista_todos}')
print(f'Lista de números pares informados: {lista_pares}')
print(f'Lista de números ímpares informados: {lista_ímpares}\n')
