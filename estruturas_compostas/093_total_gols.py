"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois, vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

dados = dict()
gols = list()
total_gols = 0

dados['Nome'] = str(input('\nEntre com o nome do jogador: ')).title()
dados['Partidas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou? \n'))
for c in range(0, dados['Partidas']):
    gols.append(int(input(f'Quantos gols fez na partida {c+1}? ')))
    total_gols += gols[c]
dados['Gols'] = gols.copy()
dados['Total'] = total_gols
print('-'*59)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-'*59)
print(dados)
print('-'*59)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partidas.')
for k, v in enumerate(dados["Gols"]):
    print(f'   => Na partida {k+1}, fez {v} gols.')
print(f'\nFoi um total de {dados["Total"]} gols.\n')