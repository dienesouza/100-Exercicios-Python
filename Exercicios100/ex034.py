sal = float(input('Qual é o seu salário: R$'))
if sal <= 1250.00:
    sal2 = sal + (sal * 15 / 100)
else:
    sal2 = sal + (sal * 10 / 100)
print(f'O seu novo salário é de {sal2:.2f}')
