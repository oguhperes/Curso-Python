# Mostrar seu primeiro e último nome

try:
    nome = input('Digite seu nome completo: ').split()
    print(f'Seu primeiro nome é {nome[0]} e seu último nome é {nome[-1]}\n')
          
except ValueError:
    print('Digite um nome válido! ')
