"""Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos. """

primeiro_termo = int(input('\nEntre com o primeiro termo: '))
razao = int(input('Entre com a razão: '))
termo = primeiro_termo
mais_termos = 10
c = 0

print('\n')

while mais_termos != 0:
    for i in range(mais_termos):
        print(f'{termo}', ' -> ', end= '')
        termo += razao
        c += 1
    mais_termos = int(input('\nDeseja ver mais quantos termos? '))
print('Fim.')
print(f'\nProgressão aritmética finalizada com {c} termos no total\n')
