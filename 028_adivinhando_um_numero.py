"""Escreva uma programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa
deverá escrever na tela se o usuário venceu o perdeu."""

from random import randint
from time import sleep

num_computador = randint(0,5)

num = int(input('\nTente adivinhar o número que estou pensando de 0 a 5: '))

if num < 0 or num > 5:
    num = int(input(f'\nJesus Christ! AGAIN: Número de 0 a 5: '))
else:
    if num==num_computador:
        print(f'\nAcertou, mizeravi! O número que pensei é o {num_computador}.\n')
    else:
        print(f'\nErrrrou (faustão voice)! O número que pensei é o {num_computador}.\n')
