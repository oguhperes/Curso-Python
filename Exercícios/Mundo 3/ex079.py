
# Criar um programa em que o usuário pode digitar sete valores e cadastra-los
# em uma única lista que mantenha separados os valores pares e ímpares
# No final, mostre os valores pares e ímpares em ordem crescente

valores = [[], []]
for c in range(0, 7):
    number = int(input(f'Digite o {c + 1}º número valor: '))
    if number % 2 != 0:
        valores[0].append(number)
    if number % 2 == 0:
        valores[1].append(number)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(valores[1]) }')
print(f'Os valores ímpares digitados foram: {sorted(valores[0]) }')