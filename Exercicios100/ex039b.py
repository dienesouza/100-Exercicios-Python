#versão do guanabara

from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year

idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o seu alistamento.')
    ano = atual + saldo
    print(f'Se alistamento será em {ano}')

elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
