""" O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import shuffle

aluno_a = str(input(f'\nInforme o nome do(a) primeiro(a) aluno(a): '))
aluno_b = str(input('Informe o nome do(a) segundo(a) aluno(a): '))
aluno_c = str(input('Informe o nome do(a) terceiro(a) aluno(a): '))
aluno_d = str(input('Informe o nome do(a) quarto(a) aluno(a): '))

alunos = [aluno_a, aluno_b, aluno_c, aluno_d]
shuffle(alunos)

print('\nA ordem da apresentação será: ')
print(alunos)
