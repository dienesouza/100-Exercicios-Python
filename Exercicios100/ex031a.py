distancia = float(input('Informe a distância da viagem: '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'O preço da passagem será de R${preço:.2f}')