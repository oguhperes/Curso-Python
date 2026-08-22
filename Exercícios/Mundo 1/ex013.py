import math

# seno cosseno e tangente

try:
    angulo = float(input('Ângulo: '))

    rad = math.radians(angulo)

    seno = math.sin(rad)
    cosseno = math.cos(rad)
    tangente = math.tan(rad)

    print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
    print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
    print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f}')

except ValueError:
    print('Digite um número válido! ')