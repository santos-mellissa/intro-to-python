# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input('\nInforme a temperatura em °C: '))

f = (9 * c) / 5 + 32

print(f'\n{c:.1f}°C corresponde a {f:.1f}°F.\n')
