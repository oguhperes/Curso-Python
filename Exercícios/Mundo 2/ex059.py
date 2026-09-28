# Ler vários números inteiros. No final da execução 
# mostre a média e qual foi o maior e menor valor entre todos os valores
# E perguntar se o usuario quer ou não digitar mais valores

soma = 0
contador = 0
maior = 0
menor = 0
num = 0

while True:
    try:
        while num != 9999:
            num = int(input('\nDigite um número inteiro (Digite 9999 para encerrar): '))
            if num != 9999:
                contador += 1
                soma += num
                media = soma / contador
                if contador == 1:
                    menor = num
                    menor = num
                if num > maior:
                        maior = num
                if num < menor:
                        menor = num
        print(f'\nA média dos números é {media:.2f}',end='')
        print(f', o maior número foi {maior} e o menor foi {menor}')
        resposta  = input('Você quer continuar? [S/N] ').lower()
        if resposta == 's':
            num = menor
            continue
        else:
            break


    except ValueError:
        print('Digite um número válido! ')