# Ler nome e falar: letra maiúscula, minúsculas, letras ao todo, letras primeiro nome

try:
    name = input('Seu nome completo: ')
    print(name.upper())
    print(name.lower())
    print(f'Seu nome tem {len(name) - name.count(' ')} letras')
    print(f'Seu primeiro nome tem {len(name.split()[0])} letras')

except ValueError:
    print('Digite um número válido! ')  