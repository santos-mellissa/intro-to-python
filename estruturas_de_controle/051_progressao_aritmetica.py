"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão."""

primeiro_termo = int(input('\nEntre com o primeiro termo: '))
razao = int(input('Entre com a razão: '))
decimo = primeiro_termo + (10 - 1) * razao

print('\n')

for c in range(primeiro_termo, decimo + razao, razao):
    print(f'{c}', end= ', ')
print('Fim.\n')
