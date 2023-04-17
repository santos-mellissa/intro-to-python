"""Fça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno."""

def área(larg,comp):
    a = larg * comp
    print(f'\nA área de um terreno {largura} x {comprimento} é de {a:.1f}m².\n')


largura = float(input(f'\nEntre com a largura do terreno: '))
comprimento = float(input(f'Entre com o comprimento do terreno: '))
área(largura, comprimento)
