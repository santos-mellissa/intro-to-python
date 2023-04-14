"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

ficha = []
continuar = 'a'

print('\n')

while True:
    nome = str(input('Entre com o nome do aluno: '))
    nota_1 = float(input('Entre a primeira nota: '))
    nota_2 = float(input('Entre a segunda nota: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? (N/S) ')).strip().upper()
    if continuar == 'N':
        break
    else:
        continuar = 'a'

print('{:<4}{:<10}{:>8}'.format('N°', 'Nome', 'Média'))
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = input('Mostrar notas de qual aluno? (999 para parar)')
    if opc == '999':
        print('Programa finalizado.\n')
        break
    if int(opc) <= len(ficha) - 1:
        print(f'Notas de {ficha[int(opc)][0]}: {ficha[int(opc)][1]}\n')
