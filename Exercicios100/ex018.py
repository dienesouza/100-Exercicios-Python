import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
# se fosse importar apenas os 4 métodos, não precisaria por o math antes de cada um
print(f'O ângulo {angulo} tem o SENO de {seno:.2f} \no COSSENO de {coss:.2f} \ne a TANGENTE de {tang:.2f}')