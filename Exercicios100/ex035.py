print('-=' * 14)
print('Analisador de Triângulos')
print('-=' * 14)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r2 and r1 + r3 > r2:
    print('SIM, esses 3 valores de reta podem formar um triângulo!')
else:
    print('NÃO, esses 3 valores de reta não podem formar um triângulo.')