"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

# Cria a tupla de números por extenso de 0 a 20
num_em_extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

print('\n')

# Inicia o loop para certificar de que a entrada será entre 0 e 20
while True:
        num = int(input('Entre com um número (de 0 a 20) para saber como escrevê-lo por extenso: '))
        if 0 <= num <= 20: # Finaliza o loop se a entrada está entre 0 e 20
                break 
        print('Entrada inválida.', end= '')
print(f'\n{num} escrito por extenso é: {num_em_extenso[num]}\n') # Referencia a tupla e indica a posição da palavra
