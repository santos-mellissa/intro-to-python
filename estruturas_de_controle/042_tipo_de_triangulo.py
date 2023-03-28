

reta_a = float(input('\nEntre com o comprimento da primeira reta: '))
reta_b = float(input('\nEntre com o comprimento da segunda reta: '))
reta_c = float(input('\nEntre com o comprimento da teraceir reta: '))

isosceles = reta_a == reta_b != reta_c or reta_a == reta_c != reta_b or reta_b == reta_c != reta_a
escaleno = reta_a != reta_b != reta_c != reta_a
equilatero = reta_a == reta_b == reta_c
triangulo = reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_b + reta_c > reta_a

if triangulo == True and triangulo== isosceles:
    print('Os segmentos acima podem formar um triângulo Isosceles.')
elif triangulo == True and triangulo == escaleno:
    print('Os segmentos podem formar um triângulo Escaleno.')
elif triangulo == True and triangulo == equilatero:
    print('Os segmentos podem formar um triângulo Equilátero.')
else:
    print('\nAs retas não podem formar um triângulo.\n')