# Gerar cinco números aleatórios e colocar uma tupla
# Depois disso, mostrar a listagem de números gerados e também indique o maior e o menor número

from time import sleep
from random import randint
numeros = tuple(randint(0, 10) for c in range(5))
print('Serão sorteados 5 números... e será mostrado o maior e o menor! ')
sleep(1)
print('Pensando...')
sleep(1.2)
print('Calculado! ')
sleep(0.5)
print(f'Os números escolhidos foram: {numeros}')
print(f'O maior número foi {max(numeros)}')
print(f'O menor número foi {min(numeros)}')
