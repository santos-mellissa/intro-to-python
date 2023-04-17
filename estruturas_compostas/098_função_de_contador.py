"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
- De 1 até 10, de 1 em 1
- De 10 até 0 de 2 em 2
- Uma contagem personalizada"""

from time import sleep


def contador(i, f, p):
    print('\n')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f:
        print(f'Contando de {i} até {f} de {p} em {p}:\n')
        p *= -1
        if i == 0:
            f -= 2
        f -= 1
    else:
        print(f'Contando de {i} até {f} de {p} em {p}:\n')
        f += 1
    for num in range(i, f, p):
        print(num, end=' ')
        sleep(1)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('\nAgora é sua vez de personalizar a contagem!')
while True:
    inicio = int(input('\nEntre com o início da contagem: '))
    fim = int(input('Entre com o fim da contagem: '))
    passo = int(input('Qual será o passo? '))
    contador(inicio, fim, passo)
    cond = str(input('\nQuer continuar? [S/N]: ')).strip().upper()[0]
    while cond not in 'SN':
        cond = str(input('\nQuer continuar? [S/N]: ')).strip().upper()[0]
    if cond == 'N':
        break
