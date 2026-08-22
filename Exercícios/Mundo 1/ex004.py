
# Mostrar dobro, triplo e raiz quadrada
import math


try:
    n1 = float(input('Digite um número: '))
    raiz = math.sqrt(n1)
    d = n1 * 2
    t = n1 * 3

    print(f'O dobro de {n1} é {d} o triplo é {t} e a Raiz quadrada é {raiz:.2f}')

except ValueError:
    print('Digite um número válido! ')



