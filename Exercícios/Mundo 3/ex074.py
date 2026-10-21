# Criar um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (ordem crescente)
# sem usar (sort). No final mostre a lista ordenada

c = 0
numbers_list = list()
while True:
    quest = int(input('Digite um número: '))
    c += 1
    if c == 1:
      numbers_list.append(quest)
      print(f'Adicionado na posição 0 na lista')
    else:
        if quest in numbers_list:
            print('Número repetido! ')
            c -= 1
            continue
        else:
            for i in numbers_list:
                position = numbers_list.index(i)
                if quest < i:
                    numbers_list.insert(position, quest)
                    print(f'Adicionado na posição {numbers_list.index(quest)} na lista')
                    break
                if quest > max(numbers_list):
                    numbers_list.append(quest)
                    print(f'Adicionado na posição {numbers_list.index(quest)} na lista')
                    break
    if c == 5:
        break
print('-=' * 30)
print(numbers_list)