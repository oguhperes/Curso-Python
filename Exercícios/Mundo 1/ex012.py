import math

# Calcular hipotenusa

n1 = float(input('Cateto 1: '))
n2 = float(input('Cateto 2: '))

hip = math.hypot(n1, n2)

print(f'A hipotenusa é {hip:.2f}')
