"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Quantas mulheres têm menos de 20 anos
- Qual é o nome do homem mais velho"""

total_idade = 0
lista_idade_h = []
lista_nome_h = []
mulheres_20 = 0

print('\n')

for c in range(1,5):
    nome = str(input(f'\nEntre com o nome da {c}ª pessoa: ')).strip().title()
    idade = int(input(f'Entre com a idade da {c}ª pessoa: '))
    sexo = int(input(f'Escolha uma opção de acordo com o sexo da {c}ª pessoa:\n[1] Feminino\n[2] Masculino\n--> '))
    total_idade += idade
    if sexo == 1 and idade < 20:
        mulheres_20 = mulheres_20 + 1
    
    if sexo == 2:
        lista_nome_h.append(nome)
        lista_idade_h.append(idade)

print(f'\nA média de idade do grupo é de {total_idade / 5:.1f}.')
print(f'A quantidade de mulheres menores de 20 anos é de {mulheres_20}.')
print(f'O homem mais velho tem {max(lista_idade_h)} anos e seu nome é {lista_nome_h[lista_idade_h.index(max(lista_idade_h))]}.\n')
