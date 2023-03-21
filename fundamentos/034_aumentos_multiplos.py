"""Escreve um programa que leia o salário d eum funcionário e calcule o valor do seu aumento.
- Para salários superiores a R$1.250,00 calcule um aumento de 10%;
- Para inferiores ou iguais, aumento de 15%."""

salario_atual = float(input('\nEntre com seu salário atual: '))
novo_salario = 0

if salario_atual > 1250:
    novo_salario = salario_atual + (salario_atual*0.10)
    print(f'\nSeu salário foi atualizado de R${salario_atual:.2f} para R${novo_salario:.2f}.\n')
else:
    novo_salario = salario_atual + (salario_atual*0.15)
    print(f'\nSeu salário foi atualizado de R${salario_atual:.2f} para R${novo_salario:.2f}.\n')