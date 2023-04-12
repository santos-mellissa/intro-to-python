"""Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol na ordem de colocação. Depois mostre:
- Os 5 primeiros colocados
- Os 4 últimos colocados
- Times em ordem alfabética
- Em que posição está o time da Chapecoense"""

import textwrap

c = 0
colocados = ('Flamengo','Santos','Palmeiras','Grêmio',
             'Atlético-PR', 'São Paulo','Internacional',
             'Corinthians','Fortaleza','Goias','Bahia','Vasco',
             'Atlético-MG','Fluminense','Botafogo','Ceará',
             'Cruzeiro','CSA','Chapecoense','Avaí')
colocados_ordenados = '\n'.join(textwrap.wrap(', '.join(sorted(colocados))))
pos_chapecoense = colocados.index('Chapecoense') + 1

print('\n5 primeiros colocados:\n')
for c in range(0,5):
    print(colocados[c])
    c += 1

print('\n4 últimos colocados:\n')
for c in range(16,20):
    print(colocados[c])
    c += 1

print(f'\nTimes colocados em ordem alfabética:\n{colocados_ordenados}')
print(f'\nO time Chapecoense está na {pos_chapecoense}ª posição.\n')
