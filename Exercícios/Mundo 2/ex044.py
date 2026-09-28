# Ler seis números inteiros e mostrar a soma apenas daqueles que forem
# pares. Se for ímpar desconsidere-o

s = 0
try:
    for i in range(1, 7):
        numero = int(input('Digite um número inteiro: '))
        if numero % 2 == 0:
            s += numero
    print(f'A soma dos números pares deu {s}')

except ValueError:
    print('Digite um número válido! ')