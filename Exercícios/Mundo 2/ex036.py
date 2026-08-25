# Verificar se é possivel fazer um triângulo com 3 retas e mostrar que tipo de triangulo sera formado
# Equilátero: todos lados iguais
# Isóceles: dois lados iguais 
# Escaleno: todos lados diferentes

while True:
    try:
        r1 = float(input('\nPrimeira reta: '))
        r2 = float(input('Segunda reta: '))
        r3 = float(input('Terceira reta: '))

        if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
            print('Não é possível criar um triângulo! Tente novamente! ')
            continue

        if r1 == r2 and r2 == r3:
            print('Esse triângulo é equilátero! ')

        elif r1 != r2 and r2 != r3 and r1 != r3:
            print('Esse triângulo é Escaleno! ')

        else:
            print('Esse triângulo é Isóceles! ')

        break

    except ValueError:
        print('Digite um número válido! ')
