# Faça um programa que leia a largura e a altura de uma parece em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('\nInforme a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
litros_tinta = area / 2

print(f'\nA área de sua parede é de {area:.1f} m².')
print(f'Você precisará de {litros_tinta:.1f} litros de tinta para pintá-la.\n')
