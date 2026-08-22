# Viagem menos de 200km R$ 0,50/km. Mais de 200km R$ 0,45/km

try:
    print(' --- Qual valor da passagem? --- ')
    viagem = float(input('Digite a distância: '))
    

except ValueError:
    print('Digite um número válido! ')
