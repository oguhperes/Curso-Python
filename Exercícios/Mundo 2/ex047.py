# Ler uma frase qualquer e dizer se ela é um palíndromo desconsiderando espaços

try:
    print('\n --- Sua frase é um palíndromo? --- ')
    frase = input('Digite uma frase: ').replace(' ', '').lower()
    frase_invertida = frase[::-1]
    if frase == frase_invertida:
        print('Essa frase é um palíndromo! ')
    else:
        print('Essa frase não é um palíndromo! ')
except ValueError:
    print('Digite um número válido! ')