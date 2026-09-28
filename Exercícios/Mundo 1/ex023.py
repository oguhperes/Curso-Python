# Radar, se ultrapassar 80km/h, multa. R$ 7,00 para cada Km a mais

try:
    print(' \n--- Radar --- ')
    velocidade = float(input('Velocidade: '))
    if velocidade > 80:
        excedido = velocidade - 80
        multa = excedido * 7
        print(f'Você passou {excedido} Km/H do limite! Sua multa será de R$ {multa:.2f}')
except ValueError: 
    print('Digite um número válido! ')