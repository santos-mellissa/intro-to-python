"""Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o seu IMC e mostre o seu status, de acordo
com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- Entre 25 e 30: Sobrepeso
- Entre 30 e 40: Obesidade
- Acima de 40: Obesidade mórbida"""

peso = float(input("\nEntre com o seu peso: "))
altura = float(input("Entre com a sua altura: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    status = 'Abaixo do peso'
elif imc >= 18.5 and imc <= 25:
    status = 'Peso ideal'
elif imc > 25 and imc <= 30:
    status = 'Sobrepeso'
elif imc > 30 and imc <= 40:
    status = 'Obesidade'
else:
    status = 'Obesidade mórbida'
print('\nO seu IMC é de {:.1f} e o status é: {}\n'.format(imc,status))