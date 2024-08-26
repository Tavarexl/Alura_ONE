from random import randint
from time import sleep
print('\033[34mSORTEIO DE SKIN by Japa\033[m')
esc = ('\033[31mCamila\033[m', '\033[33mTavares\033[m')
computador = randint(0,1)
print('''PARTICIPANTES:
\033[31mCamila\033[m
\033[33mTavares\033[m''')
print('-=' * 20)
sleep(4)
print('E o ganhador do sorteio foi...')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('{}!!'.format(esc[computador]))
sleep(10)