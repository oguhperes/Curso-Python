# Ler frase, mostrar quantas vezes 'a' aparece, em que posição primeiro, e ultima posição


try:
    frase = input('Escreva uma frase: ').lower().strip()
    quantidade_a = frase.count('a')
    primeiro_a = frase.find('a') + 1
    ultimo_a = frase.rfind('a') + 1

    print(f'\nSua frase tem {quantidade_a} A')
    print(f'O primeiro A da sua frase está na posição {primeiro_a}')
    print(f'O último A da sua frase está na posição {ultimo_a}')
except ValueError:
    print('Digite um número válida! ')
