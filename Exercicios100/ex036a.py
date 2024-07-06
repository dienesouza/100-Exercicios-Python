#versão do guanabara
casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? R$'))

prestac = casa / (anos * 12)
máximo = sal * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos')
print(f'a prestação será de R${prestac:.2f}')

if prestac <= máximo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')