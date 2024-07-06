a = int(input('Primeiro valor: '))
b: int = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando qual é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O MENOR valor digitado foi {menor} \nO MAIOR valor digitado foi {maior}')
