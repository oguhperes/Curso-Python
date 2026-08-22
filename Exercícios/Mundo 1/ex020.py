# Ler frase, mostrar quantas vezes a aparece, em que posição primeiro, e ultima posição


try:
    nome = input('Digite uma frase: ').lower()
    print(f'Na sua frase tem {nome.count('a')} A ')
    print(f'O primeiro A aparece na posição {nome.find('a')}')
    print(f'O último A aparece na posição {nome.rfind('a')}')
except ValueError:
    print('Digite um número válida! ')
