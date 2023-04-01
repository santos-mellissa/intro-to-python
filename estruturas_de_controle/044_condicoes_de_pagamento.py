"""Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de
pagamento:
- à vista (dinheiro/cheque): 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros """

val_produto = float(input('\nInforme o valor do produto:\n--> '))
forma_pgto = int(input('\nEscolha uma opção de 1 a 4 de acordo com a forma de pagamento: \n1. à vista (dinheiro/cheque)\n2. à vista no cartão: 5% de desconto\n3. em até 2x no cartão\n4. 3x ou mais no cartão\n--> '))
lista = [1,2,3,4]

if forma_pgto in lista:
    if forma_pgto == 1:
        print(f'\nValor total: R${val_produto - (val_produto * 0.10):.2f}. Você recebeu um desconto de R${val_produto * 0.10:.2f}.\n')
    elif forma_pgto == 2:
        print(f'\nValor total: R${val_produto - (val_produto * 0.05):.2f}. Você recebeu um desconto de R${val_produto * 0.05:.2f}.\n')
    elif forma_pgto == 3:
        print(f'\nValor total: R$ {val_produto}.')
    else:
        print(f'\nValor total: R${val_produto + (val_produto * 0.20):.2f}. Juros aplicado: R${val_produto * 0.20:.2f}.\n')
else:
    print(f'\nOpção inválida.\n')
