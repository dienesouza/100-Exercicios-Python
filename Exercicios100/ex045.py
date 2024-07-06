import random
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

lista = ['Pedra', 'Papel', 'Tesoura']

pedra = 0
papel = 1
tesoura = 2

computador = random.randint(0, 2)

print(f'''Computador jogou {lista[computador]}
Jogador jogou {lista[jogador]}''')

#quando o computador ganha:
if computador == pedra and jogador == tesoura or computador == papel and jogador == pedra or computador == tesoura and jogador == papel:
    print('COMPUTADOR VENCE')
elif jogador == pedra and computador == tesoura or jogador == papel and computador == pedra or jogador == tesoura and computador == papel:
    print('JOGADOR VENCE')
