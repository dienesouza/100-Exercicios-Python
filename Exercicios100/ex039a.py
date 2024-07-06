from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year

idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento.')
    print(f'Seu alistamento será em {atual + (18 - idade)}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {atual - (idade - 18)}.')
