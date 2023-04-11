"""Faça um programa que leia a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número digitado for negativo."""

num = 0
c = 1

while True:
    num = int(input('\nEntre com um número para saber sua tabuada: '))
    if num > 0:
        print('-'*30)
        while num > 0 and c < 11:
            print(f'{num} x {c} = {num*c}')
            c += 1
        print('-'*30)
        c = 1
    if num < 0:
        break
print('\nPrograma encerrado.\n')
