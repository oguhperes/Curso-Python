# Pedra, Papel, Tesoura
import random

while True:
    try:
        print('\n --- Pedra, Papel, Tesoura --- ')
        lista = ['Pedra', 'Papel', 'Tesoura']
        
        escolha_aleatorio = random.choice(lista)
        escolha_usuario = str(input('Pedra, papel ou tesoura: ')).title().strip()
        if escolha_usuario not in lista:
            print('Digite uma palavra válida! ')

        else:
            print(f'Escolha aleatória: {escolha_aleatorio}')
            if escolha_aleatorio == escolha_usuario:
                print("Empate! ")

            elif (
                (escolha_usuario == 'Tesoura' and escolha_aleatorio == 'Papel') or
                (escolha_usuario == 'Papel' and escolha_aleatorio == 'Pedra') or
                (escolha_usuario == 'Pedra' and escolha_aleatorio == 'Tesoura')
            ):
                print('Você ganhou! ')

            else:
                print('Você perdeu! ')
            break


    except ValueError:
        print('Digite um número válido! ')
