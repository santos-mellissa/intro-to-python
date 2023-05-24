def colorize(string, color):
    colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'end': '\033[m'
    }
    return f"{colors[color]}{string}{colors['end']}"


def leiaInt(num):
    while not num.isdigit():
        print(colorize('Entrada inválida, tente novamente.', 'red'))
        num = input('Entre com um número inteiro: ')
    return (num)

num = input('\nEntre com um número inteiro: ')
print(colorize(leiaInt(num), 'green'))
