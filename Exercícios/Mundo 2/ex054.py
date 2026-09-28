# Ler o número e mostrar o fatorial (usando while)

try:
    contador = 0
    fatorial = 1
    r = int(input('Digite um número: '))
    while contador < r:
        contador +=1
        fatorial *= contador
    print(f'O fatorial de {r} é {fatorial}')
except ValueError:
    print('Digite um número válido! ')