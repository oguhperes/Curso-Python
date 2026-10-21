# Crie um programa onde o usuário possa digitar vários valores numéricos e 
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final serão exibidos todos os valores únicos digitados
# em ordem crescente

number_list = list()
while True:
    quest = (int(input('Digite um valor: ')))
    if quest not in number_list:
        number_list.append(quest)
        print('Valor adicionado com sucesso... ')
        choice = input('Quer continuar? [S/N] ').lower()
        if choice == 's':
            continue
        else:
            print('-=' * 30)
            print(f'Você digitou os valores {number_list}')
            break
    else:
        print('Valor duplicado! Não foi adicionado... ')
        choice = input('Quer continuar? [S/N] ').lower()
        if choice == 's':
            continue
        else:
            print('-=' * 30)
            print(f'Você digitou os valores {number_list}')
            break
