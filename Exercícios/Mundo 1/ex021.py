# Ler o nome da pessoa e falar o primeiro e último nome

try:
    print(' --- Saiba o seu primeiro e último nome --- ')
    nome = input('Digite seu nome: ').split()
    print(f'\nSeu primeiro nome é {nome[0]}')
    print(f'Seu último nome é {nome[-1]}')
          
except ValueError:
    print('Digite um nome válido! ')
