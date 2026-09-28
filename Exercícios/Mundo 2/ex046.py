# Ler um número inteiro e dizer se é primo ou não


while True:
    try:
        num = int(input('\nDigite um número inteiro: '))
        soma = 0

        for i in range(1, num + 1):
            if num % i == 0:
                soma += 1
        if soma == 2:
            print('Esse número é primo! ')

        else:
            print('Esse número não é primo')
        break

    except ValueError:
        print('Digite um número válido! ')