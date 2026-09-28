# Ler o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão (usando while)

try:
    primeiro_termo = int(input('Digite o primeiro termo da PA: '))
    razao = int(input('Digite a razão da PA: '))
    termo = primeiro_termo
    contador = 0
    
    while contador < 10:
        print(termo)
        termo += razao
        contador += 1
except ValueError:
    print('Digite um número válido! ')

