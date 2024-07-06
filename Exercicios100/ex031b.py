distancia = float(input('Informe a distância da viagem: '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O preço da passagem será de R${preço:.2f}')