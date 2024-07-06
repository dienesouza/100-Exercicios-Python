n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('Você está REPROVADO')

elif m >= 5 and m <= 6.9:
    print('Você está de RECUPERAÇÃO')

else:
    print('Você está APROVADO')