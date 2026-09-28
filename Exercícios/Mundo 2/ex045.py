# Ler o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

while True:
    try:
        primeiro_termo = int(input('\nDigite o primeiro número da PA: '))
        razao = int(input('Digite a razão: '))
        ultimo_numero = primeiro_termo + (razao * 10)
        for numero in range(primeiro_termo, ultimo_numero, razao):
            print(numero)
        break
    except ValueError:
        print('Digite um número válido! ')