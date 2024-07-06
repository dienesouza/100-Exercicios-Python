print('\033[1mDigite dois números inteiros e te direi qual é o maior!\033[m')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O \033[1;33mprimeiro valor \033[mé \033[1;34mmaior.')
elif n1 < n2:
    print('O \033[1;33msegundo valor \033[mé \033[1;34mmaior.')
else:
    print('\033[1;33mNão existe \033[mvalor maior, os dois são \033[1;34miguais.')
#poderia ser elif tbm
#elif n1 == n2:
