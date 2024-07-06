preco = float(input('Qual o preço do produto? R$'))
#condição de pagamento
print('''\033[1mFORMAS DE PAGAMENTO\033[m
[ 1 ] À vista em dinheiro/cheque: \033[33m210%\033[m de desconto
[ 2 ] À vista no cartão: \033[33m25%\033[m de desconto
[ 3 ] Em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cart ão: \033[33m20%\033[m de juros''')
# Com 3 aspas ''' vc pode ultilizar várias linhas

cp = int(input('Qual a condição de pagamento? '))

if cp == 1:
    print(f'Com o desconto de 10% o valor a ser pago agora é de R${preco - (preco * 10 / 100):.2f}')

elif cp == 2:
    print(f'Com o desconto de 5% o valor a ser pago agora é de R${preco - (preco * 10 / 100):.2f}')

elif cp == 3:
    print(f'Como não há desconto para a forma de pagamento selecionada, o valor a ser pago continua sendo de R${preco:.2f}')

elif cp == 4:
    print(f'Com juros de 20% o valor a ser pago agora é de R${preco + (preco * 20 / 100):.2f}')
