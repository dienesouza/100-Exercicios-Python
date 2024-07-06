from random import randint
from time import sleep
print('*' * 55)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('*' * 55)
computador = randint(0, 5) # Faz o computador "PENSAR" em um número.
jogador = int(input('Em qual número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1) # O SLEEP faz o computador esperar, faz ele "dormir" por alguns segundos.
if jogador == computador:
    print(f'Isso mesmo, você ACERTOU! Eu pensei no número {computador}.')
else:
    print(f'Aha! Você PERDEU. Eu pensei no número {computador}.')