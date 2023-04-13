"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
- Quantos números foram digitados
- A lista de valores, ordenada de forma decrescente
- Se o valor 5 foi digitado e está ou não na lista"""

lista = []
continuar = 'a'


print('\n')

while True:
    lista.append(int(input('Entre com um valor: ')))
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? (N/S) ')).strip().upper()
    if continuar == 'N':
        break
    else:
        continuar = 'a'
lista.sort(reverse = True)
print(f'\nForam digitados {len(lista)} números.')
print(f'Números em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado.\n')
else:
    print(f'O valor 5 não foi digitado.\n')
