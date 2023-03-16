# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_a = int(input('\nEntre com a primeira nota: '))
nota_b = int(input('Entre com a segunda nota: '))

media = ((nota_a + nota_b) / 2)

print('\nO média das notas é: {}.\n'.format(media))
