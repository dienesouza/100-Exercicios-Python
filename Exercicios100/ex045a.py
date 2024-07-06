from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
\033[1m[ 0 ] PEDRA\033[m
\033[1;34m[ 1 ] PAPEL\033[m
\033[1;31m[ 2 ] TESOURA\033[m''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=' * 15)
print(f'O computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 15)

# comp jogou PEDRA
if computador == 0:
    if jogador == 0:
        print('\033[1mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1mJOGADOR\033[m VENCE!')
    elif jogador == 2:
        print('\033[1mCOMPUTADOR\033[m VENCE!')
    else:
        print('\033[1;37mJOGADA INVÁLIDA!\033[m')

#comp jogou PAPEL
elif computador == 1:
    if jogador == 0:
        print('\033[1mCOMPUTADOR\033[m VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('\033[1mJOGADOR\033[m VENCE!')
    else:
        print('\033[1;37mJOGADA INVÁLIDA!\033[m')

#comp jogou TESOURA
elif computador == 2:
    if jogador == 0:
        print('\033[1mJOGADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1mEMPATE!\033[m')
    else:
        print('\033[37;1mJOGADA INVÁLIDA!\033[m')