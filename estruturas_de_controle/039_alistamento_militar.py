"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também
deverá mostrar o tempo que falta ou que já passou do prazo."""

from datetime import date

atual = date.today().year
ano_nasc = int(input('\nInforme o ano de seu nascimento: '))
idade = atual - ano_nasc

print(f'\nVocê nasceu em {ano_nasc} e nesse ano ({atual}) você fez/faz {idade} anos.\n')

if idade == 18:
    print('\nVocê está no ano de seu alistamento!\n')
elif idade < 18:
    tempo = 18 - idade
    ano_alis = atual + tempo
    print(f'\nFalta(m) {tempo} ano(s) para você se alistar. Você precisa se alistar em {ano_alis}.\n')
else:
    tempo = idade - 18
    ano_alis = atual - tempo
    print(f'\nSe passaram {tempo} ano(s) do ano seu alistamento. Você deveria ter se alistado em {ano_alis}!\n')