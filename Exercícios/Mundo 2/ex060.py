# Ler  vários números... O programa só para quando o usuario digita
# 999. No final mostre quantos números foram digitados e qual foi a soma

contador = 0
soma = 0
while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    if num == 999:
        break
    soma += num
    contador += 1
print(f'Você escreveu {contador} números, que somados dão {soma}')