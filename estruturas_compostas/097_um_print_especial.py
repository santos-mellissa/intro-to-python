"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável."""

def escreva(x):
    comprimento = len(x)
    print(f'~' * (comprimento + 2))
    print(x.center(comprimento + 2))
    print(f'~' * (comprimento + 2))


palavra = str(input(f'\nEntre com um texto: '))
escreva(palavra)
