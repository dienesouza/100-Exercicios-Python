from datetime import date
print('\033[1mConfederação Nacional de Natação\033[m')

nasc = int(input('Digite o ano de nascimento do atleta: '))

ano_hoje = date.today().year

idade_atleta = ano_hoje - nasc

if idade_atleta <= 9:
    print('Sua categoria é MIRIM')
elif idade_atleta >= 10 and idade_atleta <= 14:
    print('Sua categoria é INFANTIL')

elif idade_atleta >= 15 and idade_atleta <= 19:
    print('Sua categoria é JUNIOR')

elif idade_atleta == 20:
    print('Sua categoria é SÊNIOR')

else:
    print('Sua categoria é MASTER')