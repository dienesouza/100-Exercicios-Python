from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print(f'O ângulo {angulo} tem o SENO de {seno:.2f} \ntem o COSSENO de {coss:.2f} \ne a TANGENTE de {tang:.2f}')