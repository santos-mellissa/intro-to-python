"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

lista = []
qtd_valores = 0

for qtd_valores in range(0,5):
    num = int(input('Entre com um número: '))
    if num not in lista:
        if qtd_valores == 0 or num > lista[-1]:
            lista.append(num)
        else:
            pos = 0
            while pos < len(lista):
                if num <= lista[pos]:
                    lista.insert(pos,num)
                    break
                pos += 1
print(f'\nValores distintos informados ordenados: {lista}\n')
