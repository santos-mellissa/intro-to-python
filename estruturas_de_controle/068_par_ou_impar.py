"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo."""

import random

tipo = ' '
total_vitorias = 0

print('\n')

while True:
    num_computador = random.randint(0, 10)
    num_escolhido = int(input('Entre com um número de 0 a 10: '))
    if num_escolhido >= 0 and num_escolhido <= 10:
        soma = num_escolhido + num_computador
        while tipo not in 'PI':
            tipo = str(input(f'Par ou Ímpar? (P/I) ')).strip().upper()[0]
        print(f'\nVocê escolheu {num_escolhido}, e eu {num_computador}. Total: {soma}')
        if tipo == 'P':
            if soma % 2 == 0:
                print(f'{soma} é um número par. Você venceu!\n')
                total_vitorias += 1
            else:
                print(f'{soma} é um número ímpar. Você perdeu!\n')
                break
        else:
            if soma % 2 == 1:
                print(f'{soma} é um número ímpar. Você venceu!\n')
                total_vitorias += 1
            else:
                print(f'{soma} é um número par. Você perdeu!\n')
                break 
        tipo = ' '               
    else:
        print('\nOpção inválida.\n')
print(f'Você teve um total de {total_vitorias} vitórias consecutivas!\n')
