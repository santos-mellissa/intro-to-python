"""Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
e usando a estrutura while."""

primeiro_termo = int(input('\nEntre com o primeiro termo: '))
razao = int(input('Entre com a razão: '))
termo = primeiro_termo
cont = 1

print('\n')

while cont <= 10:
    print(f'{termo}', ' -> ', end= '')
    termo += razao
    cont += 1
print('Fim.\n')
