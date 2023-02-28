# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 

valor = float(input('\nQuanto você tem em sua carteira? R$'))
dolar = valor / 5.21

print(f'\nCom R${valor:.2f} você pode comprar US${dolar:.2f}.\n') # valor do dólar em 02/23
