#desafio 2.0 - ler se é homem ou mulher
from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
sexo = int(input('''Qual o seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino
Escolha: '''))

ano_atual = date.today().year
idade = ano_atual - nasc

if nasc < 18 and sexo == 1:
    print(f'Quem nasceu em {nasc} tem {idade} anos.')
    print(f'Portanto você ainda não tem idade para se alistar.')
    print(f'Você se alistará em {18 - idade} anos, no ano de {ano_atual + (18 - idade)}.')

elif nasc == 18 and sexo == 1:
    print(f'Quem nasceu em {nasc} tem {idade} anos.')
    print(f'Você deve se alistar IMEDIATAMENTE!')

elif nasc > 18 and sexo == 1:
    print(f'Quem nasceu em {nasc} tem {idade} anos.')
    print(f'Seu tempo de alistamento já passou há {idade - 18} anos. Seu ano de alistamento foi em {ano_atual - (idade - 18)}.')

elif sexo == 2:
        print('Por ser mulher, você não precisa se alistar.')
