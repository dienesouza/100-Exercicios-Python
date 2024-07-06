print('-=' * 14)
print('\033[1mAnalisador de Triângulos\033[m')
print('-=' * 14)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('NÃO, esses 3 valores de reta não podem formar um triângulo.')

#equilátero
elif r1 == r2 and r1 == r3 and r2 == r3:
    print('SIM, esses 3 valores de reta podem formar um triângulo! \nO triângulo é \033[1;34mEquilátero\033[m')

#isósceles
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('SIM, esses 3 valores de reta podem formar um triângulo! \nO triângulo é \033[1;34mIsósceles\033[m')

#escaleno
else:
    print('SIM, esses 3 valores de reta podem formar um triângulo! \nO triângulo é \033[1;34mEscaleno\033[m')
