# Programa que leia nome e peso de várias pessoas, guardando em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas 
# Uma listagem com as pessoas mais leves

names = []
count = 0
heavy_names = []
light_names = []
maior_peso = 0
menor_peso = 0
while True:
    count += 1
    name = input('Nome: ')
    weight = float(input('Peso: '))
    names.append([name, weight])
    if count == 1:
        maior_peso = weight
        menor_peso = weight
    else:
        if weight > maior_peso:
            maior_peso = weight
        if weight< menor_peso:
            menor_peso = weight
    quest = input('Quer continuar? [S/N] ').lower().strip()
    while quest not in 'sn' or quest == '':
        print('Digite uma opção válida! ')
        quest = input('Quer continuar? [S/N] ').lower().strip()
    if quest == 's':
        continue
    else:
        break
for c in names:
    if c[1] == maior_peso:
        heavy_names.append(c[0]) 
    if c[1] == menor_peso:
        light_names.append(c[0])
print('-=' * 30)
print(f'Foram cadastradas {count} pessoas. ')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {heavy_names} ')
print(f'O menor peso foi de {menor_peso}Kg. Peso de {light_names} ')
 