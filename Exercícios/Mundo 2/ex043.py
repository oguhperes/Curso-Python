# Tabuada do número escolhido

try:
    print('\n--- Tabuadas --- ')
    n1 = int(input('Digite um número: '))
    for numero in range(1, 11):
        resultado = n1 * numero
        print(f'{n1} x {numero} = {resultado}')

except ValueError:
    print('Digite um número válido! ')