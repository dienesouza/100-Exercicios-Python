import datetime
from datetime import date
idade = int(input('Digite seu ano de nascimento: '))

current_date = date.today().year

idade = current_date - idade

quanto_falta = 18 - idade
quanto_passou = idade - 18

if idade == 17:
    print(f'Falta {quanto_falta} ano para você se alistar no exército.')

elif idade < 18:
    print(f'Faltam {quanto_falta} anos para você se alistar no exército.')

elif idade == 18:
    print(f'Você já pode de se alistar no exército.')

elif idade == 19:
    print(f'Seu tempo de alistamento já passou há {quanto_passou} ano.')

else:
    print(f'Seu tempo de alistamento já passou há {quanto_passou} anos.')
