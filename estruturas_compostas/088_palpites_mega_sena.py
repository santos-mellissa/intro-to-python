"""Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint

lista = []
jogos = []

qtd_jogos = int(input('\nQuantos jogos serão gerados? '))

for c in range(0,qtd_jogos):
    lista = [randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60)]
    jogos.append(lista[:])
    lista.clear()

for index, jogo in enumerate(jogos):
    print(f'Jogo {index+1}: {jogo}')
