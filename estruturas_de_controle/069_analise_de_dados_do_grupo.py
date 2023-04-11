"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deve perguntar
se o usuário quer ou não continuar. No final mostre:
- Quantas pessoas tem mais de 18 anos;
- Quantos homens foram cadastrados;
- Quantas mulheres tem menos de 20 anos"""

sexo = 'a'
continuar = 'a'
qtd_maiores_18 = 0
qtd_homens = 0
qtd_mulheres_menores_20 = 0

print('\n')

while True:
    idade = int(input('Entre com sua idade: '))
    while sexo not in 'FM':
        sexo = str(input('Entre com seu sexo: (F/M) ')).strip().upper()
    if idade > 18:
        qtd_maiores_18 += 1
    if sexo == 'M':
        qtd_homens += 1
    if sexo == 'F' and idade < 20:
        qtd_mulheres_menores_20 += 1
    sexo = 'a'
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? (N/S) ')).strip().upper()
    if continuar == 'N':
        break
    else:
        continuar = 'a'
print(f'\nQuantidade de pessoas maiores de 18: {qtd_maiores_18}')
print(f'Quantidade de homens: {qtd_homens}')
print(f'Quantidade de mulheres menores de 20: {qtd_mulheres_menores_20}\n')
