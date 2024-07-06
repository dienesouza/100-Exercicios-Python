from time import sleep
velocidade = float(input('Informe a velocidade atual do carro: '))
if velocidade > 80:
    print(f'O limite de velocidade de 80 Km/h foi excedido. Calculando multa...')
    sleep(3)
    print(f'Você será multado em R${(velocidade - 80) * 7:.2f} \nLembre-se se dirigir com segurança. Tenha um bom dia!')
else:
    print('Obrigado. Tenha um bom dia! Dirija com segurança.')