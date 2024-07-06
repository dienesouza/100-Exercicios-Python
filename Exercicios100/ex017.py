co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print(f'O valor da hipotenusa é {h:.2f}')
