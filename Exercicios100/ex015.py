d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km foram rodados? '))
v = d * 60 + km * 0.15
print(f'Valor a ser pago: R${v:.2f}')