distancia = float(input('Informe a distância da viagem: '))
if distancia <= 200:
    print(f'O preço da passagem será de R${distancia * 0.50:.2f}')
else:
    print(f'O preço da passagem será de R${distancia * 0.45:.2f}')