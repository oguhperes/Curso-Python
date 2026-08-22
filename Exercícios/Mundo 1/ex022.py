# Adivinhar número entre 0 e 5

import random

try:
    while True:
        print(' \n--- Adivinhe um número entre 0 e 5 ---  ') 
        print(' ------ Digite 9 para sair ------')
        lista = [0, 1, 2, 3, 4, 5]
        n = random.choice(lista)
        chute = int(input('Seu número: '))

        if chute == n:
            print('Você acertou, parabéns! ')

        elif chute == 9:
            print('Saindo... até logo!')
            break

        else:
            print('Você errou! ')
           

except ValueError:
    print('Digite um número válido! ')