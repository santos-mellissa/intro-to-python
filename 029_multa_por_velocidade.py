"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
Km acima do limite."""

velocidade = float(input('\nVelocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\nVocê ultrapassou o limite de velocidade e deve pagar R${multa:.2f} de multa.\n')
else:
    print('\nVocê está dentro do limite de velocidade permitido.')