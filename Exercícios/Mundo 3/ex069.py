# Ler 8 números e guardar eles em uma Tupla, no final mostrar:
# Quantas vezes o número 9 apareceu
# Em que posição foi digitado o primeiro 3
# Quais foram os números pares

print('=====================')
print('Verificação númeral! ')
print('=====================')
numbers_list = tuple(int(input('Digite um número:')) for c in range(8))
if 9 in numbers_list:   
    print(f'O número nove apareceu {numbers_list.count(9)} vezes! ')
else:
    print('O número 9 não foi digitado.')
if 3 in numbers_list:
    print(f'A primeira posição que o número três apareceu foi na posição número {numbers_list.index(3) + 1}')
else:
    print('O número 3 não foi digitado.')
print('Números pares:', end=' ')
for i in numbers_list:
    if i % 2 == 0:
        print(i, end=', ')
