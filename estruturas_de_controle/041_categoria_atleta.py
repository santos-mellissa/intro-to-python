"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25: MATER"""

from datetime import date

atual = date.today().year
ano_atleta = int(input('\nEntre com o ano de nascimento do atleta: '))
idade = atual - ano_atleta

print('\nO atleta tem {} anos'.format(idade))
if idade <= 9:
   cat = 'MIRIM'
elif idade > 9 and idade <= 14:
    cat = 'INFANTIL'
elif idade > 14 and idade <= 19:
    cat = 'JUNIOR'
elif idade > 19 and idade <= 20:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print(f'Categoria: {cat}\n')