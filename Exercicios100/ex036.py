print('Seja bem-vindo ao programa de impréstimos bancários da Dih!')

cval = float(input('Digite aqui o valor da casa desejada: '))
sal = float(input('Ótimo! Agora precisamos saber o valor do seu salário: '))
anos = int(input('Em quantos anos deseja parcelar? '))


#em quantos anos ele vai pagar:
# pm = cval / ((sal * 30/100) * 12)

parcelas = anos * 12
parcval = cval / parcelas

if parcval >= sal * 30/100:
    print('Infelizmente o valor da prestação mensal excedeu o limite de 30% do seu salário, não é possível realizar o empréstimo.')

else:
    print(f'É possível fazer o empréstimo, você pagará R${parcval:.2f} por mês.')
# print(f'valor das parcelas: {parcval}')