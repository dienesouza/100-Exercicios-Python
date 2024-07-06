from time import sleep
n = int(input('Me diga um número aleatório: '))
print('ANALISANDO...')
sleep(1)
if n % 2 == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é ímpar.')