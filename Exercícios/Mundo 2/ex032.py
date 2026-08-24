# Ler dois números inteiros e compare-os, o número x é maior, o número y é menos, não existe valor maior, os dois são iguais

try:
    print(' --- Comparação númeral --- ')
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))

    maior = max(n1, n2)
    menor = min(n1, n2)

    if n1 == n2:
        print('Os números são iguais! ')

    else:
        print(f'O número {maior} é o maior! ')
        print(f'O número {menor} é o menor! ')

except ValueError:
    print('Digite um número válido! ')