"""Crie um programa que faça o computador jogar Jokenpô com você."""

import random
print ("\nVAMOS JOGAR PEDRA, PAPEL E TESOURA!")
a = int(input("\nConsidere:\n1 = Pedra\n2 = Papel\n3 = Tesoura\n\nAgora, vamos escolher:\n--> "))
b = random.randint(1,3)
if a in (1,2,3):
    print (f'--> {b}')
    if a == b:
        print ("\nEMPATE!\n")
    elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        print ("\nVOCÊ PERDEU!\n")
    else:
        print ("\nVOCÊ GANHOU!\n")
else:
    print('\nOpção inválida.\n')
