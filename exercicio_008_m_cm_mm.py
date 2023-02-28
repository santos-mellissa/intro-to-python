# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('\nInsira a distância em metros: '))

cm = metro * 100
mm = metro * 1000

print(f'\nMedida em centímetros: {cm} cm')
print(f'Medida em milímetros: {mm} mm\n')