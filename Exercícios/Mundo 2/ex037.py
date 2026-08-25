# Calcular o imc e mostrar em qual categoria a pessoa se encaixa
# 18.5- Abaixo do peso
# Entre 18.5 e 25- Peso ideal
# 25 até 30- Sobrepeso
# 30 até 40- Obesidade
# Acima de 40- Obesidade mórbida

try:
    print('\n --- Cálculo Imc --- ')
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))

    if altura > 2.5:
        altura /= 100

    imc = peso / (altura * altura)

    if imc <= 18.5:
        print(f'Seu imc é {imc:.1f} e está abaixo do peso! ')

    elif imc <= 25:
        print(f'Seu imc é {imc:.1f} e está no peso ideal! ')

    elif imc <= 30:
        print(f'Seu imc é {imc:.1f} e está com sobrepeso! ')

    elif imc <= 40:
        print(f'Seu imc é {imc:.1f} e está com obesidade! ')

    else:
        print(f'Seu imc é {imc:.1f} e está com obesidade mórbida! ')

except ValueError:
    print('Digite um número válido! ')


        