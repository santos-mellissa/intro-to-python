# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('\nInsira seu salário atual: R$'))

salario_atual = salario+(salario*0.15)

print(f'\nSeu salário atualizado de R${salario:.2f} para R${salario_atual:.2f} com os 15% de aumento.\n')
