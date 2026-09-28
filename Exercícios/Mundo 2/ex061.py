# Mostrar a tabuada de varios números. O programa será interrompido quando o número solicitado for negativo
from time import sleep
import ex030
i = 0
while True:
    sleep(0.4)
    print(' \n--- Gerador de Tabuada --- ')
    num = int(input('\nDigite um número inteiro: '))
    if num < 0:
        sleep(0.7)
        print('Saindo do sistema! Até logo...')
        break
        
    while i < 10:
        i += 1
        mult = i * num
        print(f'{i} x {num} = {mult}')
    i = 0