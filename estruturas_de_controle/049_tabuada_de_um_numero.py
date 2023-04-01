"""Refaça o desafio 009 (pasta fundamentos), mostrando a tabuada de um número que o usuário escolher,
só que agora, utilizando um laço for."""

num = int(input('\nEntre com um número para saber sua tabuada: '))

print(f'\n{"TABUADA":-^30}')
for c in range(1,11):
    print(f'{num} x {c} = {num*c}')
print('-'*30)