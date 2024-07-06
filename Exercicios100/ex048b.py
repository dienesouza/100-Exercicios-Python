soma = 0 #acumulador: soma um valor; acumula os valores, soma, multiplica o que precisar
cont = 0 #contador: soma +1; conta + 1
for c in range(1, 501, 2): #lê os nº ímpares
    if c % 3 == 0: #lê os múltiplos de 3
        cont = cont + 1 # conta os múltiplos de 3
        soma = soma + c # soma os valores dos nº múltiplos de 3
        # soma += c => da no mesmo
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
