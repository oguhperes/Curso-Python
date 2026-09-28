# Ler vários números inteiros. O programa só para quando digitar 999
# no final mostre quantos números foram digitados e qual doi a soma
# entre eles

try:
    contador = 0
    soma = 0
    num = 0
    while num != 999:
        num = int(input('\nDigite um número inteiro (Digite 999 para parar): '))
        contador += 1
        if num != 999:
            soma += num

    print(f'Foram digitados {contador - 1} números... Que somados dão {soma}')
except ValueError:
    print('Digite um número válido! ')