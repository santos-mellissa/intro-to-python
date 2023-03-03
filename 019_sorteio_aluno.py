""" Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido."""

from random import choice

aluno_a = str(input(f'\nInforme o nome do(a) primeiro(a) aluno(a): '))
aluno_b = str(input('Informe o nome do(a) segundo(a) aluno(a): '))
aluno_c = str(input('Informe o nome do(a) terceiro(a) aluno(a): '))
aluno_d = str(input('Informe o nome do(a) quarto(a) aluno(a): '))

alunos = [aluno_a, aluno_b, aluno_c, aluno_d]
sorteado = choice(alunos)

print(f'\nAluno(a) sorteado: {sorteado}\n')