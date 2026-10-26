# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso mostre: 
# Quantos números foram digitados
# A lista de valores ordenada de forma decrescente
# Se o valor 5 foi digitado e está na lista ou não

list = list()
while True:
    quest = int(input('Digite um número: '))
    list.append(quest)
    option = input('Quer continuar? [S/N] ').lower()
    while option not in 'sn':
        print('Digite uma opção válida! ')
        option = input('Quer continuar? [S/N] ').lower()
    if option == 's':
        continue
    else:
        print('-=' * 30)
        print(f'Foram digitados {len(list)} números')
        print('Lista em ordem descrescente: ', end='')
        print(sorted(list, reverse=True))
        if 5 in list:
            print('O número cinco foi digitado! ')
        else:
            print('O número cinco não foi digitado! ')
        break

