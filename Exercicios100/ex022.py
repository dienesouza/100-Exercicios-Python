nome = str(input('Digite seu nome completo: ')).strip()
pnome = nome.split()
print(f'Seu nome em maiúsculas: {nome.upper()} \nSeu nome em minúsculas: {nome.lower()} \nSeu nome tem ao todo {len(nome) - nome.count(" ")} letras \nSeu primeiro nome é {pnome[0]} e tem {len(pnome[0])} letras')