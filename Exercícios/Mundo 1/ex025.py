# Viagem menos de 200km R$ 0.50/km. Mais de 200km R$ 0.45/km

try:
    print(' --- Qual valor da passagem? --- ')
    viagem = float(input('Digite a distância (Km): '))
    if viagem <= 200:
        valor_passagem = viagem * 0.5
        print(f'Para sua viagem de {viagem} Km, você irá pagar R$ {valor_passagem:.2f}')
    else:
        valor_passagem = viagem * 0.45
        print(f'Para sua viagem de {viagem}Km, você irá pagar R$ {valor_passagem:.2f} ')

except ValueError:
    print('Digite um número válido! ')
