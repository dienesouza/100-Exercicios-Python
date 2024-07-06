alt = float(input('Qual a sua altura? (m) '))
peso = float(input('Qual o seu peso? (kg) '))

imc = peso / (alt ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está \033[4;31mAbaixo do Peso\033[m.')

elif imc > 18.5 and imc < 25:
# elif 18.5 >= imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você está com o \033[4;32mPeso Ideal\033[m.')

elif imc > 25 and imc < 30:
#elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você está com \033[4;33m Sobrepreso\033[m.')

elif imc > 30 and imc < 40:
#elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f}. Você está com \033[4;33mObesidade\033[m.')

else:
    print(f'Seu IMC é {imc:.1f}. Voce está com \033[4;31mObesidade Mórbida\033[m')
