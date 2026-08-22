
# Antecessor e sucessor

try:
    n1 = int(input('Digite um número: '))

    a = n1 - 1
    s = n1 + 1

    print(f'O antecessor de {n1} é {a} e o sucessor é {s}')

except ValueError:
    print('Digite um número válido! ')

