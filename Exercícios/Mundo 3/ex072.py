# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas 
# Posições na lista

numbers_list = list()
for c in range(0, 6):
    numbers_list.append(int(input(f'Digite um valor para a Posição {c + 1}: ')))
print('=-' * 30)
print(f'Você digitou os valores {numbers_list}')
print(f'O maior valor digitado foi {max(numbers_list)} na posição {numbers_list.index(max(numbers_list)) + 1}')
print(f'O menor valor digitado foi {min(numbers_list)} na posição {numbers_list.index(min(numbers_list)) + 1}')