"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome
de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente."""

def ficha(jogador='<nome não informado>',qtd_gols=0):
    print(f'\nO jogador {jogador.title()} fez {qtd_gols} gol(s).\n')

nome = str(input('\nEntre com o nome do jogador: '))
gols = str(input('Entre com o a quantidade de gols do jogador: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(qtd_gols=gols)
else:
    ficha(nome.title(),gols)
