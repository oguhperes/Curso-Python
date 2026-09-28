# Pedra, Papel, Tesoura
import random
from time import sleep
while True:
    try:
        print('\n --- Pedra, Papel, Tesoura --- ')
        lista = ['pedra', 'papel', 'tesoura']
        escolha_usuario = input('Sua escolha: ').lower()
        escolha_computador = random.choice(lista)
        sleep(1)
        print('   Carregando...\n')
        sleep(1)
        print(f'Escolha do computador foi {escolha_computador.capitalize()}')
        sleep(0.5)
        if escolha_computador == escolha_usuario:
            print('EMPATE!!! ')
        elif (
            (escolha_usuario == 'tesoura' and escolha_computador == 'papel') or 
            (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or 
            (escolha_usuario == 'papel' and escolha_computador == 'pedra')
        ):
            print('VOCÊ GANHOU!!! ')

        else:
            print('VOCÊ PERDEU!!! ')
        break



    except ValueError:
        print('Digite um número válido! ')
