# Radar, se ultrapassar 80km/h, multa. R$ 7,00 para cada Km a mais

try:
    print(' --- Radar --- \n')
    velocidade = float(input('Digite a velocidade: '))
    if velocidade <= 80:
        print('Você está dentro do limite! ')

    else:
        velocidade_excedida = velocidade - 80
        multa = velocidade_excedida * 7
        print(f'Você está acima do limite em {velocidade_excedida} Km/h e foi multado em R$ {multa:.2f}')

except ValueError: 
    print('Digite um número válido! ')
