p = float(input('Digite o valor do produto: R$'))
v = p - (p * 10/100)
par = p + (p * 8/100)
print(f'Valor do produto pago à vista (10% de desconto): R${v:.2f} \nValor do produto parcelado (aumento de 8%): R${par:.2f}')