# Ler vários números inteiros. O programa só para quando digitar 999
# no final mostre quantos números foram digitados e qual doi a soma
# entre eles

try:
    contador = soma = num = 0
    while num != 999:
        num = int(input('\nDigite um número inteiro (Digite 999 para parar): '))
        if num != 999:
            soma += num
            contador += 1
    print(f'Foram digitados {contador} números... Que somados dão {soma}')
except ValueError:
    print('Digite um número válido! ')