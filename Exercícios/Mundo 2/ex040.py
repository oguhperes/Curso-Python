# Contagem regressiva para estouro de fogos de artifício, de 10 até 0, com pausa de 1segundo entre

from time import sleep


print(' \n--- Contagem Regressiva ---')
for i in range(10, 0-1, -1):
    sleep(1)
    print(i)
print('FOGOS!!!!!')
