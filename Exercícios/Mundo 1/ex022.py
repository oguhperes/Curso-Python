# Adivinhar número entre 0 e 5

import random

while True:
    try:
        lista = [0, 1, 2, 3, 4, 5]
        print(' \n--- Adivinhe um número entre 1 e 5 ---  ')
        numero_aleatorio = random.choice(lista)
        numero_pessoa = int(input('Digite um número de 0 a 5: '))
        if numero_pessoa > 5 or numero_pessoa < 0:
            print('Digite um número válido! ')
            continue
        else:
            print(f'\nO número aleatório é {numero_aleatorio}')
            if numero_pessoa == numero_aleatorio:
                print('Você ganhou! ')
            else:
                print('Você perdeu! ')
            break

        
            

    except ValueError:
        print('Digite um número válido! ')