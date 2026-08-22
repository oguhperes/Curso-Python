# Calcular se ano é Bissexto

try:
    print('\nO ano é Bissexto? ')
    ano = int(input('Digite um ano: '))
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
       print('Seu ano é Bissexto! ')
    else:
        print('Seu ano não é Bissexto! ')

except ValueError:
    print('Digite um número válido! ')
        


