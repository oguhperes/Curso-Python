# Ler se tem silva no nome


try:
    print('Seu nome tem Silva?\n')
    nome = input('Digite o nome: ').lower().split()
    if 'silva' in nome:
       print('Seu nome tem silva! ')

    else:
       print('Seu nome não tem silva! ')
except ValueError:
    print('Digite um nome válido! ')
