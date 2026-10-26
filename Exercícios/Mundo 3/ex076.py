# Ler vários números e colocar em uma lista
# Após isso, crie duas listas extras que vão conter apenas os 
# valores pares e os ímpares
# Ao final mostre o conteúdo das três listas

lista = list()
par = list()
impar = list()

while True:
    quest = int(input('Digite um número: '))
    lista.append(quest)
    option = input('Quer continuar? [S/N] ').lower()
    while option not in 'sn':
        print('Digite um número válido! ')
        option = input('Quer continuar? [S/N] ')
    if option == 's':
        continue
    else:
        for c in lista:
            if c % 2 == 0:
                par.append(c)
            else:
                impar.append(c)
        print('-=' * 30)
        print(f'A lista completa é {lista}')
        print(f'A lista de pares é {par}')
        print(f'A lista de ímpares é {impar}')
        break




