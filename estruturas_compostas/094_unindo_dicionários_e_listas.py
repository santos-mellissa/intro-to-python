"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
- Quantas pessoas cadastradas
- A média de idade
- Uma lista com mulheres
- Uma lista com idade acima da média"""

pessoa = dict()
lista = list()
continuar = 'S'

# coleta de dados
while True:
    if continuar == 'S':
        pessoa['nome'] = str(input('Nome: '))

        # validação do sexo
        while True:
            pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
            if pessoa['sexo'] not in 'MF':
                print('\033[1;31mERRO! O valor digitado não esta em [M/F]... Tente novamente...\033[m')
            else:
                break

        pessoa['idade'] = int(input('Idade: '))

        while True:
            continuar = input('Quer continuar? [S/N] ').upper()[0]
            if continuar not in 'SN':
                print('Entrada inválida.')
            else:
                break
        lista.append(pessoa.copy())
    elif continuar == 'N':
        break

print(f'\n Foram cadastradas o total de {len(lista)} pessoas')
soma_idade = 0
for i, v in enumerate(lista):
    soma_idade += v['idade']
print(f'Média de idade: {soma_idade / len(lista):.1f}')
print(f'Mulheres cadastradas: ', end='')
for i, v in enumerate(lista):
    if v['sexo'] == 'F':
        print(v['nome'], end=' ')
print()
print('Pessoas com idade acima da media: ')
for i, v in enumerate(lista):
    if v['idade'] > (soma_idade / len(lista)):
        for k, valor in v.items():
            print(f'  -{k} é {valor} ;', end=' ')
        print()
print('\n')
