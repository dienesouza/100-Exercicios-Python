ano = int(input('Me diga um ano e direi se ele é bissexto: '))
if ano % 4 == 0:
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')