# Par ou Ímpar

try:
    print(' --- Par ou Ímpar ---')
    n1 = int(input('Digite um número: '))

    if n1 % 2 == 0:
        print(f'O número {n1} é par! ')

    else:
        print(f'O número {n1} é ímpar! ')

except ValueError:
    print('Digite um número válido! ')