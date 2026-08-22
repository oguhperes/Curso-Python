
print(' --- Gerador de Tabuada --- ')

try:
    n1 = int(input('Digite um número: '))

    print(f'Tabuada do número {n1}')

    for i in range(1, 11):
        resultado = n1 * i

        print(f'{n1} x {i} = {resultado}')

except ValueError:
    print('Digite um número válido! ')
