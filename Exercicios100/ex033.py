print('Informe três valores e direi o maior e o menor deles.')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 < n2 < n3:
    print(f'O MENOR valor entre {n1}, {n2} e {n3} é {n1}')
if n2 < n1 < n3:
    print(f'O MENOR valor entre {n1}, {n2} e {n3} é {n2}')
if n3 < n2 < n1:
    print(f'O MENOR valor entre {n1}, {n2} e {n3} é {n3}')
if n3 > n2 > n1:
    print(f'O MAIOR valor entre {n1}, {n2} e {n3} é {n3}')
if n2 > n1 > n3:
    print(f'O MAIOR valor entre {n1}, {n2} e {n3} é {n2}')
if n1 > n2 > n3:
    print(f'O MAIOR valor entre {n1}, {n2} e {n3} é {n1}')
