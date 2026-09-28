# Ler o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão (usando while)
# e no final perguntar se o usuario quer mostrar mais termos, se sim, mostrar, se não... Não mostrar


while True:
    try:
        primeiro_termo = int(input('Digite o primeiro termo da PA: '))
        razao = int(input('Digite a razão da PA: '))
        ultimo_termo = (razao * 10) + primeiro_termo
        contador = primeiro_termo
        while contador < ultimo_termo:
            print(contador)
            contador += razao
        while True:
            pergunta = input('Você quer mostrar mais termos? [S/N] ').lower()
            if pergunta == 's':
                termo = int(input('Quantos mais quer mostrar: '))
                ultimo_termo_escolha = (razao * termo) + ultimo_termo
                contador = ultimo_termo
                while contador < ultimo_termo_escolha:
                    print(contador)
                    contador+= razao 
                    ultimo_termo = ultimo_termo_escolha
            else:
                break
    except ValueError:
        print('Digite um número válido! ')