# Computador escolhe número random, jogador precisa tentar adivinhar até acertar
# No final mostrar quantos palpites foram necessários para vencer

import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha_computador = random.choice(lista)
escolha_usuario = ''
counter = 0
while escolha_usuario != escolha_computador:
    escolha_usuario = int(input('\nDigite um número entre 0 e 10: '))
    if escolha_usuario != escolha_computador:
        print(f'Você errou! ')
        counter += 1
print(f'Você acertou e precisou de {counter} tentativas')