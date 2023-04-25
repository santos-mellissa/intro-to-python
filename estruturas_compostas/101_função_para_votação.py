"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
negado, opcional ou obrigatório nas eleições."""

from datetime import datetime

def voto(ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade in (16,17) or idade > 70:
        return f'\nIdade: {idade}\nVoto opcional.\n'
    elif idade >= 18 and idade <= 70:
        return f'\nIdade: {idade}\nVoto obrigatório.\n'
    else:
        return f'\nIdade: {idade}\nVoto negado.\n'


ano_nascimento = int(input('\nEntre com o ano de seu nascimento: '))
print(voto(ano_nascimento))
