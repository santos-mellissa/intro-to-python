"""Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0 = REPROVADO
- Média entre 5.0 e 6.9 = RECUPERAÇÃO
- Média 7.0 ou superior = APROVADO"""

nota_a = float(input('\nEntre com a primeira nota: '))
nota_b = float(input('Entre com a segunda nota: '))
media = (nota_a + nota_b) / 2

if media < 5:
    print(f'\nSua média foi de {media:.1f}. Você foi REPROVADO!\n')
elif 5 <= media < 7:
    print(f'\nSua média foi de {media:.1f}. Você pode realizar a RECUPERAÇÃO!\n')
else:
    print(f'\nSua média foi de {media:.1f}. Você foi APROVADO!\n')
