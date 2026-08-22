import random

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

nomes = [n1, n2, n3, n4]
# Nomes aleatorios

escolhido = random.choice(nomes)

print(f'O escolhido é {escolhido}')