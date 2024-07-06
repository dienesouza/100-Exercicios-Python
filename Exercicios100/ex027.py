nome = str(input('Digite seu nome completo: ')).strip()
nome2 = nome.split()
print(f'Prazer em te conhecer! \nSeu primeiro nome é {nome2[0]} \nSeu último nome é {nome2 [-1]}')
#o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.