import math

# Arredondar usando biblioteca Math

try:
    num = float(input('Digite um número: '))

    a = math.trunc(num)
    print(f'A porção inteira de {num} é {a}')

except ValueError:
    print('Digite um número válido! ')