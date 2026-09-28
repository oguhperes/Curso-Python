# Ler um número inteiro qualquer e mostrar a quantidade de digitos de uma sequência de Fibonacci

try:
    print(' === Sequência de Fibonacci === ')
    quantidade_de_numeros = int(input('Quantos termos quer mostrar: '))
    contador = 0
    a = 0
    b = 1
    while contador < quantidade_de_numeros:
        contador += 1
        print(a)
        a, b = b, b + a
except ValueError:
    print('Digite um número válido! ')