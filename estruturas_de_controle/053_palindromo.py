# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando espaços.

frase = str(input('\nEntre com a frase: ')).strip().upper()
palavras = frase.split()
juncao = ''.join(palavras)
inverso = ''

for letra in range(len(juncao)-1, -1, -1):
    inverso += juncao[letra]

print(f'\nO inverso de {juncao} é {inverso}.')

if inverso == juncao:
    print('A frase é um palíndromo.\n')
else:
    print('A frase não é um palíndromo.\n')
