# Ler o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lido

try:
    maior = 0
    menor = 0
    for i in range(1, 6):
        peso = float(input(f'Peso da {i}ª pessoa: '))
        if i == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print(f'O maior peso é {maior}Kg e o menor é {menor}Kg')

except ValueError:
    print('Digite um número válido! ')
        