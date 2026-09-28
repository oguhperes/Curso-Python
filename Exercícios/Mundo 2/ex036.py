# Verificar se é possivel fazer um triângulo com 3 retas e mostrar que tipo de triangulo sera formado
# Equilátero: todos lados iguais
# Isóceles: dois lados iguais 
# Escaleno: todos lados diferentes

while True:
    try:
        print('\n --- Verificação de Triângulo --- ')
        r1 = float(input('Primeira reta: '))
        r2 = float(input('Segunda reta: '))
        r3 = float(input('Terceira reta:'))
        if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
            if r1 == r2 and r2 == r3:
                print('É possível fazer um triângulo e ele é: Equilátero! ')
            elif r1 != r2 and r2 != r3 and r1 != r3:
                print('É possível fazer um triângulo e ele é: Escaleno! ')
            else:
                print('É possível fazer um triângulo e ele é: Escaleno! ')
            break
        else:
            print('Não é possível fazer um triângulo! ')
    except ValueError:
        print('Digite um número válido! ')