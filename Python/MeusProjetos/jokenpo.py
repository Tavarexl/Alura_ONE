from random import randint
from time import sleep
opcoes = ('pedra', 'papel', 'tesoura')
contador = 0
while True:
    pc = opcoes[(randint(0, 2))]
    print(f'Você tem {contador} ponto(s)')
    vc = str(input('Digite "Pedra", "Papel" ou "Tesoura": ')).strip() .lower()
    if vc == pc:
        contador += 0
    elif vc == 'pedra':
        if pc == 'papel':
            contador -= 1
        elif pc == 'tesoura':
            contador += 1
    elif vc == 'papel':
        if pc == 'pedra':
            contador += 1
        elif pc == 'tesoura':
            contador -= 1
    elif vc == 'tesoura':
        if pc == 'papel':
            contador += 1
        elif pc == 'pedra':
            contador -= 1
    print(f'Você escolheu {vc} e o computador {pc}')
    print('-*'*20)