"""Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora, o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

import random

num_computador = random.randint(0, 5)
palpites = 0

while True:
    palpite = input('\nTente adivinhar o número que estou pensando de 0 a 5: ')
    if not palpite.isdigit() or int(palpite) < 0 or int(palpite) > 5:
        print('\nEntrada inválida. Tente novamente: ')
        continue
    palpite = int(palpite)
    palpites += 1
    if palpite == num_computador:
        print(f'Acertou, mizeravi! O número que pensei é o {num_computador}. Você precisou de {palpites} tentativas válidas.')
        break
    else:
        print('Errrrou (faustão voice)! Tente novamente: ')
