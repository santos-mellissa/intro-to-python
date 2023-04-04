""" Crie um programa que leia dois valores e mostre o seguinte menu:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""

num_1 = float(input('\nEntre com o primeiro número: '))
num_2 = float(input('Entre com o segundo número: '))

menu = 1

while menu >= 1 and menu <= 5:
    menu = int(input('\nEscolha a operação que deverá ser realizada:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n--> '))
    if menu == 1:
        soma = num_1 + num_2
        print(f'\nO resultado da adição entre {num_1:.1f} e {num_2:.1f} é igual a {soma:.1f}.')
    elif menu == 2:
        mult = num_1 * num_2
        print(f'\nO resultado da multiplicação entre {num_1:.1f} e {num_2:.1f} é igual a {mult:.1f}.')
    elif menu == 3:
        if num_1 > num_2:
            print(f'\n{num_1:.1f} é maior que {num_2:.1f}.')
        elif num_2 > num_1:
            print(f'\n{num_2:.1f} é maior que {num_1:.1f}.')
        else:
            print(f'\nNão há maior número. {num_1:.1f} e {num_2:.1f} são dois números iguais!')
    elif menu == 4:
        num_1 = float(input('\nEntre com o primeiro número: '))
        num_2 = float(input('Entre com o segundo número: '))
    else:
        print('\nPrograma encerrado.\n')
        menu = 6
