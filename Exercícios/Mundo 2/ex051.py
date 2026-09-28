# Fazer um programa que leia o sexo de uma pessoa, mas só aceite
# os valores 'M' ou 'F'. Caso esteja errado, peça novamente, até
# ter o correto

while True:
    nome = input('\nInforme seu sexo [M/F]: ').lower().strip()
    if nome != 'm' and nome != 'f':
        print('Digite um sexo válido! ')
        continue
    else:
        print('Confirmado! ')
        break