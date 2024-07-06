print(f'{" LOJAS GUANABARA ":=^40}')
# O :^40 centraliza o texto em 40 espaços
# E :=^40 utiliza 40 espaços.
preço = float(input('Qual o preço do produto? R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] À vista em dinheiro/cheque: \033[33m210%\033[m de desconto
[ 2 ] À vista no cartão: \033[33m25%\033[m de desconto
[ 3 ] Em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cart ão: \033[33m20%\033[m de juros''')
# Com 3 aspas ''' vc pode ultilizar várias linhas

opção = int(input('Qual a condição de pagamento? '))

if opção == 1:
    total = preço - (preço * 10 / 100)

elif opção == 2:
    total = preço - (preço * 5 / 100)

elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')

elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f}')

else:
    total = preço
    print('\033[31mOPÇÃO INVÁLIDA\033[m de pagamento. Tente novamente.')

print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final')
