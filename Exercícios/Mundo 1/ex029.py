# Ler 3 retas e falar se é possivel fazer um triângulo

try:
    print(' --- É possivel fazer um triangulo? --- ')
    r1 = float(input('Primeira reta: '))
    r2 = float(input('Segunda reta: '))
    r3 = float(input('Terceira reta: '))

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('É possível criar um triângulo! ')

    else:
        print('Não é possível criar um triângulo! ')

except ValueError:
    print('Digite um numero válido')