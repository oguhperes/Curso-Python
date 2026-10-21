# Caixa Eletrônico. Perguntar qual vai ser o valor sacado (num inteiro) e o programa vai informar quantas cédulas 
# de cada valor serão entregues.
# Caixa possui cédulas de R$ 50.00, R$ 20.00, R$ 10.00, R$ 5.00, R$ 2.00 e R$ 1.00
from time import sleep

while True:
    try:
        print(' \n======== BANCO Z ======== ')
        print('\n --- Saque de dinheiro --- ')
        num = int(input('Digite um valor para sacar: ')) 

        notas_50 = num // 50
        sobra_50 = num % 50

        notas_20 = sobra_50 // 20
        sobra_20 = sobra_50 % 20

        notas_10 = sobra_20 // 10
        sobra_10 = sobra_20 % 10

        notas_5 = sobra_10 // 5
        sobra_5 = sobra_10 % 5

        notas_2 = sobra_5 // 2
        sobra_2 = sobra_5 % 2

        notas_1 = sobra_2 // 1
        sobra_1 = sobra_2 % 1
        sleep(0.5)
        print('====== Calculando...\n')
        sleep(2)

        print(f'Saque de R$ {num:.2f}')
        if notas_50 > 0:
            print(f'Notas 50: {notas_50}')
        if notas_20 > 0:
            print(f'Notas 20: {notas_20}')
        if notas_10 > 0:
            print(f'Notas 10: {notas_10}')
        if notas_5:
            print(f'Notas 5: {notas_5}')
        if notas_2:
            print(f'Notas 2: {notas_2}')
        if notas_1:
            print(f'Notas 1: {notas_1}')
        break

    except ValueError:
        print('Digite um número válido! ')